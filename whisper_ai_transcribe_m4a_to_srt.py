import os
import whisper
import ffmpeg

# Initialize Whisper model
whisper_model = whisper.load_model("base")  # Use 'tiny', 'base', 'small', 'medium', or 'large'


# Function to transcribe audio and create .srt file
def transcribe_audio(audio_path, output_folder):
    # Perform transcription using Whisper
    result = whisper_model.transcribe(audio_path)

    # Generate .srt file from the transcription
    srt_filename = os.path.splitext(os.path.basename(audio_path))[0] + '.srt'
    srt_path = os.path.join(output_folder, srt_filename)

    with open(srt_path, 'w') as srt_file:
        for i, segment in enumerate(result['segments']):
            start = segment['start']
            end = segment['end']
            text = segment['text']

            # Write to .srt file in the correct format
            srt_file.write(f"{i + 1}\n")
            srt_file.write(f"{format_timestamp(start)} --> {format_timestamp(end)}\n")
            srt_file.write(f"{text}\n\n")


# Helper function to format time for .srt file
def format_timestamp(seconds):
    hrs, mins, secs = int(seconds // 3600), int((seconds % 3600) // 60), int(seconds % 60)
    millisecs = int((seconds - int(seconds)) * 1000)
    return f"{hrs:02}:{mins:02}:{secs:02},{millisecs:03}"


# Function to process all folders within a given directory
def process_folders_in_directory(directory_path):
    # Loop through each folder in the directory
    for folder_name in os.listdir(directory_path):
        folder_path = os.path.join(directory_path, folder_name)

        # Ensure it's a directory
        if os.path.isdir(folder_path):
            # Look for .m4a files within the folder
            for file_name in os.listdir(folder_path):
                if file_name.endswith('.m4a'):
                    audio_path = os.path.join(folder_path, file_name)

                    print(f"Transcribing audio: {audio_path}")
                    # Transcribe the .m4a file and generate the .srt file in the same folder
                    transcribe_audio(audio_path, folder_path)


# Main function to start processing
def main():
    # Directory containing multiple folders (each containing .m4a files)
    directory_path = input("Enter the path to the directory with folders containing .m4a files: ")

    # Process all folders in the directory
    process_folders_in_directory(directory_path)


if __name__ == "__main__":
    main()
