import numpy as np
import os
from TAADToolbox.utils import WordVector, make_zip_downloader

NAME = "CounterFit"

URL = "https://thunlp.oss-cn-qingdao.aliyuncs.com/TAADToolbox/counter-fitted-vectors.txt.zip"
DOWNLOAD = make_zip_downloader(URL, "counter-fitted-vectors.txt")

def LOAD(path):
    with open(os.path.join(path, "counter-fitted-vectors.txt"), "r") as f:
        id2vec = []
        word2id = {}
        for line in f.readlines():
            tmp = line.strip().split(" ")
            word = tmp[0]
            embed = np.array([float(x) for x in tmp[1:]])
            if len(embed) != 300:
                continue
            word2id[word] = len(word2id)
            id2vec.append(embed)
        id2vec = np.stack(id2vec)
    return WordVector(word2id, id2vec)
