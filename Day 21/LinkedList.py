
class ListNode:

    def __init__(self,x):
        self.val = x
        self.next = None


head = None
size_of_ll = 0

def insert_node(position, value):
    # @param position, an integer
    # @param value, an integer

    global head
    global size_of_ll

    temp = ListNode(value)
    if position >= 1 and position <= size_of_ll + 1:
        if position == 1:
            temp.next = None
            head = temp 
        else:
            i = 1
            prev = head
            while i  < position - 1:
                prev = prev.next
                i += 1
           
            if position != size_of_ll+1:
                temp.next = prev.next
                prev.next = temp
            elif position == size_of_ll+1:
                prev.next = temp
                temp.next = None
        
        size_of_ll += 1
    

def delete_node(position):
    # @param position, integer
    # @return an integer
    global head
    global size_of_ll
    if position >=1 and position <= size_of_ll:
        temp = None
        if position == 1:
            temp = head
            head = head.next
        else:

            i = 1
            prev = head
            while i < position-1:
                prev = prev.next
                i += 1
            temp = prev.next
            prev.next = prev.next.next

        
        size_of_ll -= 1


def print_ll():
    # Output each element followed by a space
    global head
    global size_of_ll

    temp = head
    res = []
    while(temp != None):
        res.append(str(temp.val))
        temp = temp.next
    print(" ".join(res))
    

    

    



            
            






