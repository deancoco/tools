import os, platform

base_dir = os.path.dirname(__file__)

def filename_maker(dirname, prefix):
    if platform.system() is not "Windows":
        print("只支持window系统")
        return
    file_list = os.listdir(dirname)
    for file in file_list:
        if os.path.isfile(dirname + r"\\" +file) and not file.startswith(prefix):
            os.rename(os.path.join(dirname, file), dirname + r"\\" + prefix +file)

