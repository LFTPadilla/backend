from json import JSONEncoder
import json

class ServiceObject:

    Success = False
    Message = ''
    SessionToken = ''
    Data = ''
    User = ''
    IpAddress = ''
    ApiKey = ''
    Version = ''

    def __init__(self, Service,Module,Action):
        self.Service = Service;
        self.Module= Module;
        self.Action = Action;

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)
        
# subclass JSONEncoder
class ServiceObjectEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__