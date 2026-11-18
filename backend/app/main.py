from fastapi import FastAPI
from datetime import datetime, timezone

app = FastAPI(
    title="CloudPulse AI",
    description="Centralized Logging and Distributed Application Monitoring Platform",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "project": "CloudPulse AI",
        "message": "Cloud monitoring backend is running",
        "status": "operational",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "CloudPulse AI Backend"
    }