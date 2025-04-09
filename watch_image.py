# watch_image.py
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess

IMAGE_NAME = "your_image.jpg"  # Replace with your actual image file
FOLDER_TO_WATCH = "."          # Current folder

class ImageChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if IMAGE_NAME in event.src_path:
            print(f"{IMAGE_NAME} updated. Running detection...")
            subprocess.run(["python", "main_object_detection.py"])

if __name__ == "__main__":
    event_handler = ImageChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path=FOLDER_TO_WATCH, recursive=False)
    observer.start()
    print(f"Watching for changes to {IMAGE_NAME}...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
