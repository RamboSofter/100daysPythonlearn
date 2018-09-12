#修改find函数，index表示从word的哪个下标开始搜素
def find(word,letter,index):
    while index<len(word):
         if word[index]==letter:
              return index
         index=index +1
    return -1

#count函数，接收字符串和要计数的字母作为形参
def count(word,zf):
    count=0
    for letter in word:
        if letter == zf:
             count=count+1
    print count
    
#重写count函数，使用find函数
def count_1(word,zf):
    count=0
    index=0
    for zf in word:
         if find(word,zf,index)!=-1:
              count=count+1
              index=index+1
    print count
