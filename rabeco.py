from glob import glob
from string import ascii_lowercase
from random import choice

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import keyboard


cmaps = ('viridis', 'plasma', 'inferno', 'magma', 'cividis',
         'Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
         'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
         'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn',
         'binary', 'gist_yarg', 'gist_gray', 'gray', 'bone', 'pink',
         'spring', 'summer', 'autumn', 'winter', 'cool', 'Wistia',
         'hot', 'afmhot', 'gist_heat', 'copper',
         'PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu',
         'RdYlBu', 'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic',
         'twilight', 'twilight_shifted', 'hsv',
         'Pastel1', 'Pastel2', 'Paired', 'Accent',
         'Dark2', 'Set1', 'Set2', 'Set3',
         'tab10', 'tab20', 'tab20b', 'tab20c',
         'flag', 'prism', 'ocean', 'gist_earth', 'terrain', 'gist_stern',
         'gnuplot', 'gnuplot2', 'CMRmap', 'cubehelix', 'brg',
         'gist_rainbow', 'rainbow', 'jet', 'turbo', 'nipy_spectral',
         'gist_ncar')

valid_ext = ('png', 'jpg', 'gif')
img_files = []
[img_files.extend(glob('./data/*.' + ext)) for ext in valid_ext]

img = [mpimg.imread(img_file)[:, :, 0] for img_file in img_files]

fig = plt.figure()
figManager = plt.get_current_fig_manager()
figManager.full_screen_toggle()

print('Going for while loop...')
while True:
    if keyboard.read_key() in tuple(ascii_lowercase):
        print('You pressed a key!')
        plt.clf()
        plt.imshow(choice(img), cmap=choice(cmaps))
        plt.axis('off')
        plt.pause(0.01)
    elif keyboard.is_pressed('esc'):
        print('Stopping while loop!')
        plt.close('all')
        break

print('end')
