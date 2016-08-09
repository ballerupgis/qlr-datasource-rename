#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import fileinput
import os

#Angiv rodfolderen for qlr-filerne
rootdir = 'C:\\andb\\python\\Temastyring'
rootdir = '/home/josef/tmp/test/'
#Angiv den gamle host
oldhost = 'gc2'
#Angiv den nye host
newhost = 'anders'

#Looper over filer i mapper/undermapper
for subdir, dirs, files in os.walk(rootdir):
    for f in files:
        #For hver fil skrives "Editing: filename"
        print ('Editing: ' + os.path.join(subdir, f))
        with fileinput.FileInput(os.path.join(subdir, f), inplace=True) as qlrfile:
            #Looper over hver linie i qlr-filerne
            for line in qlrfile:
                #host erstattes hvis oldhost findes i qlr-filen
                print(line.replace("host=" + oldhost , "host=" + newhost), end='')
