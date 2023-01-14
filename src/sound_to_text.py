import whisper

model = whisper.load_model("base")

in_mp3 = "test_one_min"
result = model.transcribe(f"../data/test_mp3/{in_mp3}.mp3")

# Save transcription
with open(f"../result/test/result_{in_mp3}.txt", "w") as out_transcription:
    out_transcription.write(result["text"])