#!/usr/bin/python3

class Base:
    """Class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initialize base"""
        
        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """json serialization"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON serialization"""
        fil = cls.__name__ + ".json"
        with open(fil, "w") as jfile:
            if (list_objs is None):
                j.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return deserialized JSON STRING"""
        if (json_string is None or json_string == "[]"):
            return []
        return json.loads(json_string)

        @classmethod
    def create(cls, **dictionary):
        """Return a class instant"""
        if (dictionary and dictionary != {}):
            if cls.__name__ == "Rectangle":
                n = cls(1, 1)
            else:
                n = cls(1)
            n.update(**dictionary)
            return n
