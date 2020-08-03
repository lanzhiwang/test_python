from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.linalg import norm
import numpy as np


def jaccard_similarity(s1, s2):
    def add_space(s):
        return ' '.join(list(s))

    # 预处理，将字中间加入空格
    s1, s2 = add_space(s1), add_space(s2)
    # 形成语料库
    corpus = [s1, s2]

    # 转化为 TF 矩阵，实例化 CountVectorizer 对象
    cv = CountVectorizer(tokenizer=lambda s: s.split())
    vectors = cv.fit_transform(corpus).toarray()
    print(vectors)
    """
    [[0 0 1 1 1 1 1]
     [1 1 1 1 0 1 1]]
    """
    print(cv.get_feature_names())  # ['么', '什', '你', '呢', '嘛', '在', '干']
    """
    杰卡德系数
    """
    # 求交集
    numerator = np.sum(np.min(vectors, axis=0))
    print(numerator)  # 4
    # 求并集
    denominator = np.sum(np.max(vectors, axis=0))
    print(denominator)  # 7
    # 计算杰卡德系数
    print(1.0 * numerator / denominator)  # 0.5714285714285714
    """
    TF 计算
    """
    # 通过 TF 系数计算相似度
    print(
        np.dot(vectors[0], vectors[1]) /
        (norm(vectors[0]) * norm(vectors[1])))  # 0.7302967433402214
    """
    TFIDF 计算
    """
    # 转化为 TF 矩阵
    cv = TfidfVectorizer(tokenizer=lambda s: s.split())
    vectors = cv.fit_transform(corpus).toarray()
    print(vectors)
    """
    [[0.         0.         0.4090901  0.4090901  0.57496187 0.4090901
      0.4090901 ]
     [0.49844628 0.49844628 0.35464863 0.35464863 0.         0.35464863
      0.35464863]]
    """
    # 通过 TFIDF 系数计算相似度
    print(
        np.dot(vectors[0], vectors[1]) /
        (norm(vectors[0]) * norm(vectors[1])))  # 0.5803329846765686


s1 = '你在干嘛呢'
s2 = '你在干什么呢'
jaccard_similarity(s1, s2)
