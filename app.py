from flask import request,Flask
from flask import jsonify
app = Flask(__name__)
@app.route("/", methods=["GET"])

def main():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        return '<h1>new ip : '+request.environ['REMOTE_ADDR'])
    else:
        return '<h1>othernew ip : '+request.environ['HTTP_X_FORWARDED_FOR'])
if __name__ == '__main__':
    app.run(debug=True)
