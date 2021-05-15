#!/usr/bin/env python

"""
Rabeco fun for kids
"""

from glob import glob
from string import ascii_lowercase
from random import choice

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import keyboard

def load_images(path):
    valid_ext = ('png', 'jpg', 'gif')
    img_files = []
    [img_files.extend(glob('{}/*.{}'.format(path, ext))) for ext in valid_ext]
    assert img_files, IOError('No image files found in {}'.format(path))

    imgs = [mpimg.imread(img_file)[:, :, 0] for img_file in img_files]

    return imgs


def main():
    imgs = load_images('./data/')

    fig = plt.figure()
    figManager = plt.get_current_fig_manager()
    figManager.full_screen_toggle()

    print('Going for while loop...')
    while True:
        if keyboard.read_key() in tuple(ascii_lowercase):
            print('You pressed a key!')
            plt.clf()
            plt.imshow(choice(imgs), cmap=choice(plt.colormaps()))
            plt.axis('off')
            plt.pause(0.01)
        elif keyboard.is_pressed('esc'):
            print('Stopping while loop!')
            plt.close('all')
            break

    print('end')


if __name__ == '__main__':
    main()
