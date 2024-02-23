from gensim.models import Word2Vec
import jieba
#
def func(word1,word2):
    raw=[jieba.lcut("番茄很好吃"),jieba.lcut("西红柿番茄")]
    # print(raw)
    model=Word2Vec(raw,vector_size=192,min_count=1)
    return float(model.wv.similarity("番茄","西红柿"))
if __name__ == '__main__':
    print(func("番茄", "西红柿"))