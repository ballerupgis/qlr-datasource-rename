'''kilde: http://stackoverflow.com/a/20593644 og http://stackoverflow.com/a/20593644'''
import fileinput
import os

rootdir = 'C:\\andb\\python\\Temastyring'
oldhost = '172.30.1.161'
newhost = 'gc2'

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        print (os.path.join(subdir, file))
        with fileinput.FileInput(os.path.join(subdir, file), inplace=True, backup='.bak') as qlrfile:
            for line in qlrfile:
                print(line.replace("host=\'" + oldhost + "\'", "host=\'" + newhost + "\'"), end='')


# print (os.path.join(subdir, file))

