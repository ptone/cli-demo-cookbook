import time
from flask import Flask, request, jsonify, Response, redirect, make_response

app = Flask(__name__)

# Authentication
@app.route('/auth', methods=['POST'])
def auth():
    return jsonify({"token": "secret-token"})

# Expanded HTTP Methods
@app.route('/resource', methods=['GET', 'POST', 'PUT', 'DELETE'])
def resource():
    if request.method == 'GET':
        return jsonify({"message": "GET request successful"})
    elif request.method == 'POST':
        return jsonify({"message": "POST request successful", "data": request.get_json()})
    elif request.method == 'PUT':
        return jsonify({"message": "PUT request successful", "data": request.get_json()})
    elif request.method == 'DELETE':
        return jsonify({"message": "DELETE request successful"})

# Query Parameters
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q', 'default')
    return jsonify({"query": query})

# Diverse Content Types
@app.route('/content', methods=['GET'])
def content():
    accept_header = request.headers.get('Accept')
    if 'application/xml' in accept_header:
        return Response('<message>XML Content</message>', mimetype='application/xml')
    else:
        return jsonify({"message": "JSON Content"})

# Simulated Latency
@app.route('/slow', methods=['GET'])
def slow():
    time.sleep(5)
    return "This was slow"

# Redirects
@app.route('/redirect', methods=['GET'])
def do_redirect():
    return redirect('/destination', code=302)

@app.route('/destination', methods=['GET'])
def destination():
    return "Redirected to destination"

# Error Simulation
@app.route('/error', methods=['GET'])
def error():
    return "Internal Server Error", 500

# Cookie Management
@app.route('/set-cookie', methods=['GET'])
def set_cookie():
    resp = make_response("Cookie has been set")
    resp.set_cookie('session_id', '12345')
    return resp

@app.route('/get-cookie', methods=['GET'])
def get_cookie():
    session_id = request.cookies.get('session_id')
    if session_id == '12345':
        return "Cookie received"
    return "Cookie not found", 404

if __name__ == '__main__':
    app.run(debug=True, port=5001)
