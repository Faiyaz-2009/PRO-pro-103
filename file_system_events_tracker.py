import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/faiya/Downloads"
to_dir = "C:/Users/faiya/OneDrive/Desktop/images"


class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(event)
        print(f"Hey, {event.src_path} has been created.")

    def on_modified(self, event):
        print(event)
        print(f"Hey, {event.src_path} has been modified.")
    def on_moved(self, event):
        print(event)
        print(f"Hey, {event.src_path} has been moved.")

    def on_deleted(self, event):
        print(event)
        print(f"Hey, {event.src_path} has been deleted.")


event_handler = FileMovementHandler()

observer = Observer()
observer.schedule(event_handler, from_dir, recursive=True)
observer.start()
try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("Programm has stopped")
    observer.stop()