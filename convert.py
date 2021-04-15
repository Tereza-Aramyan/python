'''
json-xml manual converter
'''
import json as j

a = {
    "id": "0001",
    "type": "donut",
    "name": "Cake",
    "ppu": 0.55,
    "batters":
        {
            "batter":
                [
                    { "id": "1001", "type": "Regular" },
                    { "id": "1002", "type": "Chocolate" },
                    { "id": "1003", "type": "Blueberry" },
                    { "id": "1004", "type": "Devil's Food"}
                ]
        },
    "topping":
        [
            { "id": "5001", "type": "None" , "boob" : {"boob1": 1, "boob2": 2} },
            { "id": "5002", "type": "Glazed" },
            { "id": "5005", "type": "Sugar" },
            { "id": "5007", "type": "Powdered Sugar" },
            { "id": "5006", "type": "Chocolate with Sprinkles" },
            { "id": "5003", "type": "Chocolate" },
            { "id": "5004", "type": "Maple" }
        ]
}


class Tree():
    def __init__(self,root):
        self.data     = None
        self.value    = None
        self.root     = root
        self.children = []
        self.Nodes    = []

    def addNode(self,obj):
        self.children.append(obj)

    def getAllNodes(self):
        self.Nodes.append(self.root)

        for child in self.children:
            self.Nodes.append(child.data)

        for child in self.children:
            if child.getChildNodes(self.Nodes) != None:
                child.getChildNodes(self.Nodes)

        print(*self.Nodes, sep = "\n")
        print('Tree Size:' + str(len(self.Nodes)))

    def Tree2XML(self):
        xml_list = []
        for child in self.children:
            xml_list.append("<{}>".format(child.data))
            if child.value:
                xml_list.append(child.value)
            else:
                child.CTree2XML(xml_list)

            xml_list.append("</{}>".format(child.data))

        return xml_list



class Node():
    def __init__(self,data,value):
        self.data     = data
        self.value    = value
        self.children = []

    def addNode(self, obj):
        self.children.append(obj)

    def CTree2XML(self ,xml_list):
        for child in self.children:
            xml_list.append("<{}>".format(child.data))
            if child.children:
                child.CTree2XML(xml_list)
            else:
                xml_list.append(child.value)
            xml_list.append("</{}>".format(child.data))

    def getChildNodes(self,Tree):
        for child in self.children:
            if child.children:
                child.getChildNodes(Tree)
                Tree.append(child.data)
            else:
                Tree.append(child.data)


def JSON2graph(json_dict, json_tree):
    for item in json_dict:
        if isinstance(json_dict[item], dict):
            ## --------
            node = Node(item, None)
            json_tree.addNode(node)
            ## --------
            JSON2graph(json_dict[item], node)

        elif isinstance(json_dict[item], list):
            # creat a Node for a list
            node_1 = Node(item, None)
            json_tree.addNode(node_1)
            list_item = 0
            for k in json_dict[item]:
                if isinstance(k, dict):
                    JSON2graph(k,node_1)
                else:
                    json_tree.addNode(node_1)
                list_item += 1
        else:
            node = Node(item, json_dict[item])
            json_tree.addNode(node)



xml_version = "xml<?xml version=\"1.0\"?>"



json_tree = Tree('Root')

JSON2graph(a, json_tree)
print(json_tree.children[4].children[0].children[0].data)
json_tree.getAllNodes()
#
f = open(r'C:\visio_drawings\test.xml', "w")

for i in  json_tree.Tree2XML():
    f.write(str(i))
f.close()