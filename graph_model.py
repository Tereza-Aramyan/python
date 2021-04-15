'''
Simple graph model, that does not have multiple edges and loops and graph is undirected
'''


class Node:
    def __init__(self, node):
        self.node = node

class Graph:
    def __init__(self):
        self.edge = {}
        self.vertex = {}
        self.neighbours = {}

    def add_vertex(self, i):
        if(i not in self.vertex.keys()):
            new_vertex = Node(i)
            self.vertex[i] = new_vertex
            return new_vertex

    def delete_vertex(self, i):
        del self.vertex[i]

        for el in self.edge:
            if i in el:
                del self.edge[el]
                break

        del self.neighbours[i]
        for key in self.neighbours:
            if i in self.neighbours[key]:
                self.neighbours[key].remove(i)

    def add_edge(self, i, j, weight=0):
        self.add_neighbor(i,j)
        self.add_neighbor(j,i)

        if i not in self.vertex:
            self.add_vertex(i)

        if j not in self.vertex:
            self.add_vertex(j)
        self.edge[(i,j)] = weight


    def add_neighbor(self, node1, node2):
        if node1 not in self.neighbours:
            self.neighbours[node1] = {node2}
        else:
            self.neighbours[node1].add(node2)


    def get_nods(self):
        return f'Vertices = {[*self.vertex]}'

    def get_edges(self):
        return f'Edges = {self.edge}'

    def get_neighbour(self):
        return f'Neighbours = {self.neighbours}'

    def __contains__(self, other):
        flag = True
        for el in [*other.vertex]:
            if el not in [*self.vertex]:
                return False

        if ((len([*other.edge]) == 0 & len([*self.edge]) == 0)):
            return True
        elif((len([*other.edge]) >= 0 & len([*self.edge]) == 0)):
            return False
        else:
            for el in [*other.edge]:
                if el not in [*self.edge]:
                    print('dfdfd')
                    return False

        return flag


if __name__ == '__main__':
    graph = Graph()
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)

    graph.add_edge(1,2,2)
    graph.add_edge(3,1,4)

    print(graph.get_nods())
    print(graph.get_edges())
    print(graph.get_neighbour())

    print('>>>>>>>>>>>>>>>>>>>>contains>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    graph2 = Graph()
    graph2.add_vertex(1)
    graph2.add_vertex(2)
    graph2.add_vertex(3)

    graph2.add_edge(3,2,2)

    print(graph.__contains__(graph2))
    print(graph2.get_nods())
    print(graph2.get_edges())
    print(graph2.get_neighbour())

    print('>>>>>>>>>>>>>>>>>>>>deleting node>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    graph.delete_vertex(2)

    print(graph.get_nods())
    print(graph.get_edges())
    print(graph.get_neighbour())



