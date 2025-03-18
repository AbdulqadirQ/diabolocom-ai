from faster_whisper import WhisperModel

model_size = "large-v3"

# Run on GPU with FP16 //TODO CHANGE TO device="cpu", compute_type="int8"
model = WhisperModel(model_size, device="cuda", compute_type="float16")

# or run on GPU with INT8
# model = WhisperModel(model_size, device="cuda", compute_type="int8_float16")
# or run on CPU with INT8
# model = WhisperModel(model_size, device="cpu", compute_type="int8")

async def transcribe_file(audio_file):
    segments, info = model.transcribe(audio_file, beam_size=5)

    print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

    transcription = ""
    for segment in segments:
        transcription += "[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text)

    return transcription
