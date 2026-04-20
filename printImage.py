import os
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import win32print
import win32ui
from PIL import Image, ImageWin


def printer(filename):
    # printer_name是默认打印机的名字
    printer_name = win32print.GetDefaultPrinter()
    # 调用打印机打印两张图片
    hDC = win32ui.CreateDC()
    hDC.CreatePrinterDC(printer_name)

    # 打开图片
    bmp = Image.open(filename)
    bmp.rotate(90)

    scale = 1
    w, h = bmp.size
    hDC.StartDoc(filename)
    hDC.StartPage()

    dib = ImageWin.Dib(bmp)

    # (10,10,1024,768)前面的两个数字是坐标，后面两个数字是打印纸张的大小
    dib.draw(hDC.GetHandleOutput(), (0, 0, 297*23, 210*23))

    hDC.EndPage()
    hDC.EndDoc()
    hDC.DeleteDC()


class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        filename = event.src_path
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            print(f"Detected new image: {filename}")
            print_image(filename)


def print_image(filename):
    # 这里假设你有一个打印图片的命令，比如使用系统的打印命令
    # 你需要根据你的打印机类型和操作系统来更改这个命令
    # 以下命令是Linux下的打印图片命令，具体情况请根据实际情况修改
    print(filename)
    printer(filename)


if __name__ == "__main__":
    folder_to_watch = "F:\\上课作业\\毕设\\定福庄私立体检中心"  # 替换为你要监视的文件夹路径
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, folder_to_watch, recursive=True)
    observer.start()
    try:
        print(f"Watching folder: {folder_to_watch}")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
