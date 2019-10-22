#!/usr/bin/python3
""" Class Base - init the proces id """
import json


class Base:
    """ Base """
    # Create private attribute
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
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return json.dumps([])

        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        from_json_string - from json to str
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        save_to_file - save the file
        """
        file_name = str(cls.__name__) + ".json"
        with open(file_name, mode="w+", encoding="utf-8") as f:
            n_list = []
            if list_objs is None:
                f.write(str(n_list))
            else:
                for obj in list_objs:
                    data_json = obj.to_dictionary()
                    n_list.append(data_json)
                f.write(cls.to_json_string(n_list))

    @classmethod
    def create(cls, **dictionary):
        """
        create - create a new instance
        """
        # Verify if the cls is Rectangle
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        # Or is Square
        elif cls.__name__ == "Square":
            dummy = cls(1)
        # Update the dummy (Rectangle or Square)
        # and update using the public method update
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        load_from_file - load the file and return a new list to exec
        """
        # Create the namefile
        file_name = str(cls.__name__) + ".json"
        # Try to open the file
        try:
            # Read the file
            with open(file_name, mode="r", encoding="utf-8") as f:
                # Create empty file
                new_list = []
                # Read the file
                read_file = f.read()
                new_file = cls.from_json_string(read_file)
                for dic in new_file:
                    new_inst = cls.create(**dic)
                    new_list.append(new_inst)
                return new_list
        except Exception:
            return []
