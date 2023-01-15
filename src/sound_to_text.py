import os
import time

import whisper


def transcribe(path, model):
    transcription = model.transcribe(path)
    return transcription

def main():
    model = whisper.load_model("base")
    data_stream_path = "../data/recorded_data/record_stream.mp3"

    if os.path.exists(data_stream_path) and os.path.isfile(data_stream_path):
        os.remove(data_stream_path)

    prev_mod_time = -1
    start = time.time()
    max_time = 100
    while time.time() - start < max_time:
        time.sleep(0.2)
        if(os.path.exists(data_stream_path) and os.stat(data_stream_path).st_mtime != prev_mod_time):
            prev_mod_time = os.stat(data_stream_path).st_mtime  
            transcription = transcribe(data_stream_path, model)
            print(transcription["text"])
            print()

            # Save transcription
            with open(f"../results/stream/transcription.txt", "w") as out_transcription:
                out_transcription.write(transcription["text"])


if __name__ == "__main__":
    main()