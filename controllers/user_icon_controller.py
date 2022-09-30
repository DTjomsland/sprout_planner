import os
from flask import Blueprint, jsonify, request, Flask, render_template, current_app
from main import db
from models.user_icon import UserIcon
from flask_jwt_extended import jwt_required
from schemas.user_icon_schema import user_icon_schema, user_icons_schema
import cloudinary
import cloudinary.uploader
import cloudinary.api
from dotenv import load_dotenv
from flask_cors import cross_origin
from flask import jsonify
from flask import Flask,render_template, request
load_dotenv()






# Default route for all user icon requests
user_icon = Blueprint('user_icon', __name__, url_prefix='/usericon')

# Get request for user icon linked with a specific activity

@user_icon.route('/<int:user_activity_id>', methods=['GET'])
def get_user_icons(user_activity_id):
    user_icons = db.session.query(UserIcon).with_entities(UserIcon.user_icon_url).filter(UserIcon.user_activity_id == user_activity_id)
    result = user_icons_schema.dump(user_icons)
    return jsonify(result)

@user_icon.route("/<int:user_activity_id>/upload", methods=['POST'])
@jwt_required()
@cross_origin()
def upload_file(user_activity_id):
    current_app.logger.info('in upload route')
    cloudinary.config(cloud_name = os.getenv('CLOUD_NAME'), api_key=os.getenv('API_KEY'), api_secret=os.getenv('API_SECRET'))
    upload_result = None
    if request.method == 'POST':
        file_to_upload = request.files['file']
        current_app.logger.info('%s file_to_upload', file_to_upload)
        if file_to_upload:
            upload_result = cloudinary.uploader.upload(file_to_upload)
            current_app.logger.info(upload_result)
            current_app.logger.info(type(upload_result))
            activity = user_activity_id
            image_url = upload_result.get('url')
            icon = UserIcon(
                user_icon_url = image_url,
                user_activity_id = activity
            )       
            db.session.add(icon)
            db.session.commit()
            return jsonify((user_icon_schema).dump(icon))

# Delete user icon
@user_icon.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_icon(id):
    # Find the category by id
    icon = UserIcon.query.get(id)
    # Display error if category is not found
    if not icon:
        return {"error": "Image not found"}
    # Delete the category from the database (Deletes all associated activities)
    db.session.delete(icon)
    # Save the changes in the database
    db.session.commit()
    # Return message if deleted successfully
    return {"message": "Image deleted successfully"}