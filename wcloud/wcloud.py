# -*- coding: utf-8 -*-
import os

import numpy as np
from PIL import Image
from wordcloud import WordCloud

stopwords = set([x.strip() for x in open(os.path.join(
    os.path.dirname(__file__), 'stopwords.txt')).read().split('\n')])


def _load_mask(mask_fname):
    return np.asarray(Image.open(mask_fname))


def generate_wordcloud(text, bgcolor, width, height, max_words, mask):
    if mask is not None:
        mask = _load_mask(mask)
    wc = WordCloud(relative_scaling=.5, width=width, height=height,
                   background_color=bgcolor, mask=mask,
                   max_words=max_words, stopwords=stopwords)
    return wc.generate_from_text(text)
