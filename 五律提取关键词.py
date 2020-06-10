import jieba
import re
from jieba import analyse
import csv

path = './raw_poems/五律.txt'
with open(path, 'r', encoding='utf-8')as f:
    read = f.readlines()

count = 0
head = []
tail = []
for line in read:
    line = re.sub('。', '，', line)
    line = line[:-2].split('，')
    key_list = []
    flag = False
    for i in range(len(line)):
        key_word = analyse.extract_tags(line[i], allowPOS=('n','nr','ns'))
        if key_word == []:
            key_word = analyse.extract_tags(line[i])
        if key_word == []:
            flag = True
            break
        key_list.append(key_word[0])
    if flag:
        continue
    count += 1
    print(count)
    poem = ''
    for i in range(8):
        head.append(key_list[i] + ';' + poem)
        tail.append(line[i])
        if i == 0:
            poem = line[i]
        else:
            poem = poem + ';' + line[i]


for i in range(len(head)):
    with open('processed_poems/五律.csv', 'a', encoding='utf-8', newline='')as f:
        writer = csv.writer(f)
        writer.writerow([head[i], tail[i]])
