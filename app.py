from flask import request,Flask
from flask import jsonify
app = Flask(__name__)
@app.route("/", methods=["GET"])

def main():
    return '<h1>ip : '+request.remote_addr
if __name__ == '__main__':
    app.run(debug=True)
