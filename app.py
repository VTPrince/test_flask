from flask import request,Flask
from flask import jsonify
app = Flask(__name__)
@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    return '<h1>ip : '+request.remote_addr
if __name__ == '__main__':
    app.run(debug=True)
