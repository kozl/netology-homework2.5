#!/usr/bin/env python3
import glob
import os.path
import subprocess


SOURCE_DIR = os.path.join(os.path.dirname(__file__), 'Source')
RESULT_DIR = os.path.join(os.path.dirname(__file__), 'Result')

if __name__ == '__main__':
    if not os.path.exists(RESULT_DIR):
        os.mkdir(RESULT_DIR)
    images = glob.glob(os.path.join(SOURCE_DIR,'*.jpg'))
    for image in images:
        subprocess.call(['convert', image, '-resize', '200', os.path.join(RESULT_DIR, os.path.basename(image))])