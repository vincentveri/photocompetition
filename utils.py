from os import listdir
from os.path import isfile, join

workdir = 'd:\\Photos\\2025\\02\\'
cartelle = [d for d in listdir(workdir) if not isfile(join(workdir, d))]


def get_photos(destination):
    curdir = join(workdir, destination)
    photos = [f for f in listdir(curdir) if isfile(join(curdir, f))]
    return photos