from flask import Flask, jsonify, send_file
import gdown
import os

app = Flask(__name__)

@app.route('/')
def download_notebook():
    # Define the Google Drive download URL
    download_url = 'https://drive.google.com/file/d/1D2WfRcEjou6aJG6DxFAlo_gmVmzeH8vj/view?usp=drive_link'
    output = '/tmp/tradingBot.ipynb'  # Use /tmp for temporary storage in serverless functions

    try:
        # Download the file
        gdown.download(download_url, output, quiet=False)
        
        # Optionally, you can return the file to the client
        return send_file(output, as_attachment=True, mimetype='application/json', 
                         attachment_filename='tradingBot.ipynb')
        
        # If you don't want to return the file, just confirm the download
        # return jsonify(message='Notebook downloaded successfully')
        
    except Exception as e:
        return jsonify(error=str(e)), 500
