import os
import sys
import re
import glob

import cv2
from PIL import Image
import numpy as np


# width方向にリサイズ
def vconcat_resize_min(im_list, interpolation=cv2.INTER_CUBIC):
    w_min = min(im.shape[1] for im in im_list)
    im_list_resize = [
        cv2.resize(
            im, (w_min, int(im.shape[0] * w_min / im.shape[1])),
            interpolation=interpolation)
        for im in im_list]
    return cv2.vconcat(im_list_resize)

# height方向にリサイズ
def hconcat_resize_min(im_list, interpolation=cv2.INTER_CUBIC):
    h_min = min(im.shape[0] for im in im_list)
    im_list_resize = [
        cv2.resize(
            im, (int(h_min * im.shape[1] / im.shape[0]), h_min),
            interpolation=interpolation)
        for im in im_list]
    return cv2.hconcat(im_list_resize)


def main():
    # 画像パスを取得
    files = glob.glob('/data/*')
    images = []
    for f in files:
        if re.search('.+.(jpg|png)', f):
            images += [f]
    # 全ての画像をロード
    imgs = []
    images = sorted(images)
    for image in images:
        imgs.append(cv2.imread(image))

    # 画像を結合
    result = hconcat_resize_min(imgs)

    # 保存
    cv2.imwrite('/data/result.png', result)


if __name__ == '__main__':
    main()