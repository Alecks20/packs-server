from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import os
from fastapi.staticfiles import StaticFiles

app = FastAPI()
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

def get_unique_filename(directory: str, filename: str) -> str:
    base, ext = os.path.splitext(filename)
    counter = 1
    new_filename = filename
    while os.path.exists(os.path.join(directory, new_filename)):
        new_filename = f"{base}({counter}){ext}"
        counter += 1

    return new_filename

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    unique_name = get_unique_filename(UPLOAD_FOLDER, file.filename)
    file_path = os.path.join(UPLOAD_FOLDER, unique_name)

    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)

    return JSONResponse({
        "message": "File uploaded successfully",
        "filename": unique_name,
        "url": f"https://packs.alecks.dev/uploads/{unique_name}"
    })