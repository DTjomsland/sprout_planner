import os
from main import db
from flask import Blueprint, jsonify, request, current_app
from models.user_feeling_icon import UserFeelingIcon
from flask_jwt_extended import jwt_required
from schemas.user_feeling_icon_schema import user_feeling_icon_schema, user_feeling_icons_schema
from dotenv import load_dotenv
from flask_cors import cross_origin
from flask import jsonify
import cloudinary
import cloudinary.uploader
import cloudinary.api


load_dotenv()


# Default route for all user feeling icon requests
user_feeling_icon = Blueprint('user_feeling_icon', __name__, url_prefix='/userfeelingicon')

# Get request for user feeling icon linked with a specific feeling
@user_feeling_icon.route('/<int:user_feeling_id>', methods=['GET'])
def get_user_feeling_icons(user_feeling_id):
    # Search for all instances in the feeling icon table where a row contains the feeling_id
    icons = db.session.query(UserFeelingIcon).with_entities(UserFeelingIcon.user_feeling_icon_id, UserFeelingIcon.user_feeling_icon_url).filter(UserFeelingIcon.user_feeling_id == user_feeling_id)
    # Returns jsonified feeling icon for the specific feeling
    result = user_feeling_icons_schema.dump(icons)
    return jsonify(result)

    
# Upload a photo to Cloudinary and input its url into the database
# Associated with a specific feeling ID
@user_feeling_icon.route("/<int:user_feeling_id>/upload", methods=['POST'])
@jwt_required()
@cross_origin()
def upload_file(user_feeling_id):
    # Rename router variable
    feeling = user_feeling_id
    # Check to see if the feeling has an image.  Return error if it does. (Shouldn't be prompted more than once in actual app.  For test use only)
    image_check = UserFeelingIcon.query.filter_by(user_feeling_id = feeling).first()
    if image_check:
        return {"error": "An image is already associated with this feeling."}
    current_app.logger.info('in upload route')
    # Pulls Cloudinary information fromm .env
    cloudinary.config(cloud_name = os.getenv('CLOUD_NAME'), api_key=os.getenv('API_KEY'), api_secret=os.getenv('API_SECRET'))
    upload_result = None
    # Enables retrieval of client data
    if request.method == 'POST':
        file_to_upload = request.files['file']
        current_app.logger.info('%s file_to_upload', file_to_upload)
        # Uploads the result to Cloudinary/catches error if the file type is wrong
        if file_to_upload:
            try:
                upload_result = cloudinary.uploader.upload(file_to_upload)
            except Exception:
                return {"error": "Please choose a valid file type."}
            current_app.logger.info(upload_result)
            current_app.logger.info(type(upload_result))
            # Create variable that is equal only to the image url.(Cloudinary returns quite a bit of extra info)
            image_url = upload_result.get('url')
            # Create a new feeling icon object from the returned url and route variable
            icon = UserFeelingIcon(
                user_feeling_icon_url = image_url,
                user_feeling_id = feeling
            )       
            db.session.add(icon)
            db.session.commit()
            return jsonify((user_feeling_icon_schema).dump(icon))

# Delete user feeling icon
@user_feeling_icon.route("/<int:user_feeling_icon_id>", methods=["DELETE"])
@jwt_required()
def delete_icon(user_feeling_icon_id):
    # Find the feeling icon by id
    icon = UserFeelingIcon.query.get(user_feeling_icon_id)
    # Display error if feeling icon is not found
    if not icon:
        return {"error": "Image not found"}
    # Delete the feeling icon
    db.session.delete(icon)
    # Save the changes in the database
    db.session.commit()

    # Return message if deleted successfully
    return {"message": "Image deleted successfully"}

