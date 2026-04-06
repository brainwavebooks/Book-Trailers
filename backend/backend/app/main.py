from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "BookTrail API is running!"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/api/generate")
def generate():
    return {"task_id": "123", "status": "processing"}

@app.get("/api/status/{task_id}")
def status(task_id: str):
    return {"status": "completed", "video_url": "https://example.com/video.mp4"}
