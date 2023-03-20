# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: #
# Date: 15.09.2016                                                            #
# Author: Ole-Johan Skrede                                                    #
#                                                                             #
# Solution proposal as part of the exercise program in                        #
# INF4300 - Digital image analysis at the University of Oslo                  #
#                                                                             #
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: #
"""
Illustration of chain code use as part of exercise 4.
"""

# pylint: disable=bad-indentation
# pylint: disable=redefined-outer-name

import numpy as np
import matplotlib.pyplot as plt
import cv2 
import chain_code as cc

# ============= #
# PROGRAM START #
# ============= #

#print('='*80)
#print('Supplement to notes in INF4300')
#print('Week 4')
#print('Freeman chain codes')
#print('-'*80)

connectivity = 8
background = 0
image=cv2.imread('nuevo_numero82.png', cv2.IMREAD_GRAYSCALE)
if len(np.unique(image)) == 2:
  bg, fg = np.unique(image)
  image[image == bg] = background
  image[image == fg] = 255

chain_code, boundary_pixels, tortuosidad = cc.trace_boundary(image, connectivity, background)

image_with_boundary = np.copy(image)
for x, y in boundary_pixels:
  image_with_boundary[x, y] = 150

print('Chain code:')
print(chain_code)
print('Tortuosidad:')
print(tortuosidad)
#print('Start point normalization:')
#mcs_chain_code = cc.minimum_circular_shift(chain_code)
#print(mcs_chain_code)
#print('Rotation normalization:')
#fdt_chain_code = cc.first_difference_transform(chain_code, connectivity)
#print(fdt_chain_code)
#print('Rotation and start point normalization:')
#rs_chain_code = cc.minimum_circular_shift(fdt_chain_code)
#print(rs_chain_code)

fig = plt.figure()

ax1 = fig.add_subplot(1, 2, 1)
ax1.imshow(image, cmap='gray', interpolation='none', vmin=0, vmax=255)
ax1.set_title('Image')
if image.shape[0] and image.shape[1] < 20:
  # Note that matplotlib uses the opposite x,y, naming convention
  ax1.set_xticks(np.arange(0, image.shape[1]))
  ax1.set_xticks(np.arange(0.5, image.shape[1] + 0.5), minor=True)
  ax1.set_yticks(np.arange(0, image.shape[0]))
  ax1.set_yticks(np.arange(0.5, image.shape[0] + 0.5), minor=True)
  ax1.grid(b=True, which='minor', linestyle='-')

ax1 = fig.add_subplot(1, 2, 2)
ax1.imshow(image_with_boundary, cmap='gray', interpolation='none', vmin=0, vmax=255)
ax1.set_title('Image with boundary')
if image_with_boundary.shape[0] and image_with_boundary.shape[1] < 20:
  # Note that matplotlib uses the opposite x,y, naming convention
  ax1.set_xticks(np.arange(0, image_with_boundary.shape[1]))
  ax1.set_xticks(np.arange(0.5, image_with_boundary.shape[1] + 0.5), minor=True)
  ax1.set_yticks(np.arange(0, image_with_boundary.shape[0]))
  ax1.set_yticks(np.arange(0.5, image_with_boundary.shape[0] + 0.5), minor=True)
  ax1.grid(b=True, which='minor', linestyle='-')


plt.show()
