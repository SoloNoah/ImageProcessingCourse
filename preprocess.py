import argparse
from datetime import datetime
import cv2
import os.path

'''Authors: Emilia Zorin, Noah Solomon'''


def grey_scale(path):
    return cv2.imread(path, 0)


def padding(img):
    h, w = img.shape[:2]
    dif = abs((h - w) // 2)
    dim = (40, 40)
    if h > w:
        # padding added to left and right
        img = cv2.copyMakeBorder(img, 0, 0, dif, dif, cv2.BORDER_CONSTANT, value=255)

    elif h < w:
        # padding top and bottom
        img = cv2.copyMakeBorder(img, dif, dif, 0, 0, cv2.BORDER_CONSTANT, value=255)
    return cv2.resize(img, dim, interpolation=cv2.INTER_AREA)


def traverse_folder(path, save_path):
    if not os.path.exists(save_path):
        os.mkdir(save_path)
        for folder in os.listdir(path):
            os.mkdir(os.path.join(save_path, folder))
            folder_path = os.path.join(path, folder)
            for file in os.listdir(folder_path):
                try:
                    img_path = os.path.join(folder_path, file)
                    if not os.path.exists(img_path):
                        raise Exception("Path doesn't exist")
                    img = grey_scale(img_path)
                    img = padding(img)
                    cv2.imwrite(os.path.join(save_path, folder, file), img)
                except Exception as err:
                    print("{} ".format(err))
    else:
        print("path {} exists already. Delete to proceed with this programs preprocessing.".format(save_path))


def main():
    parse = argparse.ArgumentParser()
    parse.add_argument("path", metavar='path', choices=['TEST', 'TRAIN'], type=str,
                       help="Choose path for preprocessing.")
    args = parse.parse_args()

    start = datetime.now()
    print(f"[Preprocessing] start time: {datetime.now()}")
    process_path = "Preprocessed_" + args.path

    traverse_folder(args.path, process_path)
    print(f"[Preprocessing] end time: {datetime.now()}")

    print("The preprocess.py script ran {}".format(datetime.now() - start))


main()
