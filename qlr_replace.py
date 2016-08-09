#!/usr/bin/env python3
import fileinput
import os

#Angiv rodfolderen for qlr-filerne
rootdir = 'C:\\andb\\python\\Temastyring'
#Angiv den gamle host
oldhost = 'gc2'
#Angiv den nye host
newhost = 'anders'

#Looper over filer i mapper/undermapper
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        #For hver fil skrives "Editing: filename" 
        print ('Editing: ' + os.path.join(subdir, file))
        with fileinput.FileInput(os.path.join(subdir, file), inplace=True) as qlrfile:
            #Looper over hver linie i qlr-filerne
            for line in qlrfile:
                #host erstattes hvis oldhost findes i qlr-filen
                print(line.replace("host=" + oldhost , "host=" + newhost), end='')
