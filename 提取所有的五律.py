
path1 = './raw_poems/五绝七绝都有.txt'
with open(path1, 'r', encoding='gbk') as f:
    read = f.readlines()
path2 = './raw_poems/五律.txt'
with open(path2, 'a', encoding='utf-8')as f:
    for i in read:
        if len(i) == 49 and i[5] == '，':
            f.write(i)



