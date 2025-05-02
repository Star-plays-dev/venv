from flask import Flask, request, redirect, url_for, send_from_directory , render_template
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'skins'
app.config['SKINS_FOLDER'] = 'capes'

# Ensure the upload and skins folders exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['SKINS_FOLDER'], exist_ok=True)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/skins/<path:filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/capes/<path:filename>')
def uploaded_skin(filename):
    return send_from_directory(app.config['SKINS_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)