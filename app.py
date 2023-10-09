
from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scriptit')
def scriptit():
    return render_template('scriptit.html')

@app.route('/lab1_1_inst')
def lab1_inst():
    return render_template('lab1_1_inst.html')

@app.route('/lab1_1')
def lab1():
    return render_template('lab1_1.html')

@app.route('/run_script', methods=['POST'])
def run_script():
    if request.method == 'POST':
        script_file = 'saveconfigs.py'  
        try:
            result = subprocess.check_output(['python', script_file], universal_newlines=True, stderr=subprocess.STDOUT)
            return result
        except subprocess.CalledProcessError as e:
            return str(e.output)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
