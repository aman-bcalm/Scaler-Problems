 # Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None






class Solution:
    # @param A : list of list of integers
    # @return the head node in the linked list
    def solve(self, A):

        head = None
        size_of_list =  0

        for i in range(0, len(A)):
           

            #Add a node of value x before the first element of the linked list.
            if A[i][0] == 0 and A[i][2] == -1:
                temp = ListNode(A[i][1])
                temp.next = head
                head = temp
                size_of_list += 1

            #Append a node of value x to the last element of the linked list
            elif A[i][0] == 1 and A[i][2] == -1:
                temp = ListNode(A[i][1])

                if head == None:
                    head = temp
                else :
                    curr = head
                    pos = 0
                    while pos < size_of_list - 1:
                        curr = curr.next
                        pos += 1

                    #while(curr.next is not None):
                    #    curr = curr.next
                    
                
                    curr.next = temp
                size_of_list += 1

            # Delete the indexth node in the linked list, if the index is valid.
            # 0 based index
            elif A[i][0] == 3 and A[i][2] == -1:
                id = A[i][1]
                if id >= 0 and id <= size_of_list-1 :

                    if id == 0:
                        head = head.next
                    else:
                        prev = head
                        i = 0
                        while i < id-1:
                            prev = prev.next
                            i += 1
                        prev.next = prev.next.next
                    
                    size_of_list -= 1
            
            #Add a node of value x before the indexth node in the linked list. If index equals to the 
            # length of linked list, the node will be appended to the end of linked list. If index is 
            # greater than the length, the node will not be inserted.
            elif A[i][0] == 2:
                id = A[i][2]
               

                if id >= 0 and id <= size_of_list:

                    temp = ListNode(A[i][1])
                    #id is 0. Make it the first node
                    if id == 0:
                        temp.next = head
                        head = temp
                    #id is lenght of list. make it last element
                    elif id == size_of_list:
                        curr = head
                        i = 0
                        while i < size_of_list - 1:
                            curr = curr.next
                            i += 1
                        curr.next = temp
                    #id is between 0 and size_of_list
                    else:
                        prev = head
                        i = 0
                        while i < id - 1:
                            prev = prev.next
                            i += 1
                        temp.next = prev.next
                        prev.next = temp
                    
                    size_of_list += 1

        return head

                        

obj = Solution()
A = [
  [1, 13, -1],
  [3, 0, -1],
  [3, 1, -1],
  [2, 15, 0],
  [3, 0, -1],
  [1, 12, -1],
  [3, 0, -1],
  [1, 19, -1],
  [1, 13, -1],
  [3, 0, -1],
  [0, 12, -1],
  [1, 13, -1],
  [3, 2, -1]
]

h = obj.solve(A)
while h is not None:
    print(h.val)
    h = h.next


            


