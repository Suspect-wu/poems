
import opencc

with open('1poem.txt', 'r', encoding='utf-8')as f:
    poem = f.readlines()
poem_list = []
cc = opencc.OpenCC('t2s')
for i in poem:
    poem_line = cc.convert(i)
    with open('简体_poem.txt', 'a', encoding='utf-8')as f:
        f.write(poem_line)


