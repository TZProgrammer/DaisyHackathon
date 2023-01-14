import wave

import pyaudio

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

def record_audio(num_seconds):
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    frames = []
    for i in range(int(RATE/CHUNK * num_seconds)):
        data = stream.read(CHUNK)
        frames.append(data)

    return p, frames

def save_audio(path, p, frames):
    wf = wave.open(path, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

def main():
    p, frames = record_audio(5)
    file_name = "record_stream"
    save_audio(f"../data/recorded_data/{file_name}.mp3", p, frames)

if __name__ == "__main__":
    main()