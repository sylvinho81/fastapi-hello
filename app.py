import os
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import APIKeyHeader
from typing import Dict

# Get environment variables
API_TOKEN = os.getenv("API_TOKEN")
MESSAGE = os.getenv("MESSAGE", "World")  # Default to "World" if not set

# Check if API_TOKEN is set
if not API_TOKEN:
    raise ValueError("API_TOKEN environment variable is not set")

app = FastAPI(title="Hello API", description="A simple API with token authentication")

# Token authentication
api_key_header = APIKeyHeader(name="X-API-Key")

async def get_api_key(api_key: str = Depends(api_key_header)):
    if api_key != API_TOKEN:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key",
        )
    return api_key

@app.get("/", dependencies=[Depends(get_api_key)])
async def root() -> Dict[str, str]:
    return {"message": f"Hello, {MESSAGE}"}

@app.get("/health")
async def health_check() -> Dict[str, str]:
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True) 