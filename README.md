# Deduplicator

This Python script scans a specified directory for duplicate files based on their MD5 hash and provides the option to delete the duplicates.

## Features
- Scans a directory for files and computes their MD5 hashes.
- Identifies duplicate files (those with the same MD5 hash).
- Prompts the user to delete the duplicate files, keeping only one copy.
- Provides feedback if no duplicates are found or if the directory doesn't exist.

## Requirements
- Python 3.x
- No external libraries are required as it uses standard Python libraries (`os`, `sys`, `hashlib`, etc.).

## How to Use

1. **Clone the repository** or download the script file.
2. **Run the script** by passing the directory path you want to scan as a command-line argument:

   ```bash
   python deduplicate.py /path/to/directory
