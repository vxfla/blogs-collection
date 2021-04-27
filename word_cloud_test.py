#!/usr/bin/Python
# -*- coding: utf-8 -*-
from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
import jieba
from wordcloud import WordCloud, STOPWORDS,ImageColorGenerator

def form():
    ###当前文件路径
    d = path.dirname(__file__)

    color_list=['#E6789B','#89E8FA','#967DF3']#设置字体颜色

    colormap=colors.ListedColormap(color_list)#设计字体颜色

    # Read the whole text.
    file = open('cnblogs.txt','rb').read()#读取txt文档
    ##进行分词
    #刚开始是分完词放进txt再打开却总是显示不出中文很奇怪
    default_mode =jieba.cut(file)
    text = " ".join(default_mode).replace('的','')
    alice_mask = np.array(Image.open('Vinyl_mask.jpeg'))#加载背景图片
    stopwords = set(STOPWORDS)
    stopwords.add("said")
    wc = WordCloud(
        #设置字体，不指定就会出现乱码,这个字体文件需要下载
        font_path=r'simfang.ttf',#自己去电脑里找可以用的字体
        background_color="white",
        max_words=500,
        mask=alice_mask,
        colormap=colormap,
        random_state=3,
        scale=10,
        stopwords=stopwords)
    # generate word cloud
    wc.generate(text)

    # store to file
    wc.to_file(path.join(d, "B_word.jpg"))#输出图片

    # show
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.figure()
    plt.imshow(alice_mask, cmap=plt.cm.gray, interpolation='bilinear')
    plt.axis("off")

