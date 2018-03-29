from json import dumps, loads, JSONEncoder, JSONDecoder
import pickle
from decimal import *


# Modified version
class PythonObjectEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (list, dict, str, unicode, int, float, bool, type(None))):
            return JSONEncoder.default(self, obj)
        return {'_python_object': pickle.dumps(obj)}

def as_python_object(dct):
    if '_python_object' in dct:
        return pickle.loads(str(dct['_python_object']))
    return dct


def write_answers(answers_out, path_file):
    # Write answers to a file
    answers_dumps = dumps(answers_out, cls=PythonObjectEncoder)
    with open(path_file, 'w') as file:
        file.write(answers_dumps)
        file.close()
        

def reload_answers(path_file):
    with open(path_file, "r") as reader:
        answer_contents = reader.read()
    return loads(answer_contents, object_hook=as_python_object)