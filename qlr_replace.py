#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import os
import re
import sys


def rename_host(ROOTDIR, NEWHOST):
    #Looper over filer i mapper/undermapper
    for subdir, dirs, files in os.walk(ROOTDIR):
        for f in files:
            filepath = os.path.join(subdir, f)
            #For hver fil skrives "Editing: filename"
            print('Editing: ' + filepath)
            tree = ET.parse(filepath)
            root = tree.getroot()
            for ds in root.findall('maplayers/maplayer/datasource'):
                ds.text = re.sub(r'host=[^\s]*', 'host=%s' % NEWHOST, ds.text)
            tree.write(filepath)

if __name__ == '__main__':
    #Angiv rodfolderen for qlr-filerne
    ROOTDIR = sys.argv[1]

    #Angiv den nye host
    NEWHOST = sys.argv[2]

    rename_host(ROOTDIR, NEWHOST)
