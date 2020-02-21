#encoding=utf-8
from gensim import corpora,models,similarities,utils
import jieba
import re

etlre = re.compile(r"[^\u4e00-\u9f5aa-zA-Z0-9]")
#去除无用空格
def etl(content):
    content = etlre.sub('',content)
    return content

train_set=[]
f=open("all.info",encoding ='utf-8')
lines=f.readlines()
for line in lines:
    content = (line.lower()).split("\t")[1] + (line.lower()).split("\t")[0]
    #去无用空格，cut_all表示非全切分
    word_list = filter(lambda x: len(x)>0,map(etl,jieba.cut(content,cut_all=False)))
    train_set.append(word_list)

f.close()
print(train_set)
#生成字典
dictionary = corpora.Dictionary(train_set)

#去除极低频的杂质词
dictionary.filter_extremes(no_below=1,no_above=1,keep_n=None)
print(dictionary)
#将词典保存下来，方便后续使用
dictionary.save("all.dic")

corpus = [dictionary.doc2bow(text) for text in train_set]
print(corpus)
#使用数字语料生成TFIDF模型
tfidfModel = models.TfidfModel(corpus)
#存储tfidfModel
tfidfModel.save("allTFIDF.mdl")

#把全部语料向量化成TFIDF模式
tfidfVectors = tfidfModel[corpus]
#建立索引
indexTfidf = similarities.MatrixSimilarity(tfidfVectors)
indexTfidf.save("allTFIDF.idx")

#通过TFIDF向量生成LDA模型，id2word表示编号的对应词典，num_topics表示主题数。
lda = models.LdaModel(tfidfVectors, id2word=dictionary, num_topics=400)
#把模型保存下来
lda.save("allLDA.mdl")
#把所有TFIDF向量变成LDA的向量
corpus_lda = lda[tfidfVectors]
#建立索引，把LDA数据保存下来
indexLDA = similarities.MatrixSimilarity(corpus_lda)
indexLDA.save("allLDA.idx")