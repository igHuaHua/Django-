# class Solution:
#     def Print1ToMaxOfNDigits(self, n):
#         if n <= 0:
#             return
#         number = ['0'] * n  # 用数组来表示[‘0’，‘0’~~]
#         for i in range(10):
#             number[0] = str(i)  # 依次取0-9的值，第一位
#             self.Print1ToMaxOfNDigitsRecursively(number, n, 0)  # 第一次调用递归函数
#
#     def PrintNumber(self, number):  # 输出数字
#         # 此处的number为一个str类型的数组，每个数组元素是一个0-9之间数字的字符串形式
#         isBeginning0 = True
#         nLength = len(number)
#         for i in range(nLength):
#             if isBeginning0 and number[i] != '0':  # 只输出非零项
#                 isBeginning0 = False
#             if not isBeginning0:
#                 print('%c' % number[i],end='')
#                 import time
#                 time.sleep(2)
#         print('\t')
#
#     def Print1ToMaxOfNDigitsRecursively(self, number, length, index):  # index表示变换位数
#         if index == length - 1:  # 最后一位
#             self.PrintNumber(number)
#             return
#         for i in range(10):
#             number[index + 1] = str(i)  # 改变下一位
#             self.Print1ToMaxOfNDigitsRecursively(number, length, index + 1)  # 递归调用


# if __name__=="__main__":
#     Solution().Print1ToMaxOfNDigits(2)

#
# class Lnode():
#     def __init__(self,num,next_=None):
#         self.num = num
#         self.next = next_
#
# class Solution:
#     @classmethod
#     def del_node(self,head,node):
#         if head == node:
#             del head
#             return 'head die'
#         if node.next == None:
#             while head:
#                 if head.next == node:
#                     head.next = None
#                 head = head.next
#         else:
#             node.num = node.next.num
#             node.next = node.next.next
# n1 = Lnode(1)
# # b = Lnode(2)
# # n1.next = b
# # n1.next.next=Lnode(3)
# a = Solution.del_node(n1,n1)
# print(a)


# class Lnode():
#     def __init__(self,num,next_=None):
#         self.num = num
#         self.next = next_
#
#
# class Solution:
#     @classmethod
#     def del_node(self,LList):
#         self.head = LList
#         if self.head.next == None:
#             return LList.num
#         pre = self.head
#         nx = self.head.next
#         while nx.next != None:
#             if nx.num != nx.next.num:
#                 pre = nx
#
#             else:
#
#
#                 while nx!=None and nx.num != nx.next.num:
#                     pre.next = nx.next
#                     pre = nx.next
#                     nx = pre.next
#             nx = nx.next
#             pre.next = None
#
#
# n1 = Lnode(1)
# b = Lnode(2)
# n1.next = b
# n1.next.next = Lnode(3)
# n1.next.next.next=Lnode(3)
# n1.next.next.next.next=Lnode(4)
# a = Solution.del_node(n1)
# while n1:
#     print(n1.num)
#     n1 = n1.next

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# class Solution:
#     @classmethod
#     def deleteDuplication(self, pHead):
#         # 第一步先检测一下是不是空的或者是不是只有一个
#         if pHead is None or pHead.next is None:
#             return pHead
#         # 第二步因为防止第一个就是重复的节点，所以创作一个新的头节点。
#         first = ListNode(-1)
#         # 因为需要两个指针，一个指着重复结点上一个结点，一个指着重复结点后一个值。
#         first.next = pHead
#         last = first
#         while pHead and pHead.next:
#             if pHead.val == pHead.next.val:
#                 val = pHead.val
#                 while pHead and val == pHead.val:
#                     pHead = pHead.next
#                 last.next = pHead
#             else:
#                 last = pHead
#                 pHead = pHead.next
#         return first.next


# n1 = ListNode(1)
# n1.next = ListNode(2)
# n1.next.next = ListNode(3)
# n1.next.next.next = ListNode(3)
# n1.next.next.next.next = ListNode(4)
# Solution.deleteDuplication(n1)
# while n1:
#     print(n1.val)
#     n1 = n1.next

# def solution(arr):
#     i = 0
#     j = len(arr) - 1
#     while i!=j:
#         if arr[i]%2!=0 and arr[j]%2==0:
#             i += 1
#             j -= 1
#         elif arr[i]%2==0 and arr[j]%2!=0:
#             arr[i], arr[j] = arr[j], arr[i]
#             i += 1
#             j -= 1
#         elif arr[i]%2!=0 and arr[j]%2!=0:
#             i += 1
#         else:
#             i += 1
#     print(arr)
# a = solution([1,2,4,3,7,9,3,6])





# def g():
#     print('a')
#
# class Student():
#     def __init__(self,f):
#         self.name = f
#     __a = 2
#     __slots__ = ('name')
# s = Student(1)
# print(Student.__dict__)


class Lnode:
    def __init__(self,val,next_=None):
        self.val = val
        self.next = next_

#
# def solution(node,k):
#     if k == 0:
#         return False
#     if not node.val:
#         return False
#
#     count = 1
#     check = node
#     while node.next is not None:
#         node = node.next
#         count += 1
#         if count > k:
#             check = check.next
#     if count < k:
#         return False
#     return check.val
#
#
def s(n,k):

    hh = n
    oo = k
    while n.next and k.next:
        if n.val > k.val:
            temp = k.next
            k.next = n
            k = temp
        if n.val < k.val:
            temp = n.next
            n.next = k
            n = temp
    return hh



if __name__ == '__main__':
    p = Lnode(1)
    p.next = Lnode(8)
    p.next.next = Lnode(44)
    p.next.next.next = Lnode(55)
    p.next.next.next.next = Lnode(66)
    p.next.next.next.next.next = Lnode(400)
    q = Lnode(2)
    q.next = Lnode(5)
    q.next.next = Lnode(9)
    q.next.next.next = Lnode(200)
    q.next.next.next.next = Lnode(255)
    q.next.next.next.next.next = Lnode(300)
    a = s(p,q)
    while a:
        print(a.val)
        a = a.next
    # while q:
    #     print(q.val)
    #     q = q.next






