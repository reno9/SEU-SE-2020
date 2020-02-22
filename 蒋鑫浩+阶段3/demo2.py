import jieba
import re
import pandas
from gensim import corpora, models, similarities
import heapq

# 导入数据集
paperdata = pandas.read_csv('abstract.tsv', sep='\t', names=['name', 'content'])
zhPattern = re.compile(u'[\u4e00-\u9fa5]+')

# 打开停词表
with open('stopletters.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    textlist = text.split(';\n')
    stopwords = set(textlist)

paperlist = []
papername = []

# 将数据集进行分词，保存
for index, row in paperdata.iterrows():
    traindata = {'content': ''}
    traindata['content'] = [word for word in jieba.cut(row['content']) if word not in stopwords]
    paperlist.append(traindata['content'])
    papername.append(row['name'])
    if index == 1000:
        break

# 用户输入内容
paper_input = input("请输入你要查询的论文内容:")
paper_read = [word for word in jieba.cut(paper_input) if word not in stopwords]

# 将数据进行相似度计算
dictionary = corpora.Dictionary(paperlist)
corpus = [dictionary.doc2bow(stu) for stu in paperlist]
tfIdf_model = models.TfidfModel(corpus)
corpus = [dictionary.doc2bow(book) for book in paperlist]
read_bow = dictionary.doc2bow(paper_read)
index = similarities.SparseMatrixSimilarity(tfIdf_model[corpus], num_features=len(dictionary.keys()))
sim = index[tfIdf_model[read_bow]]
simarr = sim.tolist()

# 查出相似度最高的十个数据，并且找出其对应的下标
re2 = map(simarr.index, heapq.nlargest(10, simarr))

# 输出相似度最高的十个论文
print("推荐的论文有：")
for index, num in enumerate(list(re2)):
    print(index + 1, '：', papername[num])
