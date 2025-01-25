# DUST2: Dynamic Unified Structured Tensors

## Overview

DUST2 is a cutting-edge framework designed for dynamically storing, updating, and querying tensor-based data structures in real time. It’s the foundation for a new era of data manipulation and analysis, allowing relational insights and temporal tracking with unparalleled flexibility and efficiency. The framework is ideal for applications such as patient management systems, IoT sensor networks, and any domain requiring structured, multi-dimensional data storage and retrieval.

---

## Achievements

### Core Features

1. **Patient Creation:**

   - Seamlessly add new patients to the system, creating a unique tensor for each patient.
   - Example:
     ```bash
     curl -X POST -H "Content-Type: application/json" -d '{"name": "John"}' http://127.0.0.1:5000/create
     ```
2. **Tensor Updates:**

   - Dynamically update patient tensors with new data points.
   - Example:
     ```bash
     curl -X POST -H "Content-Type: application/json" -d '{"name": "John", "updates": [[0, 0, 98.6], [1, 1, 120]]}' http://127.0.0.1:5000/update
     ```
3. **Data Querying:**

   - Retrieve specific values or the entire tensor for a patient.
   - Example:
     ```bash
     curl "http://127.0.0.1:5000/query?name=John&x=0&y=0"
     ```
4. **Master Tensor Querying:**

   - Access a global view of all patients and their tensor indices.
   - Example:
     ```bash
     curl http://127.0.0.1:5000/query_master
     ```

---

## API Endpoints

### 1. `/create`

- **Method:** `POST`
- **Description:** Adds a new patient to the system and initializes their tensor.
- **Request Body:**
  ```json
  {
    "name": "John"
  }
  ```
- **Response:**
  ```json
  {
    "master_tensor": [
      {
        "id": 1,
        "name": "John",
        "tensor_index": 0
      }
    ],
    "message": "Patient 'John' added with tensor index 0"
  }
  ```

### 2. `/update`

- **Method:** `POST`
- **Description:** Updates the tensor for an existing patient.
- **Request Body:**
  ```json
  {
    "name": "John",
    "updates": [[0, 0, 98.6], [1, 1, 120]]
  }
  ```
- **Response:**
  ```json
  {
    "message": "Tensor updated for patient 'John'",
    "tensor": [
      [98.6, null, null],
      [null, 120.0, null],
      [null, null, null]
    ]
  }
  ```

### 3. `/query`

- **Method:** `GET`
- **Description:** Queries a specific value or the full tensor for a patient.
- **Query Parameters:**
  - `name`: Name of the patient (required).
  - `x`: X-axis index (optional).
  - `y`: Y-axis index (optional).
- **Example:**
  ```bash
  curl "http://127.0.0.1:5000/query?name=John&x=0&y=0"
  ```
- **Response:**
  ```json
  {
    "value": 98.6
  }
  ```

### 4. `/query_master`

- **Method:** `GET`
- **Description:** Retrieves the master tensor, showing all patients and their tensor indices.
- **Response:**
  ```json
  {
    "master_tensor": [
      {
        "id": 1,
        "name": "John",
        "tensor_index": 0
      }
    ]
  }
  ```

---

## Technical Innovations

### 1. **Dynamic Tensor Expansion**

- The tensors are dynamically resized during updates, ensuring no constraints on dimensional growth.
- Ensures that data storage scales with the complexity of the system.

### 2. **Master Tensor Management**

- Maintains a global index of all patients and their associated tensors.
- Enables seamless querying and management of multi-dimensional data.

### 3. **Lightweight and Modular Design**

- Built on Flask for simplicity and scalability.
- Modular components allow easy extension and integration with other systems.

---

## Future Enhancements

1. **Advanced Querying:**

   - Add conditional queries (e.g., all values above a certain threshold).
2. **Multi-Dimensional Tensors:**

   - Introduce additional dimensions for time-series data.
3. **Visualization Tools:**

   - Integrate Plotly Dash for real-time tensor visualization.
   - Add graph-based views for relationships and trends.
4. **Deployment:**

   - Dockerize the application for scalable deployment.
   - Host on cloud platforms like AWS, GCP, or Azure.
5. **Enhanced Security:**

   - Add authentication and authorization for secure access.
6. **Audit Logging:**

   - Track all tensor updates and queries for traceability.

---

## Usage Examples

### Adding a Patient

```bash
curl -X POST -H "Content-Type: application/json" -d '{"name": "Jane"}' http://127.0.0.1:5000/create
```

### Updating a Tensor

```bash
curl -X POST -H "Content-Type: application/json" -d '{"name": "Jane", "updates": [[0, 0, 97.8], [1, 1, 110]]}' http://127.0.0.1:5000/update
```

### Querying Data

#### Specific Value

```bash
curl "http://127.0.0.1:5000/query?name=Jane&x=0&y=0"
```

#### Full Tensor

```bash
curl "http://127.0.0.1:5000/query?name=Jane"
```

### Querying the Master Tensor

```bash
curl http://127.0.0.1:5000/query_master
```

---

## Conclusion

DUST2 is more than just a data management system; it’s a scalable, dynamic, and extensible framework that can revolutionize how we handle structured and multi-dimensional data. By combining simplicity with power, DUST2 sets the stage for groundbreaking innovations in data-driven applications.

Let’s keep building, iterating, and turning DUST2 into a game-changing platform. 🚀
