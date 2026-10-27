import socket
import nicegui

host = ""
port = 3333


def help():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, port))

    nicegui.ui.label('Testing')

nicegui.app.on_startup(help)

nicegui.ui.run(native=True, port=8005, reload=False)
