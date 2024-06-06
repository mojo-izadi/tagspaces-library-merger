import json
import os

def writeFinalJson(json):
    with open('my_file.txt', "w", encoding='utf-8') as f:
        f.writelines(str(json).replace('\'', '\"').replace(" True", " true"))
    os.rename("my_file.txt", "merged_library.json")

def getJsons():
    json_files = []
    for f in os.listdir(os.getcwd()):
        if f.endswith('.json'):
            json_files.append(f)

    jsons = []
    for i in range(2):
        with open(json_files[i], encoding="utf-8") as f:
            jsons.append(json.load(f))
    
    return jsons

jsons = getJsons()
tag_arrays = [j["tagGroups"] for j in jsons]

for tag in tag_arrays[0]:
    title = tag["title"]
    child_tags = tag["children"]
    for tag2 in tag_arrays[1]:
        if tag2["title"] == title:
            for child_tag2 in tag2["children"]:
                if child_tag2 not in child_tags:
                    child_tags.append(child_tag2)
            break
        if tag2['title'] not in [tagIter["title"] for tagIter in tag_arrays[0]]:
            tag_arrays[0].append(tag2)

writeFinalJson(jsons[0])