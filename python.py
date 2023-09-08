
from flask import Flask, request, jsonify

app = Flask(__name__)

# Replace these placeholders with your own data
user_id = "vs905964@gmail.com"
email = "vs905964@gmail.com"
roll_number = "RA2011003020087"

def find_highest_alphabet(data):
    alphabets = [char for char in data if char.isalpha()]
    if not alphabets:
        return []
    return [max(alphabets, key=lambda x: x.lower())]

@app.route('/bfhl', methods=['POST'])
def bfhl_post():
    try:
        data = request.json.get('data', [])
        numbers = [char for char in data if char.isdigit()]
        alphabets = [char for char in data if char.isalpha()]
        highest_alphabet = find_highest_alphabet(alphabets)

        response = {
            "is_success": True,
            "user_id": user_id,
            "email": email,
            "roll_number": roll_number,
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_alphabet": highest_alphabet,
        }

        return jsonify(response), 200
    except Exception as e:
        return jsonify({"is_success": False, "error_message": str(e)}), 400

@app.route('/bfhl', methods=['GET'])
def bfhl_get():
    response = {"operation_code": 1}
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
