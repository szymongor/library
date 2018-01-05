

class ResponseStatusCollection():
    statusArray = []

    def addImportStatus(self,importStatus):
        self.statusArray.append(importStatus)

    def getImportStatus(self):
        return self.statusArray

class ResponseStatus():
    status = {}

    def setAction(self,action):
        self.status['action'] = action

    def setResult(self,result):
        self.status['result'] = result

    def getStatus(self):
        return self.status


