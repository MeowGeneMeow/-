
# import fasttext
# model = fasttext.train_unsupervised('/Users/gene1214/Desktop/畢業專案/FastText/data/fil9')
# model.words
# model.get_word_vector("the")

# model.save_model("result.bin")

# $ python
# >>> import fasttext
# >>> model = fasttext.load_model('/Users/gene1214/Desktop/畢業專案/FastText/fastText/result.bin')
# model = fasttext.load_model('/Users/gene1214/Desktop/畢業專案/FastText/wiki-news-300d-1M.vec')

import io
import fasttext

def load_vectors(fname):
    fin = io.open(fname, 'r', encoding='utf-8', newline='\n', errors='ignore')
    n, d = map(int, fin.readline().split())
    data = {}
    for line in fin:
        tokens = line.rstrip().split(' ')
        data[tokens[0]] = map(float, tokens[1:])
    return data

# 載入嵌入向量
vectors_file = '/Users/gene1214/Desktop/畢業專案/FastText/wiki-news-300d-1M.vec'
model = fasttext.load_model('/Users/gene1214/Desktop/畢業專案/FastText/fastText/result.bin')
model.load_vectors(vectors_file)
