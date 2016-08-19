#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import os

#Angiv rodfolderen for qlr-filerne
rootdir = '/Volumes/DISK_IMG/qlr_dims'

#Angiv den nye host
newhost = 'anders'

#Looper over filer i mapper/undermapper
for subdir, dirs, files in os.walk(rootdir):
    for f in files:
        filepath = os.path.join(subdir, f)
        #For hver fil skrives "Editing: filename"
        print ('Editing: ' + filepath)
        tree = ET.parse(filepath)
        root = tree.getroot()
        maplayers = root.findall('maplayers')
        for group_of_maplayers in maplayers:
            for maplayer in group_of_maplayers:
                splitted = maplayer.find('datasource').text.split()
                for n,i in enumerate(splitted):
                    if i.startswith('host'):
                        host = 'host=' + newhost
                        splitted[n] = host
                maplayer.find('datasource').text = ' '.join(splitted)
        tree.write(filepath)
