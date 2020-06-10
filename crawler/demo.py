import json
import math
import urllib.request


def split_data(arr):
    a, b = int(min(arr)), int(max(arr))
    # print(a, b)
    return [a + (b - a) * i / 3 for i in range(4)]


with open('test.json', encoding='utf-8') as json_file:
    jsonData = json.load(json_file)
    screens = []
    rams = []
    cameras = []
    selfie = []
    pins = []
    for telephone in jsonData:
        # urllib.request.urlretrieve(telephone['img'], 'images/{}.{}'.format(telephone['name'], telephone['img'][-3:]))
        try:
            screens.append(float(telephone['screen'][0:4].strip()))
            rams.append(int(telephone['ram'][0:3].strip()))
            # print(telephone['camera'])
            cameras.append({
                "chinh": telephone['camera'].split('&')[0][6:].strip(),
                "phu": telephone['camera'].split('&')[1][4:].strip().split(',')
            })
            selfie.append(telephone['selfie'])
            pins.append(telephone['pin'].strip().split(",")[0].split(" ")[0])

        except:
            pass
    print(pins)
    # print(selfie)
    print(screens)
    a, b = min(screens), max(screens)
    arr_screen = [a + (b - a)*i/3 for i in range(4)]
    # print(arr)
    # print(selfie)
    # print(rams)
    # a, b = min(rams), max(rams)
    # arr_rams = [a + (b - a)*i/3 for i in range(4)]
    # print(arr_rams)
    main_camera = []
    side_camera = []
    for camera in cameras:
        arr = camera['chinh'].split(" ")[0]
        main_camera.append(arr)
        side_camera.append(
            camera['phu'][0].split(" ")[0]
        )
    print("-------------------------------------")
    print("camera_chinh {}".format(len(main_camera)))
    print("-------------------------------------")
    print("camera_phu", len(side_camera))
    print("-------------------------------------")
    print("manhinh ",screens)
    print("-------------------------------------")
    print("selfie ",[ i.strip() for i in selfie])
    print("-------------------------------------")
    print("ram ", rams)

    # print(split_data(main_camera))
