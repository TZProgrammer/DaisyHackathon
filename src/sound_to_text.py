import whisper


def transcribe(path, model):
    transcription = model.transcribe(path)
    return transcription

def main():
    model = whisper.load_model("base")
    data_stream_path = "../data/recorded_data/record_stream.mp3"

    transcription = transcribe(data_stream_path, model)
    print(transcription["text"])

    # Save transcription
    with open(f"../results/stream/transcription.txt", "w") as out_transcription:
        out_transcription.write(transcription["text"])


if __name__ == "__main__":
    main()