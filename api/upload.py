import os

from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

from services.ingestion_service import IngestionService

router = APIRouter()

UPLOAD_DIR = "data/uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload/pdf")
async def upload_pdf(file: UploadFile = File(...)):

    if not file.filename.endswith(".pdf"):
        return {
            "error": "Only PDF files are allowed"
        }

    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(file_path, "wb") as pdf_file:
        pdf_file.write(await file.read())

    result = IngestionService.process_pdf(
        file_path=file_path,
        file_name=file.filename
    )

    return {
        "status": "success",
        "data": result
    }