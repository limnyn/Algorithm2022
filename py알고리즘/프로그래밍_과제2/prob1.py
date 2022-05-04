# 1.데이터파일은 단어들이 랜덤한 순서로 배열되어 있는 영어 사전파일이다.
# 각 라인마다 하나의 단어가 저장되어 있으며, 각 단어는 다음과 같이 형식으로 저장되어 있다.

# 단어 (품사) 설명

# 즉, 각 줄의 첫 문자열이 단어이며, 이어서 괄호 안에 그 단어의 품사가 저장되어 있고,
# 이어서 그 단어에 대한 설명이 있다.
# 이 사전 파일을 읽어서 이진검색트리의 각 노등 하나의 단어를 표현하는 객체가 저장되어야 한다.
# Python 프로그램은 다음과 같은 기능을 제공해야 한다.

# (a) 프로그램을 실행하면 suffled_dict.txt 파일에 있는 모든 단어들을 순서대로 이진검색트리에 삽입한다.
# (b)검색할 단어의 리스트가 저장된 파일 search_word.txt를 읽어서 이 파일에 저장된 단어들을 순서대로 모두 이진트리에서 삭제한다.
#       한 번에 하나씩 순서대로 검색해야 한다.
# (c) (b)번을 모두 수행하는데 걸린 시간을 측정하여 출력한다.

import time 

class dword:
# 단어 (품사) 설명
    word = "" #단어
    pos = "" #품사
    expl = "" #설명

    def __init__(self, w, p, e):
        self.word = w
        self.pos = p
        self.expl = e
    



class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class BinarySearchTree(object):
    def __init__(self):
        self.root = None
    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root is not None
    
    def _insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)
        return node
    
    def find(self, key):
        return self._find_value(self.root, key)
    
    def _find_value(self, root, key):
        if root is None or root.data == key:
            return root is not None
        elif key < root.data:
            return self._find_value(root.left, key)
        else:
            return self._find_value(root.right, key)

    def delete(self, key):
        self.root, deleted = self._delete_value(self.root, key)
        return deleted
    
    def _delete_value(self, node, key):
        if node is None:
            return node, False
    
        deleted = False
        if key == node.data:
            deleted = True
            if node.left and node.right:
                # replace the node to the leftmost of node.right
                parent, child = node, node.right
                while child.left is not None:
                    parent, child = child, child.left
                child.left = node.left
                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child
            elif node.left or node.right:
                node = node.left or node.right
            else:
                node = None
        elif key < node.data:
            node.left, deleted = self._delete_value(node.left, key)
        else:
            node.right, deleted = self._delete_value(node.right, key)
        return node, deleted


array = [40, 4, 34, 45, 14, 55, 48, 13, 15, 49, 47]

delist = [4, 14, 55, 48, 15]
bst = BinarySearchTree()
for x in array:
    bst.insert(x)
# # Find
# print(bst.find(15)) # True
# print(bst.find(17)) # False
# # Delete
# print(bst.delete(55)) # True
# print(bst.delete(14)) # True
# print(bst.delete(11)) # False
start_time = time.perf_counter_ns()
for i in delist:
    print(i)
    bst.delete(i)
end_time = time.perf_counter_ns()

print('코드 실행 시간: %20dns' % (end_time - start_time))