import os
import subprocess
import csv
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

LOG_FILE = "conversion_log.csv"

# Initialize the CSV log file if it doesn't exist (with headers)
def initialize_csv_log():
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w", newline="") as log:
            writer = csv.writer(log)
            writer.writerow(["Timestamp", "File Location", "Original Size (MB)", "Converted Size (MB)", "Saved Size (MB)"])

def find_videos(folder, extensions=('.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv', '.mts')):
    """Find all videos in a folder and its subfolders with given extensions."""
    video_files = []
    for root, _, files in os.walk(folder):
        for file in files:
            if file.lower().endswith(extensions):
                video_files.append(os.path.join(root, file))
    return video_files

def convert_video(input_file, output_file):
    """Convert video using HandBrakeCLI with the Apple VideoToolbox H265 4K preset."""
    command = [
        "HandBrakeCLI",
        "-i", input_file,
        "-o", output_file,
        "--preset", "H.265 Apple VideoToolbox 2160p 4K"
    ]
    try:
        subprocess.run(command, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error converting file {input_file}: {e}")
        return False

def log_conversion(input_file, output_file, original_size):
    """Log conversion details to a CSV file."""
    try:
        converted_size = os.path.getsize(output_file) / (1024 * 1024)  # Size in MB
        saved_size = original_size - converted_size  # Difference in MB
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Write to the CSV log file
        with open(LOG_FILE, "a", newline="") as log:
            writer = csv.writer(log)
            writer.writerow([timestamp, input_file, f"{original_size:.2f}", f"{converted_size:.2f}", f"{saved_size:.2f}"])
    except Exception as e:
        print(f"Error logging conversion for {input_file}: {e}")

def retain_original_timestamps(original_file, converted_file):
    """Retain the original file's timestamps for the converted file."""
    try:
        stat = os.stat(original_file)
        original_mtime = stat.st_mtime  # Modification time
        original_atime = stat.st_atime  # Access time

        os.utime(converted_file, (original_atime, original_mtime))
        print(f"Updated timestamps for {converted_file} to match {original_file}")
    except Exception as e:
        print(f"Error retaining timestamps for {converted_file}: {e}")

def process_video(video):
    print(f"Processing: {video}")
    temp_output = video + ".tmp.mp4"
    final_output = os.path.splitext(video)[0] + ".mp4"  # Ensure the output has .mp4 extension

    original_size = os.path.getsize(video) / (1024 * 1024)  # Save original size before deletion
    
    if convert_video(video, temp_output):
        try:
            retain_original_timestamps(video, temp_output)

            if os.path.exists(video):
                print(f"Deleting original file: {video}")
                os.remove(video)

            os.rename(temp_output, final_output)
            log_conversion(video, final_output, original_size)
            print(f"Converted and replaced: {video} -> {final_output}")
        except Exception as e:
            print(f"Error replacing file {video}: {e}")
    else:
        if os.path.exists(temp_output):
            os.remove(temp_output)

def process_folder(folder):
    videos = find_videos(folder)
    with ThreadPoolExecutor(max_workers=4) as executor:  # Adjust the number of workers
        executor.map(process_video, videos)

if __name__ == "__main__":
    initialize_csv_log()  # Initialize the CSV file with headers
    source_folder = input("Enter the path to the folder with videos: ").strip()
    
    # Normalize the folder path
    source_folder = os.path.expanduser(source_folder.strip("'\""))
    
    if os.path.isdir(source_folder):
        process_folder(source_folder)
        print(f"Conversion completed. Log saved to '{LOG_FILE}'.")
    else:
        print(f"Invalid folder path: {source_folder}")
