# DUST: Dynamic Unified Structured Tensors

DUST (Dynamic Unified Structured Tensors) is a groundbreaking framework for organizing, updating, and querying complex, multi-dimensional data structures efficiently. Designed for relational intelligence, DUST provides a robust platform for managing tensor-based data models in real-time.

## Key Features

- **Dynamic Tensor Creation:** Seamlessly create and manage tensors for storing multi-dimensional data.
- **Efficient Updates:** Update tensor values dynamically, with support for automatic resizing.
- **Intuitive Querying:** Retrieve specific values or entire tensors with simple queries.
- **Master Tensor Indexing:** Maintain an organized system of tensors with metadata.
- **Extensibility:** Ready for integration with RGNNs (Relational Graph Neural Networks) and other advanced AI models.

## Getting Started

### Prerequisites

- Python 3.8+
- Flask
- NumPy

Install dependencies:

```bash
pip install flask numpy
```

### Running the Application

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/dust.git
   cd dust
   ```
2. Start the Flask application:

   ```bash
   python app.py
   ```
3. Use `curl` or any API client (e.g., Postman) to interact with the endpoints.

## API Documentation

### Endpoints

#### Create a Patient

- **Endpoint:** `/create`
- **Method:** `POST`
- **Payload:**
  ```json
  {
    "name": "Patient Name"
  }
  ```
- **Response:**
  ```json
  {
    "message": "Patient 'Name' added with tensor index X",
    "master_tensor": [
      {
        "id": 1,
        "name": "Patient Name",
        "tensor_index": 0
      }
    ]
  }
  ```

#### Update a Patient Tensor

- **Endpoint:** `/update`
- **Method:** `POST`
- **Payload:**
  ```json
  {
    "name": "Patient Name",
    "updates": [[x, y, value], ...]
  }
  ```
- **Response:**
  ```json
  {
    "message": "Tensor updated for patient 'Name'",
    "tensor": [[...], [...]]
  }
  ```

#### Query a Patient Tensor

- **Endpoint:** `/query`
- **Method:** `GET`
- **Parameters:**

  - `name`: Patient name (required)
  - `x`: X-coordinate (optional)
  - `y`: Y-coordinate (optional)
- **Response:**

  - Specific value:
    ```json
    {
      "value": 98.6
    }
    ```
  - Full tensor:
    ```json
    {
      "tensor": [[...], [...]]
    }
    ```

#### Query Master Tensor

- **Endpoint:** `/query_master`
- **Method:** `GET`
- **Response:**
  ```json
  {
    "master_tensor": [
      {
        "id": 1,
        "name": "Patient Name",
        "tensor_index": 0
      }
    ]
  }
  ```

## Roadmap

### Short-Term Goals

1. Add support for multi-dimensional tensors.
2. Implement relationships between tensors (e.g., linking patients to doctors).
3. Introduce anomaly detection features.

### Long-Term Goals

1. Integrate with Plotly Dash for interactive visualizations.
2. Deploy on cloud platforms with Docker support.
3. Expand API functionality to include advanced querying and analytics.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License**. See the LICENSE file for details.

---

Happy tinkering with DUST! 🚀
