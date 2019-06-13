#!/usr/bin/env python
# -*- coding:utf-8 -*-

# _author:"xiaolin"
# date:2018/8/7
from connect_pepper import Open_pepper

import time

class Func:
    # pepper平板显示页面
    def webview(self, session, web_ip):
        try:
            tabletService = session.service("ALTabletService")
            tabletService.enableWifi()
            tabletService.showWebview(web_ip)
        except Exception, e:
            print "Error was: ", e

    # 开启pepper的某个behavior，behavior_name是行为的名字
    def start_behavior(self, session, behavior_name):
        behavior_mng_service = session.service("ALBehaviorManager")
        if (behavior_mng_service.isBehaviorInstalled(behavior_name)):
            # Check that it is not already running.
            if (not behavior_mng_service.isBehaviorRunning(behavior_name)):
                # Launch behavior. This is a blocking call, use _async=True if you do not
                # want to wait for the behavior to finish.
                behavior_mng_service.runBehavior(behavior_name, _async=True)
                time.sleep(0.5)
            else:
                print "Behavior is already running."

        else:
            print "Behavior not found."
        return

        names = behavior_mng_service.getRunningBehaviors()
        print "Running behaviors:"
        print names

        # Stop the behavior.
        if (behavior_mng_service.isBehaviorRunning(behavior_name)):
            behavior_mng_service.stopBehavior(behavior_name)
            time.sleep(1.0)
        else:
            print "Behavior is already stopped."

        names = behavior_mng_service.getRunningBehaviors()
        print "Running behaviors:"
        print names

    def stop_behavior(self,session, behavior_name):
        behavior_mng_service = session.service("ALBehaviorManager")
        if (behavior_mng_service.isBehaviorRunning(behavior_name)):
            behavior_mng_service.stopBehavior(behavior_name)
            # print("Behavior is stop")
        else:
            pass
            # print "Behavior is already stopped."


    def speech(self, session, text):
        asr_service = session.service("ALAnimatedSpeech")
        # set the local configuration
        configuration = {"speakingMovementMode": 'random'}
        # say the text with the local configuration
        asr_service.say(text, configuration)

    def stopSpeak(self,session):
        tts = session.service("ALTextToSpeech")
        tts.stopAll()


if __name__ == '__main__':
    open_pepper = Open_pepper()
    open_pepper.star_pepper('192.168.8.110')
    session = open_pepper.get_session()
    func = Func()
    # func.webview(gl.get_value('session'), 'https://www.baidu.com/')
    # func.start_behavior(session, 'suangua-8a719a/behavior_1')
    # func.start_behavior(session, 'npfuns-9ebf58/TakePicture')
    func.stop_behavior(session,'walking-148f83/behavior_1')
