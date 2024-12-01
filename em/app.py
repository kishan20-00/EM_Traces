from flask import Flask, request, jsonify
import joblib
import numpy as np
import hashlib

app = Flask(__name__)

# Load the saved model
model_file = 'best_model.pkl'  # Ensure this path matches your saved model
model = joblib.load(model_file)

# Hash function for consistent encoding
def hash_value(val, max_hash=1e6):
    """Convert a value into a numerical hash."""
    return int(hashlib.md5(val.encode()).hexdigest(), 16) % int(max_hash)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Parse input JSON
        input_data = request.json
        
        # Extract required fields
        plaintext = input_data.get("Plaintext")
        encryption_key = input_data.get("Encryption Key")
        em_traces = input_data.get("EM Traces")
        
        if plaintext is None or encryption_key is None or em_traces is None:
            return jsonify({"error": "Missing required fields: 'Plaintext', 'Encryption Key', 'EM Traces'"}), 400

        # Hash the plaintext and encryption key
        plaintext_hashed = hash_value(plaintext)
        encryption_key_hashed = hash_value(encryption_key)
        
        # Parse EM traces and calculate the mean
        try:
            em_traces_parsed = np.array([float(val) for val in em_traces.split()])
            em_mean = np.mean(em_traces_parsed)
        except Exception as e:
            return jsonify({"error": f"Invalid EM Traces format: {str(e)}"}), 400
        
        # Prepare input for the model
        sample_input = np.array([[plaintext_hashed, encryption_key_hashed, em_mean]])
        
        # Predict using the loaded model
        prediction = model.predict(sample_input)
        prediction_label = "Vulnerable" if prediction[0] == 1 else "Not Vulnerable"
        
        # Return the prediction
        return jsonify({"Prediction": prediction_label})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
