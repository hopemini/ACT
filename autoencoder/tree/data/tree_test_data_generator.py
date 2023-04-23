import json
import os
import glob
from tqdm import tqdm

test_23_path = "../../../data_processing/semantic_annotations/json/test_23/"
test_34_path = "../../../data_processing/semantic_annotations/json/test_34/"

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

test_23 = list()
for dir in sorted(glob.glob(test_23_path+"*")):
    test_23.append(dir)

test_34 = list()
for dir in sorted(glob.glob(test_34_path+"*")):
    test_34.append(dir)

with open("test_23_data.txt", 'w') as dataset_23:
    for json_data_path in tqdm(test_23):
        json_data = open(json_data_path).read()
        data = json.loads(json_data)
        result = isComponentLabel(data)
        node = isComponentLabelforNode(data, -1)
        if result:
            dataset_23.write("%s\t%s\t%s\n" % (
                json_data_path.split("/")[-1].split(".")[0], result[1:], node))

with open("test_34_data.txt", 'w') as dataset_34:
    for json_data_path in tqdm(test_34):
        json_data = open(json_data_path).read()
        data = json.loads(json_data)
        result = isComponentLabel(data)
        node = isComponentLabelforNode(data, -1)
        if result:
            dataset_34.write("%s\t%s\t%s\n" % (
                json_data_path.split("/")[-1].split(".")[0], result[1:], node))
