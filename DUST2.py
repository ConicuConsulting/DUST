from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

# Master tensor and data tensors
master_tensor = []
data_tensors = []
logs = []

# Helper: Add a new patient to the master tensor
def add_to_master(name):
    tensor_index = len(data_tensors)
    master_tensor.append({
        "id": len(master_tensor) + 1,
        "name": name,
        "tensor_index": tensor_index
    })
    return tensor_index

# Helper: Find a patient in the master tensor
def find_patient(name):
    for entry in master_tensor:
        if entry["name"] == name:
            return entry
    return None

# Route: Create a new patient
def create_patient():
    data = request.json
    name = data.get('name')

    # Check for duplicates
    if find_patient(name):
        return jsonify({"error": f"Patient '{name}' already exists"}), 400

    # Create a new tensor for the patient
    tensor_index = add_to_master(name)
    data_tensors.append(np.full((3, 3), np.nan))  # Initial tensor size

    logs.append(f"Created patient '{name}' with tensor index {tensor_index}")
    return jsonify({
        "message": f"Patient '{name}' added with tensor index {tensor_index}",
        "master_tensor": master_tensor
    })

# Route: Update a patient's tensor
def update_tensor():
    data = request.json
    name = data.get('name')
    updates = data.get('updates')  # List of tuples [(x, y, value), ...]

    # Find the patient's tensor
    patient = find_patient(name)
    if not patient:
        return jsonify({"error": f"Patient '{name}' not found"}), 404

    tensor_index = patient['tensor_index']
    patient_tensor = data_tensors[tensor_index]

    # Apply updates
    for update in updates:
        x, y, value = update
        if x >= patient_tensor.shape[0] or y >= patient_tensor.shape[1]:
            # Dynamically resize tensor if needed
            new_size = max(x, y) + 1
            new_tensor = np.full((new_size, new_size), np.nan)
            new_tensor[:patient_tensor.shape[0], :patient_tensor.shape[1]] = patient_tensor
            patient_tensor = new_tensor
            data_tensors[tensor_index] = patient_tensor
        patient_tensor[x, y] = value

    logs.append(f"Updated tensor for patient '{name}' with updates {updates}")
    return jsonify({
        "message": f"Tensor updated for patient '{name}'",
        "tensor": patient_tensor.tolist()
    })

# Route: Delete a patient and their tensor
def delete_patient():
    data = request.json
    name = data.get('name')

    # Find the patient
    patient = find_patient(name)
    if not patient:
        return jsonify({"error": f"Patient '{name}' not found"}), 404

    tensor_index = patient['tensor_index']
    master_tensor.remove(patient)
    data_tensors.pop(tensor_index)

    logs.append(f"Deleted patient '{name}' and their tensor")
    return jsonify({"message": f"Patient '{name}' and their tensor deleted"})

@app.route('/query', methods=['GET'])
def query_tensor():
    """
    Query a specific value or the full tensor for a patient.
    """
    name = request.args.get('name')
    x = request.args.get('x', type=int)
    y = request.args.get('y', type=int)

    # Check if name is provided
    if not name:
        return jsonify({"error": "Name parameter is required"}), 400

    # Find the patient's tensor
    patient = find_patient(name)
    if not patient:
        return jsonify({"error": f"Patient '{name}' not found"}), 404

    tensor_index = patient['tensor_index']
    patient_tensor = data_tensors[tensor_index]

    # If x and y are provided, query a specific value
    if x is not None and y is not None:
        if x >= patient_tensor.shape[0] or y >= patient_tensor.shape[1]:
            return jsonify({"error": "Index out of bounds"}), 400
        return jsonify({"value": patient_tensor[x, y]})
    else:
        # Return the full tensor if no x, y parameters are provided
        return jsonify({"tensor": patient_tensor.tolist()})

# Route: Query the entire master_tensor
def query_master():
    return jsonify({"master_tensor": master_tensor})

# Route: Log actions
def get_logs():
    return jsonify({"logs": logs})

# Add routes to the Flask app
app.add_url_rule('/create', 'create_patient', create_patient, methods=['POST'])
app.add_url_rule('/update', 'update_tensor', update_tensor, methods=['POST'])
app.add_url_rule('/delete', 'delete_patient', delete_patient, methods=['DELETE'])
app.add_url_rule('/query_master', 'query_master', query_master, methods=['GET'])
app.add_url_rule('/query', 'query', query_tensor, methods=['GET'])
app.add_url_rule('/logs', 'get_logs', get_logs, methods=['GET'])

if __name__ == '__main__':
    app.run(debug=True)
