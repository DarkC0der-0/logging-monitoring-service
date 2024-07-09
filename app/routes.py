from flask import Blueprint, request, jsonify, current_app
from werkzeug.utils import secure_filename
from app import db
from app.models import Image 
from app.utils import allowed_file, process_image
import os

bp = Blueprint('main', __name__)

@bp.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error', 'No selected file'}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        process_image(filepath)
        new_image = Image(filename=filename)
        db.session.add(new_image)
        db.session.commit()
        return jsonify({'message': 'Image uploaded and processed'}), 201
    return jsonify({'error': 'File type not allowed'}), 400