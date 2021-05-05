import cv2
import numpy as np

# status effects above character center point : 780,607
# status effects top left : 738,597
# status effects bottom right : 822,616

# in paint, the coordinates are displayed as cols, rows

roi_status_effect_rows = slice(597,616)
roi_status_effect_cols = slice(738,822)

img = cv2.imread('./confuse_img_1.png')

# roi_status_effect = img[roi_status_effect_rows[0]:roi_status_effect_rows[1], roi_status_effect_cols[0]:roi_status_effect_cols[1]]
roi_status_effect = img[roi_status_effect_rows, roi_status_effect_cols]
cv2.imshow('Status effect area', roi_status_effect)

cv2.waitKey(0)