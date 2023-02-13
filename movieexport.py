import os
import shutil


def main():
    # Prompt user for the source directory to search for movie files
    src_dir = input("Enter the directory to search for movie files: ")

    # Check if the source directory exists
    if not os.path.isdir(src_dir):
        print("Error: The directory does not exist.")
        return

    # List to store the found movie files
    movie_files = []

    # Search for movie files in the source directory
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file.endswith((".mp4", ".mkv", ".avi", ".mov")):
                movie_files.append(os.path.join(root, file))

    # Check if any movie files were found
    if not movie_files:
        print("No movie files were found in the directory.")
        return

    # Prompt user for the destination directory to export the movie files to
    dest_dir = input("Enter the directory to export the movie files to: ")

    # Check if the destination directory exists
    if not os.path.isdir(dest_dir):
        print("Error: The destination directory does not exist.")
        return

    # Copy the found movie files to the destination directory
    for movie_file in movie_files:
        shutil.copy2(movie_file, dest_dir)

    print(f"Exported {len(movie_files)} movie files to {dest_dir}.")


if __name__ == "__main__":
    main()
