#!/usr/bin/env python3
import glob
import os.path
import subprocess
from multiprocessing import Pool


SOURCE_DIR = os.path.join(os.path.dirname(__file__), 'Source')
RESULT_DIR = os.path.join(os.path.dirname(__file__), 'Result')

def resize_image(image_path):
    subprocess.call(['convert', image_path, '-resize', '200', os.path.join(RESULT_DIR, os.path.basename(image_path))])

if __name__ == '__main__':
    if not os.path.exists(RESULT_DIR):
        os.mkdir(RESULT_DIR)
    pool = Pool(4)
    images = glob.glob(os.path.join(SOURCE_DIR,'*.jpg'))
    pool.map(resize_image, images)