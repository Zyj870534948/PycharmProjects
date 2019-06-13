#!/usr/bin/env python
# -*- coding:utf-8 -*-

# _author:"sidalin"
import requests
import qi
import functools,sys
import config.globalvar as gl
import config.global_variables

class ReactToTouch(object):
    """ A simple module able to react
        to touch events.
    """

    def __init__(self, app):
        super(ReactToTouch, self).__init__()
        # Get the services ALMemory, ALTextToSpeech.
        app.start()
        session = app.session
        self.memory_service = session.service("ALMemory")
        # Connect to an Naoqi1 Event.
        self.touch = self.memory_service.subscriber("MiddleTactilTouched")
        self.id = self.touch.signal.connect(functools.partial(self.onTouched, "MiddleTactilTouched"))

    def onTouched(self, strVarName, value):
        """ This will be called each time a touch
        is detected.

        """
        # Disconnect to the event when talking,
        # to avoid repetitions
        self.touch.signal.disconnect(self.id)
        print(value)
        url = "http://"+gl.get_value("robot_ip")+":8888/openwebview?name=standby"
        if value == 1:
            requests.get(url=url)
        # Reconnect again to the event
        self.id = self.touch.signal.connect(functools.partial(self.onTouched, "MiddleTactilTouched"))


if __name__ == "__main__":
    app = qi.Application(["ReactToTouch", "--qi-url=" + str(gl.get_value('connection_url'))])
    # app = qi.Application(["ReactToTouch", "--qi-url=tcp://192.168.8.115:9559"])
    react_to_touch = ReactToTouch(app)
    app.run()
