import os
from flask import Blueprint, jsonify, request, current_app
from main import db
from flask_jwt_extended import jwt_required
from models.user_icon import UserIcon
from schemas.user_icon_schema import user_icon_schema, user_icons_schema
from dotenv import load_dotenv
from flask_cors import cross_origin
from flask import jsonify
import cloudinary
import cloudinary.uploader
import cloudinary.api



load_dotenv()


# Default route for all user icon requests
user_icon = Blueprint('user_icon', __name__, url_prefix='/usericon')


# Get request for user icon linked with a specific activity
@user_icon.route('/<int:user_activity_id>', methods=['GET'])
def get_user_icons(user_activity_id):
    # Search for all instances in the icon table where a row contains the activity_id
    icons = db.session.query(UserIcon).with_entities(UserIcon.user_icon_id, UserIcon.user_icon_url).filter(UserIcon.user_activity_id == user_activity_id)
    # Returns jsonified icon for the specific activity
    result = user_icons_schema.dump(icons)
    return jsonify(result)

# Upload a photo to Cloudinary and input its url into the database
# Associated with a specific activity ID
@user_icon.route("/<int:user_activity_id>/upload", methods=['POST'])
@jwt_required()
@cross_origin()
def upload_file(user_activity_id):
    # Rename router variable
    activity = user_activity_id
    # Check to see if the activity has an image.  Return error if it does. (Shouldn't be prompted more than once in actual app.  For test use only)
    image_check = UserIcon.query.filter_by(user_activity_id = activity).first()
    if image_check:
        return {"error": "An image is already associated with this activity."}

    current_app.logger.info('in upload route')
    # Pulls Cloudinary  information form .env
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
                return {"error": "Please choose a valid filetype."}
            current_app.logger.info(upload_result)
            current_app.logger.info(type(upload_result))
            # Create variable that is equal only to the image url.(Cloudinary returns quite a bit of extra info)
            image_url = upload_result.get('url')
            # Create a new icon object from the returned url and route variable
            icon = UserIcon(
                user_icon_url = image_url,
                user_activity_id = activity
            )       
            db.session.add(icon)
            db.session.commit()
            return jsonify((user_icon_schema).dump(icon))

# Delete user icon
@user_icon.route("/<int:user_icon_id>", methods=["DELETE"])
@jwt_required()
def delete_icon(user_icon_id):
    # Find the icon by id
    icon = UserIcon.query.get(user_icon_id)
    # Display error if icon is not found
    if not icon:
        return {"error": "Image not found"}
    # Delete the icon from the database
    db.session.delete(icon)
    # Save the changes in the database
    db.session.commit()

    # Return message if deleted successfully
    return {"message": "Image deleted successfully"}