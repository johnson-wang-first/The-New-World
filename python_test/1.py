class ListNode:
    def __init__(self, value=0, next=None):
        self.val = value
        self.next = next
 
# 创建链表
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
print(node1.val)
print(node1.next)
print(node2.val)
print(node2.next)
print(node3.val)
print(node3.next)

node1.next = node2
print(111111)
print(node1.val)
print(node1.next.val)

node2.next = node3
 
# 遍历链表
current = node1
while current is not None:
    print(current.val)
    current = current.next
