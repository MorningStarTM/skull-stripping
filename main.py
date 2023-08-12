import os
import cv2
from app import app
from preprocess import read_img, predict
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

model_names = ["Model 1", "Model 2", "Model 3"]

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
	
@app.route('/')
def upload_form():
	return render_template('upload.html', model_names=model_names)

@app.route('/', methods=['POST'])
def upload_image():
	if 'files[]' not in request.files:
		flash('No file part')
		return redirect(request.url)
	files = request.files.getlist('files[]')
	file_names = []
	images = []
	for file in files:
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file_names.append(filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
	message = predict("static\\uploads")

		#else:
		#	flash('Allowed image types are -> png, jpg, jpeg, gif')
		#	return redirect(request.url)

    

	return render_template('upload.html', filenames=file_names, model_names=model_names, message=message)

"""@app.route('/', methods=['POST'])
def predict():
    if request.method == "POST":
        message = predict("static\\uploads")
    return render_template('upload.html', message=message)
	"""

"""@app.route('/display/<filename>')
def display_image(filename):
	#print('display_image filename: ' + filename)
	return redirect(url_for('static', filename='uploads/' + filename), code=301)
"""
if __name__ == "__main__":
    app.run()