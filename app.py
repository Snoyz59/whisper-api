from fastapi import FastAPI, File, UploadFile
import whisper
import torch
import os

app = FastAPI()
model = whisper.load_model("base")  # Choisis tiny / base / small...

@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    # Sauvegarde temporaire du fichier
    temp_file = "temp_audio.ogg"
    contents = await file.read()
    with open(temp_file, "wb") as f:
        f.write(contents)

    # Transcription
    result = model.transcribe(temp_file, language="fr")
    os.remove(temp_file)  # Nettoyer
    return {"text": result["text"]}
