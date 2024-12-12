import subprocess
import platform
from flask import Flask, request, jsonify, send_file

app = Flask(__name__)

@app.route('/test_latency', methods=['POST'])
def test_latency():
    target = request.json.get('target', '')
    if not target:
        return jsonify({"error": "No target provided"}), 400

    # Determine the ping command based on the operating system
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    cmd = ['ping', param, '4', target]

    try:
        # Run the ping command
        output = subprocess.check_output(cmd, universal_newlines=True, stderr=subprocess.STDOUT)
        return jsonify({"output": output})
    except subprocess.CalledProcessError as e:
        return jsonify({"output": f"Ping failed. Details: {e.output}"}), 200
    except Exception as e:
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500

@app.route('/')
def home():
    return send_file("templates/index.html")

if __name__ == '__main__':
    app.run(debug=True)
