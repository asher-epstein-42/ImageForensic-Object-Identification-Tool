# ImageForensic: Object Identification Tool



This is a Python application that allows users to recursively search for a specified object in a directory and its subdirectories of images using YOLO (You Only Look Once) object detection. The application provides a graphical user interface (GUI) for easy interaction.

## Getting Started

### Prerequisites

Make sure you have Python installed on your system. Additionally, the required Python packages can be installed by running the following commands:

```bash
pip install tkinter
pip install ultralytics
pip install opencv-python
```
## Installation
Clone the repository to your local machine:
```bash
git clone https://github.com/asher-epstein-42/ImageForensic-Object-Identification-Tool.git
cd object-search-app
```

## Running the Application

The Object Search Application can be executed using the provided `start.bat` file, which streamlines the setup process. This batch file automatically installs the required Python packages and initiates the application.

1. Use `start.bat` File
Simply click on the `start.bat` file to automatically install the required Python packages and initiate the Object Search Application. This method is convenient for a hassle-free setup,
or execute the following command in the command prompt:

```bash
start.bat
```
2. Run Directly
Alternatively, you can run the application directly by executing the main.py script. Open a terminal or command prompt, navigate to the project directory, and run the following command:
```bash
python main.py
```
## Usage
1.The GUI will prompt you to select the object you want to search for from a dropdown list.

2.Enter the directory path where you want to perform the search.

3.Specify the output directory where the results will be saved.

4.Optionally, choose to enable advanced search, show images during the process, and/or copy the original images.

5.Click the "Start Process" button to initiate the object search.

## Supported File Types
The application supports a variety of image file types commonly encountered in digital forensics:

- bmp
- dng
- jpeg
- jpg
- mpo
- png
- tif
- tiff
- webp
- pfm

## Digital Forensics
In digital forensics, the application becomes a valuable tool for investigators by offering:

- Automated Object Identification: Accelerating the process of identifying specific objects within digital images.
- Advanced Search Options: Providing flexibility with options like enabling advanced search, showing images during the process, and copying original images.
- Supported Image Types: Accommodating various image formats commonly encountered in digital forensics investigations.

## Troubleshooting
If you encounter any issues during installation or execution, please check the following:

- Ensure that Python is installed and added to the system PATH.
- Verify an active internet connection for package installation.
- If problems persist, check the console output for error messages.

## Contributions
Contributions are welcome! Feel free to submit issues or pull requests to improve the functionality or fix any bugs.
