import os
import sys
import re
import glob

import cv2


def read_markdown():
    return None


def analysis_markdown(md_file):
    return None


def generate_movie(source):
    pass


def main():
    # MarkDownファイルを読み込む
    md_file = read_markdown()

    # MDの構文を解析
    source = analysis_markdown(md_file)

    # 動画を生成
    generate_movie(source)


if __name__ == '__main__':
    main()