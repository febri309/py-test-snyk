from flask import Flask, request
import subprocess, yaml, requests
import jinja2

app = Flask(__name__)

@app.route("/ping")
def ping():
    host = request.args.get("host", "172.0.0.1")
    res = subprocess.check_output(f"ping -c 1 {host}", shell=True)
    return res

@app.route("/upload", methods=["POST"])
def upload():
    data = yaml.load(request.data, Loader=None)
    return {"ok": True, "data": str(data)}

@app.route("/fetch")
def fetch():
    url = request.args.get("url", "https://youtube.com")
    r = requests.get(url, verify=False)
    return r.text

if __name__ == "__main__":
    app.run(debug=True)