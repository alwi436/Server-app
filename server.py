from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run', methods=['POST'])
def run():
    data = request.get_json()
    cmd = data.get('cmd')

    try:
        result = subprocess.check_output(
            cmd, shell=True, stderr=subprocess.STDOUT, text=True, timeout=5
        )
    except subprocess.CalledProcessError as e:
        result = e.output
    except Exception as e:
        result = f"Error: {str(e)}"
    return result

if __name__ == '__main__':
    app.run(debug=True)