#!/usr/bin/env python

import sys
import json

def readJsonFile(filePath):
    fp = open(filePath, 'r')
    json_data = json.load(fp)
    fp.close()
    return json_data["data"]


fileContents = []
commandArgumentsCount = len(sys.argv) - 1
for i in range(commandArgumentsCount):
    filePath = sys.argv[i + 1]
    fileContents = fileContents + readJsonFile(filePath)

dict = {}
dict["data"] = fileContents
fp = open('./merged.json', 'w')
json.dump(dict, fp)
fp.close()