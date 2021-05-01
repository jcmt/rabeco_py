import keyboard
import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


cmaps = ['viridis', 'plasma', 'inferno', 'magma', 'cividis',
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
         'gist_ncar']

img = mpimg.imread('./data/stinkbug.png')[:, :, 0]

plt.ion()
fig = plt.figure()
figManager = plt.get_current_fig_manager()
figManager.full_screen_toggle()

while True:
    try:
        if keyboard.is_pressed('a'):
            print('You Pressed A Key!')
            plt.clf()
            plt.imshow(img, cmap=random.choice(cmaps))
            plt.axis('off')
            plt.pause(0.01)
    except:
        break

print('end')
