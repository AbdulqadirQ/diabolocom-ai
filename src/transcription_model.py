from faster_whisper import WhisperModel, BatchedInferencePipeline

model_size = "tiny"

# cuda vs cpu. see https://github.com/SYSTRAN/faster-whisper
model = WhisperModel(model_size, device="cpu", compute_type="int8")
batched_model = BatchedInferencePipeline(model=model)

async def transcribe_file(audio_file):
    segments, info = batched_model.transcribe(audio_file, batch_size=8)

    print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

    transcription = ""
    for segment in segments:
        transcription += f"[{round(segment.start,2)} -> {round(segment.end,2)}] {segment.text}"

    return {
        "transcription": transcription,
        "language": info.language, "duration": info.duration,
        "latency": info.vad_options.min_silence_duration_ms
        }
