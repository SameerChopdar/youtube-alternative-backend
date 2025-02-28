from fastapi import FastAPI, UploadFile, File
import shutil
import os

# Create FastAPI app
app = FastAPI()

# Define the storage folder for videos
VIDEO_STORAGE = "videos"
os.makedirs(VIDEO_STORAGE, exist_ok=True)

@app.get("/")
def home():
    return {"message": "Welcome to YouTube Alternative API"}

# Upload Video API
@app.post("/upload/")
async def upload_video(file: UploadFile = File(...)):
    file_location = f"{VIDEO_STORAGE}/{file.filename}"
    
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"message": "Video uploaded successfully", "file": file.filename}
