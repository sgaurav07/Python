import json
with open('test.json', 'r') as files:
    data = json.load(files)
def val():
    for p in data['people']:
        print("Name: " + p['name'])
        print("Website: " + p['website'])
        print("from: " + p['from'])
        print("")
if __name__ == '__main__':
    val()