import json
import os
from tqdm import tqdm
import glob

train_data = open("train_data.txt", 'w')
val_data = open("val_data.txt", 'w')

train_data_path = []
val_data_path = []

for dir in tqdm(glob.glob("../../../data_processing/semantic_annotations/json/train/*")):
    train_data_path.append(dir)

for dir in tqdm(glob.glob("../../../data_processing/semantic_annotations/json/val/*")):
    val_data_path.append(dir)

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

print("train data generate...")
for p in tqdm(train_data_path):
    json_data = open(p).read()
    data = json.loads(json_data)
    result = isComponentLabel(data)
    node = isComponentLabelforNode(data, -1)
    if result:
        train_data.write("%s\t%s\t%s\t%s\n" % (result[1:], node, result[1:], node))

print("val data generate...")
for p in tqdm(val_data_path):
    json_data = open(p).read()
    data = json.loads(json_data)
    result = isComponentLabel(data)
    node = isComponentLabelforNode(data, -1)
    if result:
        val_data.write("%s\t%s\t%s\t%s\n" % (result[1:], node, result[1:], node))

print("done...")
