import whisper # pyright: ignore[reportMissingImports]

model = whisper.load_model("large-v2")

result = model.transcribe(audio = "Audios/ ",
                          language = "hi",
                          task = "translate")

print(result["text"]) 