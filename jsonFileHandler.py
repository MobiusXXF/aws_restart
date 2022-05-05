import json

# open returns a file handler to the files/insulin.json file
# json.load reads the JSON file and returns the content as a python dictionary
# adding a try/except block makes the function more reliable
def readJsonFile(fileName):
    data=""
    try:
        with open('files/insulin.json') as json_file:
            data = json.load(json_file)
    except IOError:
        print("Could not read file")
    return data

# jsonFileHandle module created that can be imported in other Python files to access the--
#  --readJsonFile function.
