#!/usr/bin/python3
"""The Base model class"""


import json
import os
import csv
import turtle


class Base:
    """class base rep"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initializing base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return JSON representation"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if (type(list_dictionaries) != list or not
                all(type(i) == dict for i in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """JSON serialization of a list of objects"""
        my_file = cls.__name__ + ".json"
        with open(my_file, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dict = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """list of JSON string representation"""
        json_string_list = []

        if json_string is not None and json_string != '':
            if type(json_string) != str:
                raise TypeError("json_string must be a string")
            json_string_list = json.loads(json_string)

        return json_string_list

    @classmethod
    def create(cls, **dictionary):
        """return class instance from a dictionary"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                pha = cls(1, 1)
            else:
                pha = cls(1)
            pha.update(**dictionary)
            return pha

    @classmethod
    def load_from_file(cls):
        """list of instances that is returned"""
        my_file = cls.__name__ + ".json"
        list_of_instances = []
        list_dictionaries = []

        if os.path.exists(my_file):
            with open(my_file, 'r') as the_file:
                c_string = the_file.read()
                list_dictionaries = cls.from_json_string(c_string)
                for dictionary in list_dictionaries:
                    list_of_instances.append(cls.create(**dictionary))
        return list_of_instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """CSV serialization of a list of obj"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """list of class instances from a CSV file returned"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
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
        """Rectangles and Squares using the turtle module"""
        anim = turtle.Turtle()
        anim.screen.bgcolor("#b7312c")
        anim.pensize(3)
        anim.shape("turtle")

        anim.color("#ffffff")
        for rec in list_rectangles:
            anim.showturtle()
            anim.up()
            anim.goto(rec.x, rec.y)
            anim.down()
            for i in range(2):
                anim.forward(rec.width)
                anim.left(90)
                anim.forward(rec.height)
                anim.left(90)
            anim.hideturtle()

        anim.color("#b5e3d8")
        for sq in list_squares:
            anim.showturtle()
            anim.up()
            anim.goto(sq.x, sq.y)
            anim.down()
            for i in range(2):
                anim.forward(sq.width)
                anim.left(90)
                anim.forward(sq.height)
                anim.left(90)
            anim.hideturtle()

        turtle.exitonclick()
