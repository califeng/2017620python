#!/usr/bin/python
# coding:utf-8
'''
#coding:utf-8
'''
print "你好"
x = int(raw_input("请输入一个整数："))
if x < 0:
    x = 0
    print 'Negative changed to zero'
elif x == 0:
    print 'zero'
elif x == 1:
    print 'Single'
else:
    print 'More'
