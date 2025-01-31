 

# HNG12 Stage 0 - Public API

## Description
This project is a simple public API developed for the HNG12 Stage 0 Backend Task. It provides basic information such as the registered email, the current datetime in ISO 8601 format, and a link to the project's GitHub repository.

## Technology Stack
- **Programming Language:** Python
- **Framework:** Flask
- **Deployment:** Publicly accessible endpoint (to be provided upon deployment)
- **CORS Handling:** Implemented using Flask-CORS

## Setup Instructions
### Prerequisites
Ensure you have the following installed:
- Python (>=3.6)
- pip (Python package manager)

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Olaiwonismail/HNG12-Stage-0.git
   ```
2. Navigate to the project directory:
   ```bash
   cd HNG12-Stage-0
   ```
3. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the Flask application:
   ```bash
   python app.py
   ```

## API Documentation
### Endpoint
**GET /**

### Response Format
**Success Response (200 OK):**
```json
{
  "email": "olaiwonismail@gmail.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/Olaiwonismail/HNG12-Stage-0"
}
```

### Features
- Accepts **GET** requests.
- Returns the required JSON response dynamically.
- Handles **CORS** properly.

## Deployment
The API is deployed at:
- **https://dayo1111.pythonanywhere.com/** 

## Related Resources
For more details about Python developers, check:
[Hire Python Developers](https://hng.tech/hire/python-developers)

---

## Author
Olaiwon Ismail

