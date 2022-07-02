from flask import request,Flask
from flask import jsonify
import geocoder
app = Flask(__name__)
@app.route("/", methods=["GET"])
def main():
    if 'X-Forwarded-For' in request.headers:
        proxy_data = request.headers['X-Forwarded-For']
        ip_list = proxy_data.split(',')
        user_ip = ip_list[0]  # first address in list is User IP
    else:
        user_ip = request.remote_addr
    ip = geocoder.ip(user_ip)
    return '<h1>ip : '+ str(ip.city) #request.remote_addr
if __name__ == '__main__':
    app.run(debug=True)
