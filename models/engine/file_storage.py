#!/usr/bin/python3
'''serializes instances to a JSON file and deserializes JSON file to instances
'''
import json


class FileStorage():
    '''
Private class attributes:
    __file_path: string - path to the JSON file (ex: file.json)
    __objects: dictionary - empty but will store all objects by <class name>.id
Public instance methods:
    all(self): returns the dictionary __objects
    new(self, obj): sets in __objects the obj with key <obj class name>.id
    save(self): serializes __objects to the JSON file (path: __file_path)
    reload(self): deserializes the JSON file to __objects
'''
    __file_path = 'file.json'
    __objects = {}
    def __init__(self, __file_path=None):
        '''Initializes file path and objects provate attribute'''
        if __file_path is not None:
            self.__file_path = __file_path

    def all(self):
        '''Returns a dictionary of all objects'''
        return self.__objects

    def new(self, obj):
        '''sets in __objects the obj with key <obj class name>.id'''
        dicti = obj.to_dict()
        print(dicti)
        print(obj.__class__.__name__)
        self.__objects.update({"[{}] ({})".format(obj.__class__.__name__,
                                                obj.id): dicti})
    def save(self):
        '''serializes __objects to the JSON file (path: __file_path)'''
        try:
            with open(self.__file_path, "a") as f:
                f.write(json.dumps(self.__objects))
                f.close()
        except FileNotFoundError:
            with open(self.__file_path, "w") as f:
                f.write(json.dumps(self.__objects))
                f.close()

    def reload(self):
        '''deserializes the JSON file to __objects'''
        try:
            with open(self.__file_path, "r") as f:
                stuff = f.read()
                print("Stuff and things" + stuff)
                print(type(stuff))
                js = json.loads(stuff)
                print(js)
                print(type(js))
                f.close()
        except FileNotFoundError:
            pass
