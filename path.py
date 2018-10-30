import pathlib
p = pathlib.Path('.') # Current directory
for x in p.iterdir():
    if x.is_dir(): # see also x.is_file()
        print(x)

