class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        # Solution 1 - All duplicate elements are always removed.
        queue = [head] if head else []

        result_head = None
        result_list = Solution()
        result = []

        while queue:
            node = queue.pop()

            if node.data not in result:
                result.append(node.data)
                result_head = result_list.insert(result_head, node.data)

            if node.next:
                queue.insert(0, node.next)

        return result_head

        # # Solution 2 - The duplicate element corresponding to the constraint is removed.
        # if head == None or head.next == None:
        #     return head
        
        # if head.data == head.next.data:
        #     head.next = head.next.next
        #     self.removeDuplicates(head)
        # else:
        #     self.removeDuplicates(head.next)
        
        # return head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
head=mylist.removeDuplicates(head)
mylist.display(head)