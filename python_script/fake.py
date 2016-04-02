import json
def ioio():
    with open('../../python_script/output.json') as data_file:    
        data = json.load(data_file)
    print json.dumps(data);    
ioio()