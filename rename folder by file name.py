import os


# Function to rename folders based on the first .mp4 file found
def rename_folders_with_mp4(directory_path):
    # Loop through each item in the directory
    for folder_name in os.listdir(directory_path):
        folder_path = os.path.join(directory_path, folder_name)

        # Ensure it's a directory
        if os.path.isdir(folder_path):
            # Initialize a variable to hold the new folder name
            new_folder_name = None

            # Look for .mp4 files within the folder
            for file_name in os.listdir(folder_path):
                if file_name.endswith('.mp4'):
                    new_folder_name = os.path.splitext(file_name)[0]  # Get the filename without extension
                    break  # Exit the loop after the first .mp4 is found

            # If an .mp4 file was found, rename the folder
            if new_folder_name:
                new_folder_path = os.path.join(directory_path, new_folder_name)

                # Rename the folder
                os.rename(folder_path, new_folder_path)
                print(f'Renamed "{folder_name}" to "{new_folder_name}"')


# Main function to start processing
def main():
    # Directory containing multiple folders
    directory_path = input("Enter the path to the directory containing folders: ")

    # Rename folders based on .mp4 filenames
    rename_folders_with_mp4(directory_path)


if __name__ == "__main__":
    main()
