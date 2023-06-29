from flask import render_template, request, jsonify
from werkzeug.utils import secure_filename
import PyPDF2
import json
import os

from app import app
from app.utils import allowed_file, extract_resume_data

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'resume' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    resume = request.files['resume']
    
    if resume.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if resume and allowed_file(resume.filename):
        filename = secure_filename(resume.filename)
        temp_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        resume.save(temp_path)
        
        extracted_data = extract_resume_data(temp_path)
        
        os.remove(temp_path)
        
        return jsonify(extracted_data), 200
    
    return jsonify({'error': 'Invalid file type'}), 400
