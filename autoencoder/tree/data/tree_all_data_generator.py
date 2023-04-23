import json
import os
from tqdm import tqdm

data_path = "../../../data_processing/semantic_annotations/json/all/"

dataset = open("all_data.txt", 'w')

def isComponentLabel(data):
    result = ""
    if data.get("componentLabel"):
        result = result + " " + data["componentLabel"].replace(" ","")
    if data.get("children"):
        for i in data["children"]:
            result = result + isComponentLabel(i)
    return result

def isComponentLabelforNode(data, node_num):
    result = ""
    if data.get("componentLabel"):
        result = result + " " + str(node_num)
    if data.get("children"):
        for i in data["children"]:
            result = result + isComponentLabelforNode(i, node_num+1)
    return result

for i in tqdm(range(0,80000)):
    json_data_path = data_path + str(i) + ".json"
    if os.path.isfile(json_data_path):
        json_data = open(json_data_path).read()
        data = json.loads(json_data)
        result = isComponentLabel(data)
        node = isComponentLabelforNode(data, -1)
        if result:
            dataset.write("%s\t%s\t%s\n" % (str(i), result[1:], node))
    else:
        continue
