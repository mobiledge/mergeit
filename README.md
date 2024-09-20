# MergeIt!

This Python script merges multiple PDF files in a specified folder into a single PDF file.

## Features

- Merges all PDF files in a given folder
- Sorts files alphabetically before merging
- Creates a single output file named `merged_output.pdf`
- Includes a pre-built executable for easy use

## Project Structure

```
pdf-merger/
│
├── build/
│   └── mergeit/         # Build files for the executable
├── dist/
│   └── mergeit          # Standalone executable
├── env/                 # Virtual environment (not tracked by Git)
├── mergeit.py           # Source Python script
├── mergeit.spec         # PyInstaller specification file
└── README.md            # This file
```

## Requirements

- Python 3.6 or higher (for running the script directly)
- No additional requirements for running the pre-built executable

## Usage

### Using the Pre-built Executable

1. Navigate to the `dist` directory
2. Run the executable from the command line, providing the path to the folder containing your PDF files:
   ```
   ./mergeit /path/to/your/pdf/folder
   ```
   On Windows, you might need to use:
   ```
   mergeit.exe C:\path\to\your\pdf\folder
   ```

### Running the Python Script

If you prefer to run the Python script directly:

1. Create and activate a virtual environment:
   ```
   python -m venv env
   source env/bin/activate  # On Unix or MacOS
   env\Scripts\activate     # On Windows
   ```

2. Install the required packages:
   ```
   pip install PyPDF2
   ```

3. Run the script:
   ```
   python mergeit.py /path/to/your/pdf/folder
   ```

## Building the Executable (Optional)

If you want to rebuild the executable:

1. Ensure you have PyInstaller installed:
   ```
   pip install pyinstaller
   ```

2. Run PyInstaller:
   ```
   pyinstaller mergeit.spec
   ```

3. The new executable will be in the `dist` folder.

## Notes

- The script will only merge files with a `.pdf` extension.
- Files are merged in alphabetical order.
- If no PDF files are found in the specified folder, the script will notify you and exit.
- The `env` directory containing the virtual environment is not included in the repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/yourusername/pdf-merger/issues) if you want to contribute.
