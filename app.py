import cloudinary
import cloudinary.uploader
import cloudinary.api
import re

from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url
from flask import Flask, render_template, request,flash,redirect,url_for

cloudinary.config(
  cloud_name = "your_clod_name",
  api_key = "your_api_key",
  api_secret = "your_api_secret_key"
)

app = Flask(__name__)

allowed_extensions={'jpg','jpeg','png'}

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    upload_result = None
    upload_result2=None
    thumbnail_url1 = None
    thumbnail_url2 = None
    yo='harshy'
    folder_name='harsh/harsh/'+yo
    if request.method == 'POST':
        file_to_upload = request.files['file']
        file_to_upload2 = request.files['file2']
        z=(file_to_upload.filename.rsplit(".",1)[1].lower())
        print(file_to_upload.filename)
        if z in allowed_extensions:
            if file_to_upload and file_to_upload2:
                print('success')
                upload_result = cloudinary.uploader.upload(file_to_upload,folder=folder_name,width=200,height=100)
                upload_result2 = cloudinary.uploader.upload(file_to_upload2,folder="demo_images",width=200,height=100)
                thumbnail_url1, options = cloudinary_url(upload_result['public_id'], format="jpg", crop="fill", width=100,
                                                         height=100)
                thumbnail_url2, options = cloudinary_url(upload_result['public_id'], format="jpg", crop="fill", width=200,
                                                         height=100, radius=10, effect="sepia")
                print(thumbnail_url1)
                print(thumbnail_url2)
                print(upload_result['url'])
        else:
            print('failure')
            return redirect(url_for('upload_file')),flash("File format not suppoerted")
    return render_template('upload_form.html', upload_result=upload_result,upload_result2=upload_result2, thumbnail_url1=thumbnail_url1,
                           thumbnail_url2=thumbnail_url2)


if __name__ == "__main__":
    app.debug = True
    app.run()
