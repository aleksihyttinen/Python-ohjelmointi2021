#Tämä scripti etsii kuvat kansiosta ja alakansioista
import os #järjestelmään liittyvät toiminnallisuudet

def find_pics(dir, pics):
    files = os.listdir(dir)
    for file in files:
        path = os.path.join(dir, file)
        if os.path.isdir(path):
            find_pics(path, pics)
        else:
            fileName = file.lower()
            if fileName.endswith(".png") or fileName.endswith(".jpg"):
                pics.append(path)
    return pics

pics = []
current_dir = os.path.dirname(os.path.realpath(__file__))
find_pics(current_dir, pics)

for pic in pics:
    print(pic)