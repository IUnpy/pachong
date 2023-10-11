import json
from py2neo import Node, Relationship, Graph, NodeMatcher
import time
import csv
import pandas as pd

print('正在连接Neo4j')
g = Graph('http://localhost:7474', user='neo4j', password='123456')
matcher = NodeMatcher(g)
print('连接成功')


# 创建函数，用来创建关系
def create_rel(node1, node2, _graph, rel):
    relation = Relationship(node1, rel, node2)
    _graph.create(relation)


# 首先将每节课都放到图数据库中，并且学段、年级等作为属性导入
with open(r"D:\桌面\data.csv", 'r', encoding='utf-8') as m:
    reader = csv.reader(m)
    skip = 0
    for row in reader:
        if skip == 0:
            skip = 1
            continue
        xueduan, nianji, xueke, banben, ceci, danyuan, wenzhang = row
        node = Node('文章')
        node['学段'] = xueduan
        node['年级'] = nianji
        node['学科'] = xueke
        node['版本'] = banben
        node['册次'] = ceci
        node['单元'] = danyuan
        node['文章'] = wenzhang
        # g.create(node)

lis_xd = []
lis_nj = []
lis_xk = []
lis_bb = []
lis_cc = []
lis_dy = []
with open(r"D:\桌面\data.csv", 'r', encoding='utf-8') as m:
    reader = csv.reader(m)
    skip = 0
    for row in reader:
        if skip == 0:
            skip = 1
            continue
        xueduan, nianji, xueke, banben, ceci, danyuan, wenzhang = row
        if xueduan not in lis_xd:
            lis_xd.append(xueduan)
        if nianji not in lis_nj:
            lis_nj.append(nianji)
        if xueke not in lis_xk:
            lis_xk.append(xueke)
        if banben not in lis_bb:
            lis_bb.append(banben)
        if ceci not in lis_cc:
            lis_cc.append(ceci)
        if danyuan not in lis_dy:
            lis_dy.append(danyuan)
    print(len(lis_xd))
    print(len(lis_nj))
    print(len(lis_xk))
    print(len(lis_bb))
    print(len(lis_cc))
    print(len(lis_dy))

for i in lis_xd:
    node = Node('学段')
    node['学段'] = i
    # g.create(node)

for i in lis_nj:
    node = Node('年级')
    node['年级'] = i
    # g.create(node)

for i in lis_xk:
    node = Node('学科')
    node['学科'] = i
    # g.create(node)

for i in lis_bb:
    node = Node('版本')
    node['版本'] = i
    # g.create(node)

for i in lis_cc:
    node = Node('册次')
    node['册次'] = i
    # g.create(node)

for i in lis_dy:
    node = Node('单元')
    node['单元'] = i
    # g.create(node)
count = 0
i = 0
with open(r"D:\桌面\data.csv", 'r', encoding='utf-8') as m:
    reader = csv.reader(m)
    skip = 0
    for row in reader:
        if skip == 0:
            skip = 1
            continue
        xueduan, nianji, xueke, banben, ceci, danyuan, wenzhang = row
        xueduan = str(xueduan)
        nianji = str(nianji)

        xd = matcher.match('学段', 学段=xueduan).first()
        nj = matcher.match('年级', 年级=nianji).first()
        xk = matcher.match('学科', 学科=xueke).first()
        bb = matcher.match('版本', 版本=banben).first()
        cc = matcher.match('册次', 册次=ceci).first()
        dy = matcher.match('单元', 单元=danyuan).first()
        wz = matcher.match('文章', 文章=wenzhang).first()

        if xueduan and nianji:
            # create_rel(xd, nj, g, '该学段有')
            print('WORKED')
            count+=1

        if nj and xk:
            # create_rel(nj, xk, g, '该年级有')
            count+=1
        if xk and bb:
            # create_rel(xk, bb, g, '该学科有')
            count+=1
        if bb and cc:
            # create_rel(bb, cc, g, '该版本有')
            count+=1
        if cc and dy:
            # create_rel(cc, dy, g, '该册次有')
            count+=1
        if dy and wz:
            # create_rel(dy, wz, g, '该单元有')
            count+=1
        x = i / 12582
        x = x * 100
        i = i + 1
        print('已完成' + str(x) + '%')

print(count)