import re

def read_lines(location):
    with open(location, 'r', encoding='utf-8')as f:
        read = f.readlines()#产生一行为字符串的列表
    list = []
    for i in read:
        content = re.findall('\:[\u4e00-\u9fa5\u3002\uff0c]*\。', i)#获取每一首诗的内容，然后从：之后到。 进行截断，输出为列表,其中\u4e00-\u9fa5表示所有汉字，\u3002表示句号，\uff0c表示逗号
        if content == []:#去除空白
            continue
        with open('1poem.txt', 'a', encoding='utf-8')as f:#写入新的txt，a为追加，w会覆盖原来的
            f.write(content[0][1:])
            f.write('\n')

if __name__ == '__main__':
    read_lines('qijue.txt')