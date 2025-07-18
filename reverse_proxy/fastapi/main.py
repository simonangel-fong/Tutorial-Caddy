from fastapi import FastAPI
from os import environ

app = FastAPI()

# read env var
APP_NAME = environ.get("APP_NAME", "Unknown App")


@app.get("/")
async def root():
    return {
        "message": f"Current app: {APP_NAME}"
    }
