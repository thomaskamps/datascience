import json
def json_round_trip(structure):
    return json.loads(json.dumps(structure))
struc1 = [
 1,
 "string",
 ["l", "i", "s", "t"],
 {
  "dict": "with",
  "various": "string keys"
 }
]

json_string = json.dumps(struc1)
print(json_string)
print(eval(json_string))
if struc1 == json_round_trip(struc1):
    print("Round trip succeeded")# See https://docs.python.org/2/howto/urllib2.html
import urllib2
url = "https://raw.githubusercontent.com/DevTeam-TheOpenBastion/int-py-notes/master/nbsource/list-dict-and-set-comprehensions.ipynb"
jsonfile= urllib2.urlopen(url)
jsonfile = jsonfile.read()  # The jsonfile as a Python string
json_as_python_object = json.loads(jsonfile) # The josnfile transformed into a Python dict

# test 
jsonfile[:40],json_as_python_object.keys(),len(json_as_python_object), len(jsonfile) 
# show the keys
#json_as_python_object.keys()
struc2 = float("NaN")
print("Python:", str(struc2))std_encoder = json.JSONEncoder()
print("JSON:", std_encoder.encode(struc2))strict_encoder = json.JSONEncoder(allow_nan=False)
strict_encoder.encode(struc2)class nonJson:
    """Demonstrates how an object that cannot be represented."""
    def __init__(self, one, two):
        self.one = one
        self.two = two
    @classmethod
    def decode(cls, json_string):
        strict_decoder