import logging
from faster_whisper import WhisperModel, BatchedInferencePipeline

# Would prefer to add more customisation to logger
logging.basicConfig()
logging.getLogger("faster_whisper").setLevel(logging.INFO)

# Explanation: used for testing. Would be good to move this into a config file
model_size = "tiny"

# cuda vs cpu. see https://github.com/SYSTRAN/faster-whisper
# Explanation: would like to experiment more with finding the fastest model
#              The documentation suggested using batched and int8 for fastest results
logging.INFO("Setting up model...")
model = WhisperModel(model_size, device="cpu", compute_type="int8")
batched_model = BatchedInferencePipeline(model=model)

# Explanation: main function for using model. Would be interesting to see other potential uses such as VAD filter
async def transcribe_file(audio_file):
    logging.INFO("Starting audio transcription...")
    segments, info = batched_model.transcribe(audio_file, batch_size=8)

    transcription = ""
    for segment in segments:
        # Explanation: handling as much logic here rather than the REST endpoints module
        transcription += f"[{round(segment.start,2)} -> {round(segment.end,2)}] {segment.text}"

    logging.INFO(f"transcription: {transcription}")

    return {
        "transcription": transcription,
        "language": info.language, "duration": info.duration,
        "latency": info.vad_options.min_silence_duration_ms
        }
