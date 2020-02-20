import csv
import gensim
import jieba

# 加载数据集
title = []
abstract = []

# 打开文件
with open('abstract_cs_full.tsv', 'r', encoding='utf8') as fd:
    # 创建csv读取器
    text = fd.readlines()
    # 循环得到数据特征与标签（一条邮件）
for item in text:
    item = item.split('\t')
    title.append(item[0])
    abstract.append(item[1].replace('\n', ''))
print('数据读取完毕！')

processed_data = []
# 文本预处理（禁用词，单词长度过滤，大小写统一，词干处理）
for a_abstract in abstract:
    # 禁用词
    stop_words = ['基于', '模型', '实验', '结果', '表明', '时', '具有', '算法', '是', '了', '的', '得', '地', '但', ',', '.', '(', ')', '+', '-', '。', ',', '/', ';']   # 停用词列表
    seg_list = jieba.cut(a_abstract)
    seg_list = [word for word in seg_list if word not in stop_words]
    processed_data.append(seg_list)
number = len(processed_data)
print('数据预处理完毕！')

# 转换为BoW模型
# 构造词袋字典
dict_data = gensim.corpora.dictionary.Dictionary(processed_data)
# 使用词袋字典来构造词袋
corpus_data = [dict_data.doc2bow(text) for text in processed_data]   # 一个句子（单词列表）转换为一个词袋（上面字典的索引与计数）
#构建木星
lsi = gensim.models.LsiModel(corpus_data, id2word=dict_data, num_topics=100)
lsi.save("./model.lsi")
lsi = gensim.models.LsiModel.load("./model.lsi")
index = gensim.similarities.MatrixSimilarity(lsi[corpus_data])

#查询过程
consult_number = input("请输入论文编号（0~{}）：".format(number-1))
rec_number = int(consult_number)

vec_lsi = lsi[corpus_data[rec_number]]
sims = index[vec_lsi]
sims = sorted(enumerate(sims), key=lambda item: -item[1])
sims = sims[1:11]
print("\n查询的论文题目为:", title[rec_number])
print("该论文的摘要是:", abstract[rec_number])
print("\n与该论文相关度最高的十篇论文是：")
for i, s in enumerate(sims):
    print(i+1, ":", title[s[0]])




