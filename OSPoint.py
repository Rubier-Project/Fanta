import os
from FantaConverter import Convertify

class StringType(Convertify.String):
    ...

class Executer(object):
    def pathWorker():
        return os.getcwd()
    
    def pathNull():
        return os.devnull
    
    def deviceEncoding(fd: int):
        return os.device_encoding(fd=fd)
    
    def command(Command: str | StringType = None):
        os.system(Command)

    def listPath(pathWorking: str | StringType = None):
        return os.listdir(pathWorking)
    
    class IS(object):
        def exists(path: str | StringType):
            return os.path.exists(path)
        
        def file(path: str | StringType):
            return os.path.isfile(path)
        
        def dir(path: str | StringType):
            return os.path.isdir(path)
        
        def abs(path: str | StringType):
            return os.path.isabs(path)
        
        def link(path: str | StringType):
            return os.path.islink(path)
        
        def mount(path: str | StringType):
            return os.path.ismount(path)
        
