#!/usr/bin/python

import re
import os

for file in os.listdir('.'):
    if file.find('.vtt')>0:
        print('processing: %s' %file),
        infile=open(file)
        outfile=open(file.replace('.vtt','.srt'),'w')

        for line in infile:
            # line=line.strip()
            line=line.replace('WEBVTT','')
            line=re.sub('(\d)\.(\d)','\g<1>,\g<2>',line)
            outfile.write(line)
        print('done')
        outfile.close()
