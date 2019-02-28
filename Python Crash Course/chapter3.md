#列表是什么？
用[]表示列表，用逗号分割其中的元素。索引从0开始。
修改cycle[0]='ssd'
添加cycle.append('add')
插入元素cycle.insert(0,'diyi')
删除元素 del cycle[0]
使用pop()删除元素：popped_cyc=cycle.pop()，被弹出的元素不在列表中；
使用pop()可以实现打印最后一条消息
如果要从列表中删除一个元素，且不再以任何方式使用它，就使用del语句；如果要在删除元素后还能继续使用，就用pop（）方法；
根据值删除元素：cycle.remove('add') remove()只删除第一个指定的值。如果要删除的值可能在列表中出现多次，就需要使用循环
