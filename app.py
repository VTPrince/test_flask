# import flask
# from flask import Flask
# from flask import request
# app = Flask(__name__)
# from flask import Flask, request

# app = Flask(__name__)

# @app.route('/')
# # def hello_world():
# #     ip_addr = request.remote_addr
# #     return '<h1> Your IP address is:' + ip_addr


# # @app.route("/get_my_ip", methods=["GET"])
# # def get_my_ip():
# #     ipadr=request.access_route[-1]
# #     return '<h1>You real ip address is: '+ipadr

# # @app.route('/client')
# # def client():
# #     ip_addr = request.environ['REMOTE_ADDR']
# #     return '<h1> YourClinet IP address is:' + ip_addr


# # @app.route('/proxy-client')
# # def proxy_client():
# #     ip_addr = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
# #     return '<h1> Your IP address is:' + ip_addr

# def hello_world():
#     return '<h1>New:'+request.environ.get('HTTP_X_REAL_IP', request.remote_addr)

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import request,Flask
from flask import jsonify
app = Flask(__name__)
@app.route("/", methods=["GET"])
def get_my_ip():
    return '<h1>ip : '+request.remote_addr
if __name__ == '__main__':
    app.run(debug=True)



