import os
import shutil
from os import listdir
from os.path import isfile, join

PATH = "C:/Users/Chenmeng/Documents/WeChat Files/wxid_3637116365022/FileStorage/File/2022-09"

files = [file for file in listdir(PATH) if isfile(join(PATH, file))]
# file_types = []
# sub_directories = {}

number = 1
for file in files:
    file_type = file.rsplit(".", 1)[1]
    new_directory = PATH + "/" + file_type + "_folder"
    source_path = PATH + "/" + file
    # if file_type not in file_types:
    #     file_types.append(file_type)
    # if file_type not in sub_directories.keys():
    #     sub_directories["file_type"] = new_directory_name
    if not os.path.isdir(new_directory):
        os.mkdir(new_directory)
    shutil.move(source_path, new_directory)
    print(f"{number}. Moved {file} from {PATH} to {new_directory}.")
    number += 1
