from flask import Flask, jsonify
import gdown
app = Flask(__name__)

@app.route('/run-colab')
def run_colab():
    gdown.download('https://drive.google.com/file/d/1D2WfRcEjou6aJG6DxFAlo_gmVmzeH8vj', 'tradingBot.ipynb', quiet=False)
    return jsonify(message='colab notebook ran successfully')
