import time

class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self)
        self.tracker = ALProxy( "ALTracker" )
        self.memory = ALProxy("ALMemory")
        self.targetName = "Face"
        self.distanceX = 0.0
        self.distanceY = 0.0
        self.angleWz = 0.0
        self.thresholdX = 0.0
        self.thresholdY = 0.0
        self.thresholdWz = 0.0
        self.subscribeDone = False
        self.effector = "None"
        self.isRunning = False

    def onLoad(self):
        self.BIND_PYTHON(self.getName(), "setParameter")
        self.BIND_PYTHON(self.getName(), "onTargetLost")
        self.BIND_PYTHON(self.getName(), "onTargetReached")
        self.BIND_PYTHON(self.getName(), "onTargetChanged")
        self.memory.subscribeToEvent("ALTracker/ActiveTargetChanged", self.getName(), "onTargetChanged")

    def onUnload(self):
        if self.subscribeDone:
            self.memory.unsubscribeToEvent("ALTracker/TargetLost", self.getName())
            self.memory.unsubscribeToEvent("ALTracker/TargetReached", self.getName())
            self.subscribeDone = False

        if self.isRunning:
            self.tracker.setEffector("None")
            self.tracker.stopTracker()
            self.tracker.unregisterTarget(self.targetName)
            self.isRunning = False

    def onInput_onStart(self):
        self.memory.subscribeToEvent("ALTracker/TargetLost", self.getName(), "onTargetLost")
        self.memory.subscribeToEvent("ALTracker/TargetReached", self.getName(), "onTargetReached")
        self.subscribeDone = True

        mode = self.getParameter("Mode")
        width = self.getParameter("Width (m)")
        self.distanceX = self.getParameter("Distance X (m)")
        self.thresholdX = self.getParameter("Threshold X (m)")
        self.distanceY = self.getParameter("Distance Y (m)")
        self.thresholdY = self.getParameter("Threshold Y (m)")
        self.angleWz = self.getParameter("Theta (rad)")
        self.thresholdWz = self.getParameter("Threshold Theta (rad)")
        self.effector = self.getParameter("Effector")

        self.tracker.setEffector(self.effector)

        self.tracker.registerTarget(self.targetName, width)
        self.tracker.setRelativePosition([-self.distanceX, self.distanceY, self.angleWz,
                                           self.thresholdX, self.thresholdY, self.thresholdWz])
        self.tracker.setMode(mode)

        self.tracker.track(self.targetName) #Start tracker
        self.isRunning = True

    def onInput_onStop(self):
        self.onStopped()
        self.onUnload()

    def setParameter(self, parameterName, newValue):
        GeneratedClass.setParameter(self, parameterName, newValue)
        if (parameterName == "Mode"):
            self.tracker.setMode(newValue)
            return

        if (parameterName == "Width (m)"):
            self.tracker.registerTarget(self.targetName, newValue)
            return

        if (parameterName == "Distance X (m)"):
            self.distanceX = newValue
            self.tracker.setRelativePosition([-self.distanceX, self.distanceY, self.angleWz,
                                               self.thresholdX, self.thresholdY, self.thresholdWz])
            return

        if (parameterName == "Distance Y (m)"):
            self.distanceY = newValue
            self.tracker.setRelativePosition([-self.distanceX, self.distanceY, self.angleWz,
                                               self.thresholdX, self.thresholdY, self.thresholdWz])
            return

        if (parameterName == "Theta (rad)"):
            self.angleWz = newValue
            self.tracker.setRelativePosition([-self.distanceX, self.distanceY, self.angleWz,
                                               self.thresholdX, self.thresholdY, self.thresholdWz])
            return

        if (parameterName == "Threshold X (m)"):
            self.thresholdX = newValue
            self.tracker.setRelativePosition([-self.distanceX, self.distanceY, self.angleWz,
                                               self.thresholdX, self.thresholdY, self.thresholdWz])
            return

        if (parameterName == "Threshold Y (m)"):
            self.thresholdY = newValue
            self.tracker.setRelativePosition([-self.distanceX, self.distanceY, self.angleWz,
                                               self.thresholdX, self.thresholdY, self.thresholdWz])
            return

        if (parameterName == "Threshold Theta (rad)"):
            self.thresholdWz = newValue
            self.tracker.setRelativePosition([-self.distanceX, self.distanceY, self.angleWz,
                                               self.thresholdX, self.thresholdY, self.thresholdWz])
            return

        if(parameterName == "Effector"):
            self.tracker.setEffector(newValue)
            self.effector = newValue
            return

    def onTargetLost(self, key, value, message):
        self.targetLost()

    def onTargetReached(self, key, value, message):
        self.targetReached()

    def onTargetChanged(self, key, value, message):
        if value == self.targetName and not self.subscribeDone:
            self.memory.subscribeToEvent("ALTracker/TargetLost", self.getName(), "onTargetLost")
            self.memory.subscribeToEvent("ALTracker/TargetReached", self.getName(), "onTargetReached")
            self.subscribeDone = True
        elif value != self.targetName and self.subscribeDone:
            self.memory.unsubscribeToEvent("ALTracker/TargetLost", self.getName())
            self.memory.unsubscribeToEvent("ALTracker/TargetReached", self.getName())
            self.subscribeDone = False