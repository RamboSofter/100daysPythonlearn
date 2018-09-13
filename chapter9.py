#读入words.txt并且打印处那些长度超过20个字符的单词
def print20():
    fin=open('E:\PythonTest\words.txt')
    line=fin.readline()
    for line in fin:
        if len(line)>21:
            word=line.strip()
            print(word)
#写一个函数has_no_e,给定单词不包含字母e时返回True
def has_no_e(word):
    if word.find('e')==-1:
        return True
    else:
        return False
#打印出不含‘e’的单词，并计算这种单词在整个单词表中的百分比
def print_no_e():
    fin=open('E:\PythonTest\words.txt')
    line=fin.readline()
    count=0
    sum=0
    for line in fin:
        if has_no_e(line)==True:
            word=line.strip()
            print(word)
            count=count+1
            sum=sum+1
        else:
            sum=sum+1
    bf=count/sum
    print(bf)
    
#编写一个avoids待修改：
def avoids(word,x):
    count=0
    for s in x:
        if word.find(s)==-1:
            count=count+1
    if count==0:
        return True    
    else:
        return False
def print_no():
    fin=open('E:\PythonTest\words.txt')
    line=fin.readline()
    count=0
    sum=0
    str=input('请输入禁止字符串：')
    
    for line in fin:
        if avoids(line,str)==False:
            word=line.strip()
            print(word)
            count=count+1
            sum=sum+1
        else:
            sum=sum+1
    bf=count/sum
    print(bf)
