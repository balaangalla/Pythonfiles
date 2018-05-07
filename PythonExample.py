import json
from pprint import pprint

with open('C:\Users\BAngalla\Desktop\AWS-Documentation\SampleFile.json') as data_file:
    data = json.load(data_file)
    pprint(data)
    var = data["color"]
    print(var)
    data["fruit"] = var
    print(data)