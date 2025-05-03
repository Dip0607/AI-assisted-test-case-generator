from flask import Flask, request, send_file
from flask_cors import CORS
from io import BytesIO
from werkzeug.utils import secure_filename
from utils import generate_test_cases
from url_extractor import extract_webpage_data, read_file_content,extract_urls
import logging

ALLOWED_ORIGINS = [
    "http://localhost:3000"  # Include this if you need local development
]

app = Flask(__name__)
#CORS(app)
CORS(app, resources={r"/*": {"origins": ALLOWED_ORIGINS}})

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'doc', 'docx'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



class InputData:
    def __init__(self, file=None, url=None, text=None):
        self.file = file
        self.url = url
        self.text = text

    @property
    def filename(self):
        return self.file.filename if self.file else ''

@app.route('/process_input/', methods=['POST'])
def process_input():
    input_data = InputData(
        file=request.files.get('file'),
        url=request.form.get('url'),
        text=request.form.get('text')
    )

    if not input_data.file or input_data.filename == '':
        return {'error': 'No file provided.'}, 400

    if not allowed_file(input_data.filename):
        return {'error': 'Invalid file type.'}, 400

    try:
        file_content = read_file_content(input_data.file)
        file_url=extract_urls(input_data.file)
        content, links = None, None
        if input_data.url:
            content, links = extract_webpage_data(input_data.url)
        
        csv_content = generate_test_cases(file_content,file_url,content, links, input_data.text)
        
        return send_file(
            BytesIO(csv_content.encode()),
            mimetype='text/csv',
            as_attachment=True,
            download_name=f'test_cases_{secure_filename(input_data.filename)}.csv'
        )
    except Exception as e:
        return {'error': f'An error occurred: {str(e)}'}, 500

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
