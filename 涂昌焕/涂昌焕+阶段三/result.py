#encoding=utf-8

from gensim import corpora,models,similarities,utils
import jieba
import sys
import pickle
import logging
import re


logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.INFO)

sys.setdefaultencoding('utf-8')

#

etlre = re.compile(r"[^\u4e00-\u9f5aa-zA-Z0-9]")
def etl(content):
    content = etlre.sub('',content)
    return content

#加载函数
def loadObject(filename):
    f=open(filename,'r')
    obj=pickle.load(f)
    return obj

#载入论文信息
docinfos = loadObject("all.info")
#载入query中生成的字典
dictionary = corpora.Dictionary.load("all.dic")


#载入query中生成的tfidf模型索引
tfidfModel = models.TfidfModel.load("allTFIDF.mdl")
indexTfidf = similarities.MatrixSimilarity.load("allTFIDF.idx")

#载入query中生成的LDA模型索引
ldaModel = models.LdaModel.load("allLDA.mdl")
indexLDA = similarities.MatrixSimilarity.load("allLDA.idx")


query= """
随着智能手机的普及,已研究出多种基于WiFi和移动智能终端的室内定位技术。与前期定位
技术相比,基于智能手机和WiFi进行室内定位具有明显优势。从室内定位规模化应用的关键
因素着手,分析总结了基于智能手机和WiFi的室内定位的基本方法,并对基于WiFi和移动智
能终端定位中有待研究的难点和未来可能的研究方向进行展望。
"""
query_bow = dictionary.doc2bow(filter(lambda x: len(x)>0,map(etl,jieba.cut(query,cut_all=False))))

#测试tfidf效果
tfidfvect = tfidfModel[query_bow]
simstfidf = indexTfidf[tfidfvect]
sort_sims = sorted(enumerate(simstfidf), key=lambda item: -item[1])
print ("TFIDF Top 10:::")
for sim in sort_sims[:10]:
    print ( docinfos[sim[0]]["title"] + "\tsimilary:::" + str(sim[1]))

#测试Lda效果
ldavec = ldaModel[tfidfvect]
simlda = indexLDA[ldavec]
sort_sims = sorted(enumerate(simlda), key=lambda item: -item[1])
print ("LDA Top 10:::")
for sim in sort_sims[:10]:
    print (docinfos[sim[0]]["title"] + "\tsimilary:::" + str(sim[1]))

