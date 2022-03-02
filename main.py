#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# --------------------------------------------------------
# 诗云Lite (Poem Cloud Lite) Ver 0.4
# Copyright (c) 2022 MoeTwo Studio
# Licensed under The MIT License
# Written by Coolsong
# 提示：在运行本程序前请先阅读自述文件。
# Tip: Please read the readme file before running this.
# https://github.com/Coolsong-max/Poem_cloud_lite
# --------------------------------------------------------

def main():
    file = open('./out/out.txt', 'w')  # 创建输出文档
    ziku = open('./zikueng.txt')  # 读取字库
    lines = ziku.readlines()
    sentence = ''.join(lines)
    alphabet = [one for one in sentence]
    count = 0
    w = []

    alpha_len = len(alphabet)

    for i in range(length):
        w.append(0)

    # alphabet.insert(0, '')
    # w[0] += 1

    while w[-1] != alpha_len:
        # word = []
        # count += 1
        # for a in range(length):
        #     m = w[a]
        #     word.append(alphabet[m])
        # w[0] += 1
        #
        # for i in range(length):
        #     if w[i] == alpha_len and i + 1 != length:
        #         w[i] = 0
        #         w[i + 1] += 1
        #
        # word = word[::-1]
        #
        # wordStr = ''.join(word)
        # out = str(count) + ': ' + wordStr + '\n'

        poem = []
        count += 1
        for p in range(poemSentence):
            word = []
            for a in range(length):
                m = w[a]
                word.append(alphabet[m])
            w[0] += 1

            for i in range(length):
                if w[i] == alpha_len and i + 1 != length:
                    w[i] = 0
                    w[i + 1] += 1

            wordStr = ''.join(word[::-1])
            poem.append(wordStr)

        poemStr = '，'.join(poem)
        out = str(count) + ': ' + poemStr + '。\n'

        file.write(out)  # 保存运行结果
        print(f'{out}')

    input('运行结束。')


if __name__ == '__main__':
    length = 5  # 单句字数
    poemSentence = 2  # 每首句数
    main()
