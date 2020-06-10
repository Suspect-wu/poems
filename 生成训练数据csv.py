import re
import csv

with open('简体_poem.txt', 'r', encoding='utf-8')as f:
    poems = f.readlines()
poem = []
for i in poems:
    i = re.sub('，|。', ';', i)
    poem.append(i.strip('\n').strip(';'))
head = []
tail = []
for i in poem:
    seq = i.split(';')
    if len(seq) != 4:
        continue
    head.append(seq[0])
    tail.append(seq[1])
    head.append(seq[0]+';'+seq[1])
    tail.append(seq[2])
    head.append(seq[0]+';'+seq[1]+';'+seq[2])
    tail.append(seq[3])
for i in range(len(head)):
    with open('head_tail.csv', 'a', encoding='utf-8', newline='')as f:
        writer = csv.writer(f)
        writer.writerow([head[i], tail[i]])




