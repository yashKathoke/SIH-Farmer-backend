# Backend for farmer chatbot



### Prerequisites

### ⚙️ Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-project-name.git](https://github.com/your-username/your-project-name.git)
    cd your-project-name
    ```

2.  **Create and activate a virtual environment** (highly recommended):
    ```bash
    # For Linux/macOS
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### ▶️ Running the Application

This project uses **Uvicorn** as the ASGI server.

1.  **Start the server with auto-reload:**
    ```bash
    uvicorn app.main:app --reload
    ```
    *Note: Adjust `app.main:app` if your main application file and instance are located elsewhere (e.g., `main:app` if your app is in `main.py`).*

2.  The application will be accessible at:
    **http://127.0.0.1:8000**

---

## 📚 API Documentation

FastAPI automatically generates interactive documentation for all your endpoints:

* **Swagger UI:** Access the interactive documentation at **http://127.0.0.1:8000/docs**
* **ReDoc:** Access the alternative documentation at **http://127.0.0.1:8000/redoc**

---

## 📁 Project Structure

A typical, structured FastAPI layout:

Here is the full Markdown code for a FastAPI project README.md template. You can copy and paste this directly into your file.

Markdown

# [Project Title]

A concise, one-or-two-sentence description of what this FastAPI project does.

---

## 🚀 Getting Started

These instructions will help you set up and run a copy of the project on your local machine for development and testing.

### Prerequisites

You'll need **Python 3.8+** installed on your system.

### ⚙️ Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-project-name.git](https://github.com/your-username/your-project-name.git)
    cd your-project-name
    ```

2.  **Create and activate a virtual environment** (highly recommended):
    ```bash
    # For Linux/macOS
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### ▶️ Running the Application

This project uses **Uvicorn** as the ASGI server.

1.  **Start the server with auto-reload:**
    ```bash
    uvicorn app.main:app --reload
    ```
    *Note: Adjust `app.main:app` if your main application file and instance are located elsewhere (e.g., `main:app` if your app is in `main.py`).*

2.  The application will be accessible at:
    **http://127.0.0.1:8000**

---

## 📚 API Documentation

FastAPI automatically generates interactive documentation for all your endpoints:

* **Swagger UI:** Access the interactive documentation at **http://127.0.0.1:8000/docs**
* **ReDoc:** Access the alternative documentation at **http://127.0.0.1:8000/redoc**

---

## 📱 Using the Chatbot Endpoint for Mobile Apps

Mobile app developers can use the `/chat` endpoint to send user queries and receive responses from the chatbot. Below is an example of how to interact with this endpoint.

### Endpoint Details

- **URL:** `http://127.0.0.1:8000/chat/`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
        "query": "Your question here"
    }
    ```
- **Response:**
    ```json
    {
        "response": "Chatbot's answer here"
    }
    ```

### Example Usage

#### cURL Example
```bash
curl -X POST "http://127.0.0.1:8000/chat/" \
-H "Content-Type: application/json" \
-d '{"query": "What is the weather today?"}'
```

#### Flutter Example
```dart
import 'dart:convert';
import 'package:http/http.dart' as http;
void fetchChatbotResponse(String query) async {
    final url = Uri.parse("http://127.0.0.1:8000/chat/");
    final headers = {"Content-Type": "application/json"};
    final body = jsonEncode({"query": query});

    try {
        final response = await http.post(url, headers: headers, body: body);

        if (response.statusCode == 200) {
            final responseData = jsonDecode(response.body);
            print("Chatbot Response: ${responseData['response']}");
        } else {
            print("Error: ${response.statusCode}, ${response.body}");
        }
    } catch (e) {
        print("An error occurred: $e");
    }
}
```

### Notes
- Ensure the FastAPI server is running before making requests.
- Handle exceptions gracefully in your mobile app to account for potential server errors.
- Refer to the API documentation at **http://127.0.0.1:8000/docs** for more details.