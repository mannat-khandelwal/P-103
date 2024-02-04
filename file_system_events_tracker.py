import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/Kalyan/Downloads"

class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print("Hey, {event.from_dir} has been created")
        
    def on_deleted(self, event):
        print("{event.from_dir} has been deleted")

    def on_modified(self, event):
        print("{event.from_dir} has been modified")
        
    def on_moved(self, event):
        print("{event.from_dir} has been moved")

# Initialize Event Handler Class
event_handler = FileEventHandler()


# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)

# Start the Observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stop")
    observer.stop()
