import whisper
import torch
from whisper import Whisper
from tempfile import NamedTemporaryFile
from app.models.transcription_model import TranscriptionResult


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = whisper.load_model("base", device=device)


class TranscriptionService:
    def __init__(self, model: Whisper):
        self.model = model

    def transcribe_audio(self, files) -> list[TranscriptionResult]:
        results = []
        for file in files:
            with NamedTemporaryFile(delete=True) as temp:
                with open(temp.name, "wb") as temp_file:
                    temp_file.write(file.file.read())

                result = self.model.transcribe(temp.name)
                results.append(
                    TranscriptionResult(
                        filename=file.filename,
                        transcript=result.get("text"),
                        language=result.get("language")
                    )
                )
        return results


def get_transcription_service():
    return TranscriptionService(model)
