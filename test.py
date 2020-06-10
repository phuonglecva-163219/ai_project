import json
from urllib.error import HTTPError
from urllib.request import urlretrieve


with open("comments.json", "r", encoding="utf-8") as input:
    data = json.load(input)

# list_item = []
# for (id, telephone) in enumerate(data):
#     item = telephone
#     item["id"] = id
#     list_item.append(item)
# print(list_item)
# for telep in data:
#     print(telep)
# print(len(data))

# load images
try:
    for (index, telephone) in enumerate(data):
        image_url = telephone['img']
        image_local_path = "images_1/{}.jpg".format(index)
        urlretrieve(image_url, image_local_path)
except FileNotFoundError as err:
    print(err)   # something wrong with local path
except HTTPError as err:
    print(err)  # something wrong with url

# # index = 1
# file_out = []

# for index, telephone in enumerate(data):
#     file_out.append({
#         "id": index,
#         "name": telephone['name'],
#         "price": telephone['price'],
#         "img": telephone['img'],
#         "screen": telephone['screen'],
#         "cpu": telephone['cpu'],
#         "ram": telephone['ram'],
#         "camera": telephone['camera'],
#         "selfie": telephone['selfie'],
#         "pin": telephone['pin']
#     })
# with open("sample.json", "w", encoding="utf-8") as output:
#     output.write(json.dumps(file_out, indent=2))
