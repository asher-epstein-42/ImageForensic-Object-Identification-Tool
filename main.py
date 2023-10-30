import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from functools import partial
from ultralytics import YOLO
import cv2
import os
import shutil
from consts import NAMES, IMAGE_TYPES


def main(object_to_search, dir_path, show, advanced, copy, output_folder):
    object_image_count = 0
    copied_image = 0

    # Search recursively for files with the specified object in the folder
    for foldername, subfolders, filenames in os.walk(dir_path):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)

            # Check if the file is an image file
            if filename.endswith(IMAGE_TYPES):
                try:
                    # Load the chosen YOLO model
                    if advanced:
                        model_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'yolov8l.pt')
                        model = YOLO(model_path)
                    else:
                        model_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'yolov8n.pt')
                        model = YOLO(model_path)

                    # Perform object detection using YOLO
                    if show:
                        results = model(file_path, show=True)
                    else:
                        results = model(file_path)

                    # Load the input image
                    img = cv2.imread(file_path)

                    # Check if the image was loaded successfully
                    if img is None:
                        print(f"Error: Unable to load the image from {file_path}")
                        continue  # Skip to the next iteration

                    # Create a counter for object screenshots
                    object_counter = 1

                    for r in results:
                        for box in r.boxes:
                            cls = int(box.cls[0])
                            class_name = NAMES[cls]

                            # Check if the detected object is the specified object
                            if class_name == object_to_search:
                                # Extract the coordinates of the bounding box
                                x1, y1, x2, y2 = map(int, box.xyxy[0])

                                # Crop the region of interest (ROI) containing the object
                                object_roi = img[y1:y2, x1:x2]

                                # Define a filename for the screenshot
                                screenshot_filename = f'{object_to_search}_{object_counter}{filename[:-4]}.png'

                                # Define the full path to save the screenshot
                                screenshot_path = os.path.join(output_folder, screenshot_filename)

                                # Save the screenshot or copy the original image based on user choice
                                if copy and not os.path.exists(os.path.join(output_folder, filename)):
                                    shutil.copy(file_path, output_folder)
                                    copied_image += 1
                                else:
                                    cv2.imwrite(screenshot_path, object_roi)

                                # Increment the object and screenshot counter
                                object_counter += 1
                                object_image_count += 1

                except FileNotFoundError as e:
                    print(f"Error: {e}")
                    continue  # Skip to the next iteration

    # Generate result message based on user's choice to copy or save images
    if copy:
        result_message = f"Total {copied_image} images with a {object_to_search} were copied to {output_folder}"
    else:
        result_message = f"Total {object_image_count} screenshots were created in {output_folder}"

    # Show result message in an info box
    messagebox.showinfo("Process Complete", result_message)


def create_folder(item_to_search, output_dir):
    # Create a folder to store object screenshots in the selected output directory
    output_folder = os.path.join(output_dir, f"{item_to_search}_images")
    os.makedirs(output_folder, exist_ok=True)
    return output_folder


def browse_button(entry):
    # Open a folder dialog and insert the selected path into the provided entry widget
    filename = filedialog.askdirectory()
    entry.delete(0, tk.END)
    entry.insert(0, filename)


def start_process(object_entry, dir_entry, show_var, advanced_var, copy_var, output_dir_entry):
    # Extract values from the GUI elements
    object_to_search = object_entry.get()
    dir_path = dir_entry.get()
    show = show_var.get()
    advanced = advanced_var.get()
    copy = copy_var.get()
    output_dir = output_dir_entry.get()

    # Create the output folder for storing screenshots or copied images
    output_folder = create_folder(object_to_search, output_dir)

    # Start the main process
    main(object_to_search, dir_path, show, advanced, copy, output_folder)


def create_gui():
    # Create the main GUI window
    root = tk.Tk()
    root.title("Object Search")

    # Use the 'clam' theme for ttk widgets
    style = ttk.Style()
    style.theme_use('clam')

    # GUI elements
    object_label = tk.Label(root, text="Object to search:")
    object_label.grid(row=0, column=0, padx=10, pady=10)

    selected_object_var = tk.StringVar()

    object_combobox = ttk.Combobox(root, textvariable=selected_object_var, values=list(NAMES.values()))
    object_combobox.grid(row=0, column=1, padx=10, pady=10, sticky='ew')
    object_combobox.set("Select an object")
    object_combobox.configure(state="readonly")

    dir_label = tk.Label(root, text="Directory path:")
    dir_label.grid(row=1, column=0, padx=10, pady=10)

    dir_entry = tk.Entry(root)
    dir_entry.grid(row=1, column=1, padx=10, pady=10)

    browse_button_partial = partial(browse_button, dir_entry)
    browse_btn = tk.Button(root, text="Browse", command=browse_button_partial)
    browse_btn.grid(row=1, column=2, padx=10, pady=10)

    output_dir_label = tk.Label(root, text="Output Directory:")
    output_dir_label.grid(row=2, column=0, padx=10, pady=10)

    output_dir_entry = tk.Entry(root)
    output_dir_entry.grid(row=2, column=1, padx=10, pady=10)

    output_dir_browse_button_partial = partial(browse_button, output_dir_entry)
    output_dir_browse_btn = tk.Button(root, text="Browse", command=output_dir_browse_button_partial)
    output_dir_browse_btn.grid(row=2, column=2, padx=10, pady=10)

    advanced_var = tk.BooleanVar()
    advanced_checkbox = tk.Checkbutton(root, text="Advanced Search", variable=advanced_var)
    advanced_checkbox.grid(row=3, column=0, padx=10, pady=10)

    show_var = tk.BooleanVar()
    show_checkbox = tk.Checkbutton(root, text="Show Images", variable=show_var)
    show_checkbox.grid(row=3, column=1, padx=10, pady=10)

    copy_var = tk.BooleanVar()
    copy_checkbox = tk.Checkbutton(root, text="Copy Original Images", variable=copy_var)
    copy_checkbox.grid(row=3, column=2, padx=10, pady=10)

    start_process_partial = partial(start_process, selected_object_var, dir_entry, show_var, advanced_var, copy_var,
                                    output_dir_entry)
    start_btn = tk.Button(root, text="Start Process", command=start_process_partial)
    start_btn.grid(row=4, column=0, columnspan=3, pady=20)

    exit_btn = tk.Button(root, text="Exit", command=root.destroy)
    exit_btn.grid(row=5, column=0, columnspan=3, pady=10)

    # Run the GUI event loop
    root.mainloop()


if __name__ == '__main__':
    create_gui()
