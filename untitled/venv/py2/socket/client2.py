from tornado.websocket import WebSocketHandler
from tornado.web import asynchronous, Application
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.gen import coroutine, sleep
import socket
while 1:
    ws = create_connection("ws://192.168.3.5:11111/Robotsocket/", timeout=5)
    if ws.connected:
        ws.send('am coming', opcode=websocket.ABNF.OPCODE_TEXT)
        print ws.recv()
    # ws.close()