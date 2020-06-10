import jieba.analyse
import re
import csv

with open('简体_poem.txt', 'r', encoding='utf-8')as f:
    lines = f.readlines()
    print(lines)

poem = []
head = []
tail = []
count = 0
for i in lines:
    seq = re.sub('，|。', ';', i)
    seq = seq.strip('\n').strip(';')
    seq = seq.split(';')
    if len(seq) != 4:
        continue
    topics = []
    for line in seq:
        topic = jieba.analyse.textrank(line, topK=1, allowPOS=('n'))
        topics.append(topic)
    count += 1
    print(count)
    if [] in topics:
        continue
    head.append(topics[0][0] + ',')
    tail.append(seq[0])
    head.append(topics[1][0] + ',' + seq[0])
    tail.append(seq[1])
    head.append(topics[2][0] + ',' + seq[0] + ';' + seq[1])
    tail.append(seq[2])
    head.append(topics[3][0] + ',' + seq[0] + ';' + seq[1] + ';' + seq[2])
    tail.append(seq[3])
for i in range(len(head)):
    with open('textrank_topic_head_tail.csv', 'a', encoding='utf-8', newline='')as f:
        writer = csv.writer(f)
        writer.writerow([head[i].strip('"'), tail[i]])
print('666')

