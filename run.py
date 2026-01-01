import os
import uvicorn
from app.main import app

port = int(os.environ.get("PORT", 9000))  # Render sets this automatically
host = "0.0.0.0"

if __name__ == "__main__":
    uvicorn.run(app, host=host, port=port)
