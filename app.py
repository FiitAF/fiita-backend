from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from FiitA Backend!"

@app.route('/api/users', methods=['POST'])
def register_user():
    data = request.get_json()
    # Here you would typically save the user data to a database
    print(f"Received user registration data: {data}")
    return jsonify({"id": "123", "name": data.get("name")}), 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

