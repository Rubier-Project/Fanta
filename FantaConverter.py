class Convertify(object):

    def CurrentType(obj: object):
        return type(obj)

    class String(object):
        def __init__(self) -> None:
            pass

        def toString(self, obj: object):
            return str(obj)
        
        def toStringEncoding(self, obj: object, encoding: str = "utf-8"):
            return str(obj).encode(encoding=encoding)
        
        def toUpperCase(self, obj: str):
            return self.toString(obj).upper()
        
        def toLowerCase(self, obj: str):
            return self.toString(obj).lower()
        
        def rePlace(self, obj: str, fromObj: str, toObj: str):
            return self.toString(obj).replace(fromObj, toObj)
        
        def makeStrip(self, obj: str, readableObj: bytes = None):
            return self.toString(obj).strip(readableObj)
        
        def makeSplit(self, obj: str, splitterObj: str = None):
            return self.toString(obj).split(splitterObj)
        
        def createNew(self):
            return ""
        
        def isStartsWith(self, obj: str, starterObj):
            data = self.toString(obj)

            if data.startswith(starterObj):return True
            else:return False

        def isEndsWith(self, obj: str, enderObj):
            data = self.toString(obj)

            if data.endswith(enderObj):return True
            else:return False

        def isDigit(self, obj: str):
            return obj.isdigit()

    class List(object):
        def __init__(self) -> None:
            pass

        def toList(self, obj: object):
            return list(obj)

        def getIndex(self, obj: list, index: int = None):
            return obj if index == None or index > len(obj) or index < 0 else obj.index(index)
        
        def get(self, obj: list, index: int = None):
            return obj if index == None or index > len(obj) or index < 0 else obj[index]
        
        def makeSort(self, obj: list, isReverse: bool = False):
            return obj.sort() if isReverse == False else obj.sort(reverse=True)
        
        def makeClear(self, obj: list):
            obj.clear()

        def makeReverse(self, obj: list):
            return obj.reverse()

        def createNew(self):
            return []
        
        def push(self, obj: list, item: object):
            obj.append(item)
            return obj
        
        def pushIndex(self, obj: list, item: object, indexes: int):
            return obj.insert(indexes, item)
        
        def removeItem(self, obj: list, itemIndexOrObj: object):
            return obj.remove(itemIndexOrObj)
        
    class Dictionary(object):
        def __init__(self) -> None:
            pass

        def toDict(self, obj: object):
            return dict(obj)
        
        def get(self, obj: dict, key: object):
            return obj if not key in obj.keys() else obj.get(key)
        
        def getKeys(self, obj: dict):
            return Convertify.List().toList(obj=obj.keys())
        
        def getValues(self, obj: dict):
            return Convertify.List().toList(obj=obj.values())
        
        def createNew(self):
            return {}
        
        def add(self, obj: dict, key: object, value: object):
            obj[key] = value
            return obj
        
        def updateStream(self, obj: dict, updatedItem: object):
            obj.update(updatedItem)
            return obj
        
        def sortKeysByNumber(self, obj: dict):
            num = 0
            dbs = self.createNew()

            for k, v in obj.items():
                num += 1
                self.add(dbs, num, k)

            return dbs
        
        def sortValsByNumber(self, obj: dict):
            num = 0
            dbs = self.createNew()

            for k, v in obj.items():
                num += 1
                self.add(dbs, num, v)

            return dbs