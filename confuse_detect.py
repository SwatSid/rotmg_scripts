import cv2
import numpy as np

# status effects above character center point : 780,607
# status effects top left : 738,597
# status effects bottom right : 822,616

# in paint, the coordinates are displayed as cols, rows

def find_confuse_status(img, tpl):
    
    roi_status_effect_rows = slice(597,616)
    roi_status_effect_cols = slice(738,822)

    roi_status_effect = img[roi_status_effect_rows, roi_status_effect_cols]
    # cv2.imshow('Status effect area', roi_status_effect)
    
    im = np.atleast_3d(roi_status_effect)
    tpl = np.atleast_3d(tpl)
    H, W, D = im.shape[:3]
    h, w = tpl.shape[:2]

    # Integral image and template sum per channel
    sat = im.cumsum(1).cumsum(0)
    tplsum = np.array([tpl[:, :, i].sum() for i in range(D)])

    # Calculate lookup table for all the possible windows
    iA, iB, iC, iD = sat[:-h, :-w], sat[:-h, w:], sat[h:, :-w], sat[h:, w:] 
    lookup = iD - iB - iC + iA
    # Possible matches
    possible_match = np.where(np.logical_and.reduce([lookup[..., i] == tplsum[i] for i in range(D)]))

    # Find exact match
    for y, x in zip(*possible_match):
        if np.all(im[y+1:y+h+1, x+1:x+w+1] == tpl):
            return (y+1, x+1)

    # raise Exception("Image not found")
    return None
    
def main():
    im = cv2.imread('./confuse_img_1.png')
    template = cv2.imread('./confuse_icon.png')

    print(find_confuse_status(im, template))
   
if __name__ == '__main__':
    main()