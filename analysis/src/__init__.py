import os
from .geographic_distribution import *


def stopwords_list():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    stopwords_path = os.path.join(current_dir, 'stopwords.txt')
    with open(stopwords_path, 'r', encoding='utf-8') as f:
        stopwords = f.readlines()
    stopwords = [word.strip() for word in stopwords]
    return stopwords