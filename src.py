import json
import os

json_files = []
for f in os.listdir(os.getcwd()):
    if f.endswith('.json'):
        json_files.append(f)

jsons = []
with open(json_files[0], encoding="utf-8") as f:
    jsons.append(json.load(f))

with open(json_files[1], encoding="utf-8") as f:
    jsons.append(json.load(f))

tag_arrays = [j["tagGroups"] for j in jsons]

# for elem in jsons[0]["tagGroups"]:
#     print(elem)

i = -1
for tag in tag_arrays[0]:
    i += 1
    title = tag["title"]
    child_tags = tag["children"]
    for tag2 in tag_arrays[1]:
        if tag2["title"] == title:
            for child_tag2 in tag2["children"]:
                if child_tag2 not in child_tags:
                    print(title)
                    print(child_tag2)
                    child_tags.append(child_tag2)
            tag_arrays[0][i]["children"] = child_tags
            break

print(tag_arrays[0])