from FantaConverter import Convertify

class ObjectSun(object):
    def getName(obj: object):
        return obj.__name__
    
    def getFuncs(obj: object):
        return Convertify.List().toList(dir(obj))