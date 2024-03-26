from fastapi import APIRouter, File, UploadFile, Depends, HTTPException
from fastapi.responses import JSONResponse
from loguru import logger
from typing import Final
from app.services.transcription_service import get_transcription_service
from app.models.transcription_model import TranscriptionResponse

router = APIRouter()
ALLOWED_EXTENSIONS: Final[set] = {"wav", "mp3", "m4a"}


@router.post("/transcribe", response_model=TranscriptionResponse)
async def transcribe_audio(files: list[UploadFile] = File(...), service=Depends(get_transcription_service)):
    if not files:
        raise HTTPException(status_code=400, detail="No files were provided")

    for file in files:
        file_extension = file.filename.split('.')[-1].lower()
        if file_extension not in ALLOWED_EXTENSIONS:
            logger.info(f"File extension '{file_extension}' not supported")
            raise HTTPException(status_code=400, detail="File type not supported.")

    results = service.transcribe_audio(files)
    return TranscriptionResponse(results=results)
