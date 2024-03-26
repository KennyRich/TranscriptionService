from pydantic import BaseModel, Field


class TranscriptionResult(BaseModel):
    filename: str = Field(..., description="The name of the file")
    transcript: str = Field(..., description="The transcript of the audio file")
    language: str = Field(..., description="The language of the audio")


class TranscriptionResponse(BaseModel):
    results: list[TranscriptionResult] = Field(..., description="List of Transcription results")
