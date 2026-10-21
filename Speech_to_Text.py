import whisper
import os

file_name = input("Enter audio file name (with extension): ").strip()
lang = input("Enter language code (e.g., en, hi, ta) / (or press Enter for auto-detect): ").strip()
task = input("Enter task (transcribe/translate): ").strip().lower()
model_name = input("Choose model (tiny/base/small/medium/large-v3/turbo) / (or press Enter for Default): ").strip().lower()


if not model_name:
    model_name="small"
valid_model = { "tiny", "base", "small", "medium", "large-v3", "turbo" }

if not os.path.isfile(file_name):
    print("error : Audio file doesn't exist or found!")
elif task not in ("transcribe", "translate"):
    print("Error: Invalid task! Choose 'transcribe' or 'translate'.")
elif task == "translate" and model_name == "turbo":
    print("Disclaimer! Choose medium or large-v3 for translation.")
elif model_name not in valid_model:
    print("Error: Invalid model name!")
else:
    try:
        print(f"\nLoading Whisper model: {model_name}...")
        model = whisper.load_model(model_name)

        print("Processing audio...")
        result = model.transcribe(
        file_name,
        language=lang if lang else None,
        task=task)

        print("\n----output----")
        print(result["text"])

    except Exception as e:
        print(f"Error during transcription: {e}")
