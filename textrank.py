import jieba
from jieba import analyse
import jieba.posseg as pseg
path = r'C:\Users\Suspect.X\PycharmProjects\study\py\writepoems\raw_poems\五律.txt'
with open(path, 'r', encoding='utf-8')as f:
    read = f.readlines()
a = ''.join(read[:100])

b = jieba.analyse.textrank(a, topK=2000, allowPOS= ('un', 'ns', 'n', 'vn', 'v','ag', 'a', 'ad','an','b','c','dg','d','e','f','g','h','i','j','k','l','m','ng','n'
                                                 ,'nr','ns','nt','nz','o','p','q','r','s','tg','t','u','vg','v','vd','vn','y','z','un'), withWeight=True)
c = jieba.lcut(a)
print(pseg.lcut(a))

print(c)
print(len(b))
dict = {}
print(b)

for i in range(len(b)):
    dict[b[i][0]] = b[i][1]
if a[0] not in dict or a[1] not in dict:
    print('error')
print(dict)