

class ResponseStatusCollection():

    def __init__(self):
        self.statusArray = []

    def addImportStatus(self,importStatus):
        self.statusArray.append(importStatus.copy())

    def getImportStatus(self):
        return self.statusArray

class ResponseStatus():
    status = {}

    def setAction(self,action):
        self.status['action'] = action

    def setResult(self,result):
        self.status['result'] = result

    def getAction(self):
        return self.status['action']

    def getResult(self):
        return self.status['result']

    def getStatus(self):
        return self.status


