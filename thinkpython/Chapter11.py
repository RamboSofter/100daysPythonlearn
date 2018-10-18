#给定一个字符串，计算每个字母出现的次数
def histogram(s):
    d=dict()
    for c in s:
        if c not in d:
            d[c]=1
        else:
            d[c]+=1
    return d
def get(x,y):
    if x in h:
        return x
    else:
        return y

m=histogram('a')
m.get('b',0)

#打印字典的每一个键及对应的值
def print_hist(h):
    for c in h:
        print(c,h[c])
