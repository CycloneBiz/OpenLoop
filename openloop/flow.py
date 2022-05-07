from types import BuiltinFunctionType, FunctionType, MethodType
from flask import Blueprint, jsonify, escape
from openloop.defaults import package

class Flow(dict):
    def __init__(self):
        super().__init__()
        self["defaults"] = package
        self["pages"] = {
            "builtin": {},
            "plugins": {} # This wont be used for a while
        }

class Flow_Serve:
    def __init__(self, reflow : dict) -> None:
        api = Blueprint("flow", __name__)
        self.web = api

        @api.route("/")
        def information():
            return {
                "version": "ReFlow Protocol Version 1.0"
            }

        @api.route("/refresh/<element>")
        def update_item(element : str):
            path = element.split(".")

            current = reflow
            for i in path:
                if i in current:
                    current = current[i]
                else:
                    current = {}

            if current == {}:
                current = None
            elif type(current) == BuiltinFunctionType:
                current = str(current())
            elif type(current) == MethodType:
                current = str(current())
            elif type(current) == FunctionType:
                current = current()

            if current == None:
                current = "null"

            return {
                "item": escape(element),
                "value": current
            }