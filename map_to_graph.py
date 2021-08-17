import numpy as np

from Dijkstra import *
from excel_to_map import *

class Read_map(object):
    def __init__(self, map):
        self.map = map
        self.node_num = len(map)

    def node_name(self):               # labels为节点名称
        labels = []
        for i in range(0,self.node_num):
            labels.append(str(self.map[i]))
        return labels

    def map_nodegraph(self):
        graph = np.zeros(shape=(self.node_num,self.node_num))
        for i in range(0,self.node_num):
            for j in range(0,self.node_num):
                if i==j:
                    graph[i][j] = 0
                else:
                    pos_i = np.array(self.map[i])
                    pos_j = np.array(self.map[j])
                    x_pos_i = pos_i[0]
                    y_pos_i = pos_i[1]
                    x_pos_j = pos_j[0]
                    y_pos_j = pos_j[1]
                    if (abs(x_pos_i-x_pos_j)==0 and abs(y_pos_j-y_pos_i)==1) or \
                            (abs(x_pos_i-x_pos_j)==1 and abs(y_pos_j-y_pos_i)==0):
                        graph[i][j] = 1
                    else:
                        graph[i][j] = float('inf')
        return graph


class Calculation(Read_map):
    def __init__(self):
        pass
    def calculation_2point(self, start, endnode, map_name):
        book1 = Read_Excel(map_name, 'map')
        map = book1.excel_map()[0]
        graph = Read_map(map)
        nodegraph = graph.map_nodegraph()  # 节点二维数组
        labels = graph.node_name()  # 节点名称：节点坐标的字符形式
        G = Graph(nodegraph, labels)
        dist, path = Dijkstra(G, G.labels.index(start), G.labels.index(endnode))
        Path = []
        Path1 = []
        for i in range(len(path)):
            Path.append(G.labels[path[len(path) - 1 - i]])  # Path为最短路径（列表格式，列表元素为字符串）
        for point in Path:
            Path1.append(map[labels.index(point)])          # Path1为最短路径（列表格式，列表元素为列表）
        return Path1, dist

    def calculation_3point(self, start, middle, end, map_name):
        path1, dist1 = self.calculation_2point(start, middle, map_name)
        path2, dist2 = self.calculation_2point(middle, end, map_name)
        path1.pop()                   # 删除path1中的最后一个元素
        path1.extend(path2)
        dist = dist1 + dist2
        return path1, dist-1



