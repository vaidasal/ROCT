import time, os, json
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from octcsvreader import OctCsvReader
from mqtt import Mqtt

def readAndSendData(filePath):
    reader = OctCsvReader()
    fileDetail = reader.getCSVNameDetailFromFile(os.path.basename(filePath))
    data = reader.readCSVTables(filePath, fileDetail)
    mqtt = Mqtt()
    for key in data.keys():
        mqtt.sendMessage(json.dumps(data[key]))


class EventHandler(FileSystemEventHandler):
    def on_created(self, event): # when file is created
        readAndSendData(event.src_path)

if __name__ == "__main__":
    observer = Observer()
    event_handler = EventHandler()
    # set observer to use created handler in directory
    observer.schedule(event_handler, path='.\data')
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

