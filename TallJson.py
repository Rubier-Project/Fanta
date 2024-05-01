import json

class JsonLoop(object):
    def toString(obj: dict, flex: int = None):
        return json.dumps(obj, indent=flex)
    
    def toStringFromFile(fp: str, flex: int = None):
        return json.dump(fp=fp, indent=flex)
    
    def fromString(obj: str):
        return json.loads(obj)
    
    def fromStringFromFile(fp: str):
        return json.load(fp=fp)
    
