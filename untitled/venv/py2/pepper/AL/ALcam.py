# #! /usr/bin/env python
# # -*- encoding: UTF-8 -*-
#
# # This test demonstrates how to use the ALPhotoCapture module.
# # Note that you might not have this module depending on your distribution
# import os
# import sys
# import time
# from naoqi import ALProxy
#
# # Replace this with your robot's IP address
# IP = "192.168.3.18"
# PORT = 9559
#
# # Create a proxy to ALPhotoCapture
#
# al = ALProxy("kTopCamera", IP, PORT)
#
#
#
# print "a"

#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Example: Use setParameter Method"""

import qi
import argparse
import sys


def main(session):

    sound_detect_service = session.service("ALSoundDetection")

    sound_detect_service.setParameter("Sensitivity", 0.3)
    print "Sensitivity set to 0.3"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="192.168.3.18",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    main(session)