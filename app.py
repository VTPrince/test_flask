from flask import request,Flask
from flask import jsonify
app = Flask(__name__)
@app.route("/", methods=["GET"])
def main():
    if 'X-Forwarded-For' in request.headers:
        proxy_data = request.headers['X-Forwarded-For']
        ip_list = proxy_data.split(',')
        user_ip = 'np'+ip_list[1]  # first address in list is User IP
    else:
        user_ip = 'tp'+request.remote_addr
    return '<h1>ip : '+ user_ip #request.remote_addr
if __name__ == '__main__':
    app.run(debug=True)
