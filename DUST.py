from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

# Master tensor and data tensors
master_tensor = []
data_tensors = []

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

@app.route('/create', methods=['POST'])
def create_patient():
    data = request.json
    name = data.get('name')
    if not name:
        return jsonify({"error": "Patient name is required"}), 400

    # Create initial tensor for the patient
    tensor_index = add_to_master(name)
    initial_tensor = np.full((3, 3), np.nan)  # Example tensor dimensions
    data_tensors.append(initial_tensor)
    
    return jsonify({
        "message": f"Patient '{name}' added with tensor index {tensor_index}",
        "master_tensor": master_tensor
    })

@app.route('/update', methods=['POST'])
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

    return jsonify({
        "message": f"Tensor updated for patient '{name}'",
        "tensor": patient_tensor.tolist()
    })
    
@app.route('/query', methods=['GET'])
def query_tensor():
    name = request.args.get('name')
    x = request.args.get('x', type=int)
    y = request.args.get('y', type=int)

    # Find the patient's tensor
    patient = find_patient(name)
    if not patient:
        return jsonify({"error": f"Patient '{name}' not found"}), 404
    
    tensor_index = patient['tensor_index']
    patient_tensor = data_tensors[tensor_index]

    # Return specific value or full tensor
    if x is not None and y is not None:
        if x >= patient_tensor.shape[0] or y >= patient_tensor.shape[1]:
            return jsonify({"error": "Index out of bounds"}), 400
        return jsonify({"value": patient_tensor[x, y]})
    else:
        return jsonify({"tensor": patient_tensor.tolist()})
    
if __name__ == '__main__':
    app.run(debug=True)