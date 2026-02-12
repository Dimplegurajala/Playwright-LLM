from flask import Flask, jsonify
from jsonschema import validate

app = Flask(__name__)

# Full schema matching the 'Add Contact' UI fields
CONTACT_SCHEMA = {
    "type": "object",
    "properties": {
        "firstName": {"type": "string"},
        "lastName": {"type": "string"},
        "birthdate": {"type": "string"},
        "email": {"type": "string", "format": "email"},
        "phone": {"type": "string"},
        "street1": {"type": "string"},
        "street2": {"type": "string"},
        "city": {"type": "string"},
        "stateProvince": {"type": "string"},
        "postalCode": {"type": "string"},
        "country": {"type": "string"}
    },
    "required": ["firstName", "lastName", "email"]
}

@app.route('/mock/contact', methods=['GET'])
def mock_contact():
    # Mock data representing a successful API response
    data = {
        "firstName": "Dimple",
        "lastName": "SDET",
        "birthdate": "1995-01-01",
        "email": "dimple.qa@celcom.com",
        "phone": "8005551234",
        "street1": "123 Main St",
        "street2": "Apt 4B",
        "city": "Bangalore",
        "stateProvince": "KA",
        "postalCode": "560001",
        "country": "India"
    }
    validate(instance=data, schema=CONTACT_SCHEMA)
    return jsonify(data)

if __name__ == "__main__":
    app.run(port=5001) # Using 5001 to avoid common macOS/Windows conflicts