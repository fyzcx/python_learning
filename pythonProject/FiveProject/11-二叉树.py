class Node:
    """节点类"""

    def __init__(self, elem=-1, lchild=None, rchild=None):  # 左右孩子默认为空，不用传参
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class Tree:
    def __init__(self):
        self.root = None  # 树根
        self.queue = []  # 辅助队列

    def add_node(self, elem):
        new_node: Node = Node(elem)
        self.queue.append(new_node)  # 进队列
        # 判断树根是否为None
        if self.root is None:
            self.root = new_node
        else:
            if self.queue[0].lchild is None:  # 父亲的左孩子为空，新结点就作为左孩子
                self.queue[0].lchild = new_node
            else:
                self.queue[0].rchild = new_node  # 父亲的右孩子为空，新结点就作为右孩子
                self.queue.pop(0)  # 出队

    def pre_order(self, current_node: Node):
        if current_node:
            print(current_node.elem, end=' ')
            self.pre_order(current_node.lchild)  # 遍历左子树
            self.pre_order(current_node.rchild)  # 遍历右子树


if __name__ == '__main__':
    tree = Tree()
    for i in range(1, 11):
        tree.add_node(i)
    tree.pre_order(tree.root)
