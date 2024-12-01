import requests

# Flask app URL (replace with your deployed app's URL if running on a server)
url = "http://127.0.0.1:5000/predict"

# Sample inputs with EM traces
sample_inputs = [
    {
        "Plaintext": "AABBCCDD",
        "Encryption Key": "FFEEDDCC",
        "EM Traces": "-0.009514566014924373 -0.013724001130807649 0.9403457480180761 0.8942119968142345 -0.017500740743369946 1.0340090701597553"
    },
    {
        "Plaintext": "11223344",
        "Encryption Key": "A1B2C3D4",
        "EM Traces": "0.8418147712689243 -0.025394775270929766 0.011301171440817716 1.1632388544719994 -0.006000990260594461 0.005833487339144985"
    },
    {
        "Plaintext": "XYZ12345",
        "Encryption Key": "5678ABCD",
        "EM Traces": "-0.006565745227460187 -0.0063642811656343225 0.8277286417384847 -0.002614745510521627 0.02713044076777904 -0.060533539289199086"
    }
]

# Test the Flask app with sample inputs
for i, input_data in enumerate(sample_inputs, 1):
    try:
        print(f"Test {i}: Sending input: {input_data}")
        response = requests.post(url, json=input_data)
        
        # Check for successful response
        if response.status_code == 200:
            print(f"Response: {response.json()}\n")
        else:
            print(f"Error: Received status code {response.status_code}")
            print(f"Message: {response.json()}\n")
    except Exception as e:
        print(f"Error during test {i}: {e}\n")
