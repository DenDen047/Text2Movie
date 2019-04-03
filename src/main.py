import os
import sys
import re
import glob

import cv2


def read_markdown(file_path):
    # Markdown -> HTML -> BeautifulSoup
    soup = None
    return soup


def soup2source(soup):
    source = None
    return source


def text_frame(text):
    frames = [None]
    return frames

def generate_movie(source, width, height, result_path):
    # 形式はMP4Vを指定
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    fps = 20
    # 出力先のファイルを開く
    out = cv2.VideoWriter(result_path, int(fourcc), fps, (int(width), int(height)))

    # 動画を生成
    for part in source:
        # 要素の性質に分けて処理
        if part['type'] == 'text':
            frames = text_frame(part['text'])
        # 生成したフレームを書き込み
        for f in frames:
            out.write(f)


def main():
    # MarkDownファイルを読み込む
    soup = read_markdown()

    # BeautifulSoupを用いて、HTMLを解析する
    source = soup2source(soup)

    # 動画を生成
    result_path = 'output.m4v'
    width = 720
    height = 480
    generate_movie(source, width, height, result_path)


if __name__ == '__main__':
    main()