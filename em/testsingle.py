import requests

# Flask app URL (replace with your deployed app's URL if running on a server)
url = "http://127.0.0.1:5000/predict"

# Single sample input
input_data = {
    "Plaintext": "AABBCCDD",
    "Encryption Key": "FFEEDDCC",
    "EM Traces": "-0.009514566014924373 -0.013724001130807649 0.9403457480180761 0.8942119968142345 -0.017500740743369946 1.0340090701597553"
}

# Send the request
try:
    print(f"Sending input: {input_data}")
    response = requests.post(url, json=input_data)
    
    # Check for a successful response
    if response.status_code == 200:
        print(f"Response: {response.json()}")
    else:
        print(f"Error: Received status code {response.status_code}")
        print(f"Message: {response.json()}")
except Exception as e:
    print(f"Error: {e}")
