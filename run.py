import json
import PIL
from PIL import Image
import sys

try:
    a = sys.argv[1]
except:
    raise Exception('Missing screenshot argument!')
database = json.load(open("phone_resolutions.json"))
img = PIL.Image.open(sys.argv[1])
width, height = img.size
resolution = f"{width}x{height}"
phone = []
try:
    for k, v in database.items():
        for i in v:
            if resolution == i:
                phone.append(k)
    raise Exception()
except:
    if phone == []:
        phone.append("I can't seem to figure out what phone this screenshot came from...")
    print(f"\nScreenshot Resolution: {resolution}\n")
    print("Suspected Phones: \n\n" + '\n'.join(phone) + "\n")