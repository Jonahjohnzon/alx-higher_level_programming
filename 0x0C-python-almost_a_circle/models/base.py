#!/usr/bin/python3

"""base model clas"""
import json
import csv
import turtle


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
                jfile.write("[]")
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

    @classmethod
    def load_from_file(cls):
        """load_from_file"""
        fil = str(cls.__name__) + ".json"
        try:
            with open(fil, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save to file"""
        filen = cls.__name__ + ".csv"
        with open(filen, "w", newline="") as csvfile:
            if (list_objs is None or list_objs == []):
                csvfile.write("[]")
            else:
                if (cls.__name__ == "Rectangle"):
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writ = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writ.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """load from file"""
        filen = cls.__name__ + ".csv"
        try:
            with open(filen, "r", newline="") as csvfile:
                if (cls.__name__ == "Rectangle"):
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Rectangles and Squares
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
