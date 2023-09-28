#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#


# @lc code=start
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class DLL:
    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, node):
        if self.size == 0:
            node.next = node
            node.prev = node
            self.head = node
        else:
            tail = self.head.prev
            node.next = self.head
            node.prev = tail
            tail.next = node
            self.head.prev = node
        self.size += 1

    def delete(self, node):
        if self.size == 1:
            self.head = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            if node == self.head:
                self.head = self.head.next
        self.size -= 1

    def deleteHead(self):
        if self.size == 0:
            raise Exception("Can't delete head of empty list")
        headNode = self.head
        self.delete(self.head)
        return headNode

    def __repr__(self):
        if self.size == 0:
            return "EMPTY"
        curr = self.head
        res = "(" + str(self.head.key) + ":" + str(self.head.value) + ")"
        curr = curr.next
        while curr.key != self.head.key:
            res += " (" + str(curr.key) + ":" + str(curr.value) + ")"
            curr = curr.next
        return res


# use double linked list
class LRUCache:
    def __init__(self, capacity: int):
        self.key2Node = {}
        self.ll = DLL()
        self.max = capacity

    def get(self, key: int) -> int:
        # if found, delete the node from ll and append it at the end
        if key not in self.key2Node or self.ll.size == 0:
            return -1
        node = self.key2Node[key]
        self.ll.delete(node)
        self.ll.add(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        # 1. already in the list, update value
        if key in self.key2Node:
            newNode = Node(key, value)
            node = self.key2Node[key]
            self.ll.delete(node)
            self.ll.add(newNode)
            self.key2Node[key] = newNode
        # 2. not in the list but still has room
        elif self.ll.size < self.max:
            newNode = Node(key, value)
            self.key2Node[key] = newNode
            self.ll.add(newNode)
        # 3. not in the list but full
        else:
            # delete head
            node = self.ll.deleteHead()
            del self.key2Node[node.key]
            newNode = Node(key, value)
            self.ll.add(newNode)
            self.key2Node[key] = newNode


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
