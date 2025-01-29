from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust the origins as needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_current_datetime():
    return datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")

@app.get("/getUserInfo")
def root():
    return {
            "email": "chisomedoka48@gmail.com",
            "current_datetime": get_current_datetime(),
            "github_url": "https://github.com/chizzyedoka"
            }