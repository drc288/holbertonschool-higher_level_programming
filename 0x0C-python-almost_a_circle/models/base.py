#!/usr/bin/python3
import json
"""
Class Base - init the proces id
"""


class Base:
    """ private class attribute """
    __nb_objects = 0
    def __init__(self, id=None):
        """
        init - init the constructor
        """
        if id is not None:
            self.id = id
        else:
            # Accessing the private attribute and assigning it a new value
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        to_json_string - return the str of dictionary
        """
        if list_dictionaries is None:
            return []
        return json.dumps(list_dictionaries)
    
    @classmethod
    def save_to_file(cls, list_objs):
        """
        save_to_file - save the file
        """
        file_name = str(cls.__name__) + ".json"
        with open(file_name, mode="w+", encoding="utf-8") as f:
            n_list = []
            if list_objs == None:
                f.write(str(n_list))
            else:
                for obj in list_objs:
                    data_json = obj.to_dictionary()
                    n_list.append(data_json)
                f.write(cls.to_json_string(n_list))
                