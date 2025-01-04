# Video Conversion Script

This Python script automates the process of converting videos in various formats to MP4 using **HandBrakeCLI** with the **Apple VideoToolbox H.265 4K** preset. The script processes all videos within a given folder (including subfolders), converts them to the MP4 format, and replaces the original files with the converted ones while retaining the original timestamps.

Additionally, it logs the conversion details, including file sizes and saved space, into a CSV file.

## Features

- **Batch Conversion**: Convert all video files (MP4, MOV, AVI, MKV, FLV, WMV, MTS) in a folder and its subfolders.
- **Preserve Timestamps**: Retain the original file's creation and modification timestamps for the converted file.
- **File Replacement**: Replace the original video file with the converted one.
- **CSV Logging**: Generate a log file (`conversion_log.csv`) that includes the following details:
  - File location (path)
  - Original file size (in MB)
  - Converted file size (in MB)
  - Saved size (in MB)

## Requirements

- **Python 3.x**
- **HandBrakeCLI**: Install HandBrakeCLI for video conversion. You can download it from [here](https://handbrake.fr/downloads.php).
- **ThreadPoolExecutor**: To process files in parallel.

You can install required Python dependencies by running:

```bash
pip install subprocess csv os

Usage
	1.	Clone this repository or download the script files.
	•	You can clone it using the following command:

git clone https://github.com/Kristi-Tech/convert_videos.git


	2.	Ensure that HandBrakeCLI is installed and properly configured on your machine.
	•	You can check this by running HandBrakeCLI --version in the terminal. If it’s not installed, follow the installation instructions on HandBrake’s official website.
	3.	Run the script:
	•	In your terminal, navigate to the directory where the script is located and execute:

python convert_videos.py


	4.	Enter the path to the folder containing the videos you want to convert when prompted.
	•	For example: /path/to/your/video/folder
	5.	The script will:
	•	Process all videos in the specified folder and its subfolders.
	•	Convert each video to MP4 using the Apple VideoToolbox H.265 4K preset.
	•	Replace the original video file with the converted one while retaining timestamps.
	6.	Check the conversion log:
	•	After the script completes, it will generate a conversion_log.csv file in the same directory where the script is located.
	•	The log file will contain the following columns:
	•	Timestamp: Date and time of conversion.
	•	File Location: Path of the original video.
	•	Original Size (MB): Size of the original video in MB.
	•	Converted Size (MB): Size of the converted MP4 file in MB.
	•	Saved Size (MB): Difference in size between the original and converted file (how much space was saved).
Example CSV log:

Timestamp,File Location,Original Size (MB),Converted Size (MB),Saved Size (MB)
2025-01-01 12:34:56,/path/to/video/file.mov,500.00,250.00,250.00



Notes
	•	Ensure that HandBrakeCLI is installed and properly configured on your system.
	•	The script will delete the original video file after successful conversion and replacement by the new MP4 file.
	•	The script uses multithreading (via ThreadPoolExecutor) to process multiple videos concurrently, speeding up the conversion process.

License

This project is licensed under the MIT License. See the LICENSE file for more details.

MIT License Summary

The MIT License allows users to freely use, modify, and distribute the software, with the condition that the original license and copyright notice must be included. The software is provided “as-is” without warranties of any kind.

Acknowledgements
	•	This script utilizes HandBrakeCLI for video encoding.
	•	The ThreadPoolExecutor from Python’s standard library is used to process videos concurrently.

