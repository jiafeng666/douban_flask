import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import numpy as np
import sqlite3


# 提词
con = sqlite3.connect('movie.db')
cur = con.cursor()
sql = 'select introduction from movie250'
data = cur.execute(sql)
text = ""
for item in data:
    text = text + item[0]
    #print(item[0])
#print(text)
cur.close()
con.close()


# 分词并去掉停用词
def stop_words(path):
    with open(path, 'r', encoding='utf-8', errors='ignore')as f:
        content = ''
        for l in f:
            l = l.strip()
            content += l
        return content


path = "D:/pycharm/trainings/myproject/实验&作业/stopwords.txt"
stopwords = [x for x in jieba.cut(stop_words(path))]

text_cut = jieba.cut(text)
text_list = list(text_cut)
list_cut = []
for item in text_list:
    if item not in stopwords and item != " ":
        list_cut.append(item)
#print(list_cut)
text_String = ' '.join(list_cut)
#print(text_String)


# 生成遮罩图片
img = Image.open(r'./static/assets/img/tree.jpg')
img_array = np.array(img)   # 将图片封装成数组
wc = WordCloud(
    background_color='white',
    mask=img_array,
    font_path='msyh.ttc'
).generate_from_text(text_String)


# 绘制图片
fig = plt.figure()
plt.imshow(wc)   #按照词云规则显示
plt.axis('off')  #是否显示坐标轴

#plt.show()     #显示生成的词云图片


# 输出词云图片到文件
plt.savefig(r'./static/assets/img/word.jpg', dpi=500)
