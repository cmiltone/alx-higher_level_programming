#!/usr/bin/python3
"""
module for base class
"""
import json
from io import StringIO
import csv
import turtle


class Base:
    """sbase class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """set the id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns json representation of the class"""
        if list_dictionaries is None or len(list_dictionaries) <= 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        rects = []
        sqrs = []
        for item in list_objs:
            filename = item.__class__.__name__ + ".json"
            if item.__class__.__name__ == "Rectangle":
                rects.append(item.to_dictionary())
            if item.__class__.__name__ == "Square":
                sqrs.append(item.to_dictionary())
        if len(rects) > 0:
            with open("Rectangle.json", "w+") as f:
                f.write(cls.to_json_string(rects))
        if len(sqrs) > 0:
            with open("Square.json", "w+") as f:
                f.write(cls.to_json_string(sqrs))

    @staticmethod
    def from_json_string(json_string):
        """returns an object represented by a JSON string"""
        io = StringIO(json_string)
        return json.load(io)

    @classmethod
    def create(cls, **dictionary):
        """eturns an instance with all attributes already set"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                _class = cls(1, 1)
            else:
                _class = cls(1)
            _class.update(**dictionary)
            return _class

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        _list = []
        filename = cls.__name__ + ".json"
        try:
            with open(filename, encoding="utf-8") as f:
                string = f.read()
                for obj in cls.from_json_string(string):
                    _list.append(cls.create(**obj))
            return _list
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """saves to csv"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w") as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
                return
            fields = []
            if cls.__name__ == "Square":
                fields = ["id", "size", "x", "y"]
            elif cls.__name__ == "Rectangle":
                fields = ["id", "width", "height", "x", "y"]
            w = csv.DictWriter(f, fieldnames=fields)
            for obj in list_objs:
                w.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """loads from csv file"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as f:
                if cls.__name__ == "Square":
                    fields = ["id", "size", "x", "y"]
                else:
                    fields = ["id", "width", "height", "x", "y"]
                items = csv.DictReader(f, fieldnames=fields)
                items = [dict([i, int(j)] for i, j in item.items())
                         for item in items]
                _list = []
                for d in items:
                    _list.append(cls.create(**d))
                return _list
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ draws the shapes"""
        t = turtle.Turtle()
        t.screen.bgcolor("#02bbee")
        t.pensize(3)
        t.shape("turtle")

        t.color("#ffffff")
        for rect in list_rectangles:
            t.showturtle()
            t.up()
            t.goto(rect.x, rect.y)
            t.down()
            for i in range(2):
                t.forward(rect.width)
                t.left(90)
                t.forward(rect.height)
                t.left(90)
            t.hideturtle()

        t.color("#0224ee")
        for sq in list_squares:
            t.showturtle()
            t.up()
            t.goto(sq.x, sq.y)
            t.down()
            for i in range(2):
                t.forward(sq.width)
                t.left(90)
                t.forward(sq.height)
                t.left(90)
            t.hideturtle()

        turtle.exitonclick()
