# Regular
def regular_io(file):
    with open(file, mode="r", encoding="utf8") as file_obj:
        text = file_obj.read()
        print(text)


# Fast and emproved
import mmap


def mmap_io(file):
    with open(file, mode="r", encoding="utf8") as file_obj:
        with mmap.mmap(
            file_obj.fileno(), length=0, access=mmap.ACCESS_READ
        ) as mmap_obj:
            text = mmap_obj.read()
            print(text, 3)
