import os

start_path = input("what directory would you like the size of?: ")

def dir_size(start_path):
    size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if not os.path.islink(fp):
                size  += os.path.getsize(fp)
                print(f"{fp}: {size} bytes")
    return size

print(dir_size(start_path), 'bytes')


if dir_size(start_path) >= 1000:
    print(f"{start_path} exceeds 1000 bytes!")