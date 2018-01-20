

class ResponseStatusCollection():

    def __init__(self):
        self.status_array = []

    def add_import_status(self, import_status):
        self.status_array.append(import_status.copy())

    def get_import_status(self):
        return self.status_array

class ResponseStatus():
    status = {}

    def set_action(self, action):
        self.status['action'] = action

    def set_result(self, result):
        self.status['result'] = result

    def set_message(self, message):
        self.status['message'] = message

    def get_action(self):
        return self.status['action']

    def get_result(self):
        return self.status['result']

    def get_message(self):
        return self.status['message']

    def get_status(self):
        return self.status


