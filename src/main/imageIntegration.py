#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import numpy as np

bgi = np.zeros((1080, 1920, 3), np.uint8)
bgi[:, :, :] = 255

cv2.imwrite('back.jpg', bgi)


# In[ ]:




