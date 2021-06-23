from flask import Flask,render_template
import jinja2,json
from authlib.flask.client import OAuth
from pdf2image import convert_from_path
app = Flask(__name__)

@app.route("/")
def home_view():
    
    imgsrc=r"C:\Users\sunny\OneDrive\Documents\GitHub\min_flask_template-main\app\TCP.JPG"
    return render_template('output.html',imgsrc=imgsrc)


@app.route("/abc",methods=["POST","GET"])
def abc():
    
    pages = convert_from_path(r"C:\Users\sunny\OneDrive\Documents\GitHub\min_flask_template-main\app\TCP.PDF", poppler_path=r"C:\Users\sunny\Downloads\Release-21.03.0 (1)\poppler-21.03.0\Library\bin")
    count = 0
    for page in pages:
     count +=1
     page.save('TCP'+'.jpg', 'JPEG')
     break
    imgsrc=r"C:\Users\sunny\OneDrive\Documents\GitHub\min_flask_template-main\app\TCP.JPG"
    return render_template('output.html',imgsrc=imgsrc)
