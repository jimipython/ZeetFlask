import json
import base64

from flask import Flask, request

app = Flask(__name__)

def decode_base64(data):
    try:
        decoded_data = base64.b64decode(data)
        return decoded_data.decode('utf-8')
    except Exception as e:
        return f"Error decoding base64 data: {str(e)}"

@app.route('/handle_post', methods=['POST'])
def handle_post():
    try:
        data = request.get_json()  # assuming incoming data is in JSON format
        if 'data' in data and isinstance(data['data'], dict):
            for key, value in data['data'].items():
                if isinstance(value, str):
                    decoded_value = decode_base64(value)
                    data['data'][key] = decoded_value
            # Process the modified data as needed
            print("Received data:", data)
            # You can return a response if needed
            return "POST request handled successfully"
        else:
            return "Invalid JSON format. 'data' parameter with key-value pairs expected."

    except Exception as e:
        return f"Error processing POST request: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
