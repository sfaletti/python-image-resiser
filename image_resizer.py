import os
from PIL import Image
import Tkinter, tkFileDialog

sizes = {'thumb': 360, 'small': 640, 'medium': 960, 'large': 1280}
# change this dictionary if you want different file names and output sizes.

def split_path(img_path):
    _path = os.path.split(img_path)
    _file = os.path.splitext(_path[1])
    # print img_path
    print _path, _file

def find_file(path):
    for sub in os.listdir(path):
        _path = path + '/' + sub
        name, extension = os.path.splitext(sub)
        extensions = ['.jpg', '.png']
        if extension in extensions:
            split_path(_path)
            resize_image(_path)
        elif os.path.isdir(_path):
            find_file(_path)

def resize_image(img_path, sizes=sizes):
    extension_map = {'.jpg':'JPEG', '.png':'PNG'} 
    #converts file extensions into something useable by PIL. Add more if you like.
    _path = os.path.split(img_path)
    _file = os.path.splitext(_path[1])
    im = Image.open(img_path)
    im_ratio = 1.0 * im.size[1] * 1.0 / im.size[0]
    print im_ratio
    for key in sizes.keys():
        new_size = (int(sizes[key]), int(sizes[key]*im_ratio))
        resized_img = im.resize(new_size)
        resized_img.save(str(_path[0]) + '/' + str(_file[0]) + '-' + key + str(_file[1]), extension_map[_file[1]])

root = Tkinter.Tk()
dirname = tkFileDialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')
find_file(dirname)
