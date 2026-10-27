import sys
import PySide6
import socket
import nicegui

host = ""
port = 3333

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((host, port))

class main(PySide6.QtWidgets.qWidget):
    def __init__(self):
        super().__init__()

        self.hello = "hello"
        self.button = PySide6.QtWidgets.QPushButton("Click me")
