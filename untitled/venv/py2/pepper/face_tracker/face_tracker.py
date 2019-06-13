#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Example: Use Tracking Module to Track a Face"""

import qi
import argparse
import sys
import time

ip = "192.168.3.71"

def main(session, faceSize):
    """
    This example shows how to use ALTracker with face.
    """
    # Get the services ALTracker and ALMotion.

    motion_service = session.service("ALMotion")
    tracker_service = session.service("ALTracker")

    # First, wake up.
    motion_service.wakeUp()

    # Add target to track.
    targetName = "Face"
    faceWidth = faceSize
    tracker_service.registerTarget(targetName, faceWidth)

    # Then, start tracker.
    tracker_service.track(targetName)

    print "ALTracker 成功启动，现在向机器人展示你的脸!"
    print "使用ctrl+c停止此脚本."

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print
        print "被用户中断"
        print "中止..."

    # Stop tracker.
    tracker_service.stopTracker()
    tracker_service.unregisterAllTargets()
    motion_service.rest()

    print "ALTracker stopped."


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default=ip,
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")
    parser.add_argument("--facesize", type=float, default=0.1,
                        help="Face width.")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print ("无法在IP上连接到naoqi \"" + args.ip + "\" 端口上 " + str(args.port) +".\n"
               "请检查脚本参数。使用-h选项运行以获取帮助。")
        sys.exit(1)
    main(session, args.facesize)