# Regular
def regular_io(file):
    with open(file, mode="r", encoding="utf8") as file_obj:
        text = file_obj.read()
        print(text)


regular_io("a.txt")
# Fast and emproved
import mmap


def mmap_io(filename):
    with open(filename, mode="r", encoding="utf8") as file_obj:
        with mmap.mmap(
            file_obj.fileno(), length=0, access=mmap.ACCESS_READ
        ) as mmap_obj:
            text = mmap_obj.read()
            print(text)


mmap_io("a.txt")
