import time, os, json
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from octcsvreader import OctCsvReader
from mqtt import Mqtt

def readAndConvertData(filePath):
    reader = OctCsvReader()
    print(filePath)
    fileDetail = reader.getCSVNameDetailFromFile(os.path.basename(filePath))
    data = reader.readCSVTables(filePath, fileDetail)
    for key in data.keys():
        with open(f'{fileDetail["seamid"]}__{key}.json', 'w', encoding='utf-8') as f:
            json.dump(data[key], f, ensure_ascii=False, indent=4)



class EventHandler(FileSystemEventHandler):
    def on_created(self, event): # when file is created
        historicalSize = -1
        while (historicalSize != os.path.getsize(event.src_path)):
            historicalSize = os.path.getsize(event.src_path)
            time.sleep(1)
        readAndConvertData(event.src_path)

if __name__ == "__main__":
    observer = Observer()
    event_handler = EventHandler()
    # set observer to use created handler in directory
    observer.schedule(event_handler, path='.\data')
    observer.start()

    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()