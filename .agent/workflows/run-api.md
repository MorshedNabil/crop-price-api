---
description: How to run the Crop Price API locally
---

To run the Crop Price API on your local machine, follow these steps:

1. **Install Dependencies**
   Ensure you have all required packages installed, including the newly added `pandas`:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the FastAPI Server**
   Use `uvicorn` to start the development server with auto-reload enabled:
   ```bash
   python -m uvicorn app.main:app --reload
   ```

3. **Verify the API**
   Once the server is running, you can access the interactive API documentation (Swagger UI) at:
   `http://127.0.0.1:8000/docs`

4. **Testing the Endpoint**
   You can send a POST request to `http://127.0.0.1:8000/predict` with a JSON body like this:
   ```json
   {
     "state": "California",
     "district": "Central Valley",
     "prediction_date": "2025-12-23",
     "avg_temperature": 25.5,
     "avg_humidity": 60.2,
     "season": "Summer"
   }
   ```
