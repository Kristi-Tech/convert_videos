# Video Conversion Script

This Python script is designed to automate the process of converting videos in various formats to MP4 using **HandBrakeCLI** with the **Apple VideoToolbox H.265 4K** preset. The script processes all videos within a given folder (including subfolders), converts them to the MP4 format, and replaces the original files with the converted ones while retaining the original timestamps.

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
