# 词云图可视化
from math import ceil
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def _wordcloud(frequencies:dict):
    wordcloud = WordCloud(
        font_path='simhei.ttf',
        background_color='white',
        colormap='viridis',
        width=1000,
        height=800,
        max_words=100,
        max_font_size=150,
        random_state=42
    ).generate_from_frequencies(frequencies)
    return wordcloud

def freq_dict_wordcloud(freq_dict:dict, sup_title, save_path=None):
    m = 4
    n = ceil(len(freq_dict) / m)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.figure(figsize=(m*2, n*2))
    plt.suptitle(sup_title)
    i = 0
    for _, (title, freq) in enumerate(freq_dict.items()):
        if not freq: continue
        plt.subplot(n, m, i+1)
        i += 1
        wordcloud = _wordcloud(freq)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title(title)
    plt.tight_layout(h_pad=0.2, w_pad=0.2, rect=(0, 0, 1, 0.98))
    if save_path: 
        plt.savefig(save_path, dpi=300)
    plt.show()

