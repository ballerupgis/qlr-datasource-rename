#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import os
import re
import argparse


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

    #Parametre for argparse modulet
    parser = argparse.ArgumentParser()
    parser.add_argument("ROOTDIR", help="Specify the root directory of qlr files")
    parser.add_argument("NEWHOST", help="Specify the new host adress")
    args = parser.parse_args()

    #Angiv rodfolderen for qlr-filerne
    ROOTDIR = args.ROOTDIR

    #Angiv den nye host
    NEWHOST = args.NEWHOST

    rename_host(ROOTDIR, NEWHOST)
