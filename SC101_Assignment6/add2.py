"""
File: add2.py
Name: Anita Lee
------------------------
TODO: This program prints the sum of 2 linked list as a linked list with reversed order
      from units digit to higher the greatest digit.
"""

import sys


class ListNode:
    def __init__(self, data=0, pointer=None):
        self.val = data
        self.next = pointer


def add_2_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    l1_cur = l1
    l2_cur = l2
    carry = 0  # the digit that is transferred from the lower digits to the greater
    num_lst = 0  # the index of the node in the ans
    while True:
        if l1_cur is not None and l2_cur is not None:  # both linked list exit a node after
            num_sum = (l1_cur.val + l2_cur.val + carry) % 10  # the unit digit of the sum
            carry = (l1_cur.val + l2_cur.val + carry - num_sum) // 10  # the tenth digit of the sum
            l1_cur = l1_cur.next
            l2_cur = l2_cur.next

        elif l1_cur is not None:  # only l1 exits a node after
            num_sum = (l1_cur.val + carry) % 10  # the unit digit of the sum
            carry = (l1_cur.val + carry - num_sum) // 10  # the tenth digit of the sum
            l1_cur = l1_cur.next

        elif l2_cur is not None:  # only l2 exits a node after
            num_sum = (l2_cur.val + carry) % 10  # the unit digit of the sum
            carry = (l2_cur.val + carry - num_sum) // 10  # the tenth digit of the sum
            l2_cur = l2_cur.next

        elif carry:  # both linked list don't exit a node after, but there is still a number to be carried
            num_sum = carry
            carry = 0

        else:  # both linked list don't exit a node after, and there is no number to be carried
            break  # stop calculating the sum

        if num_lst == 0:  # the head of the linked list
            lst = ListNode(num_sum, None)  # the "next" value will be the previous node
            head = lst
        else:
            lst = ListNode(num_sum, lst)  # the "next" value will be the previous node
        num_lst += 1
    '''
    organize the order of the nodes: 
    originally, node.next links to the previous node, but it should be linking to the next node.
    '''
    cur = lst  # the last node of the ans
    next_node = None
    while cur is not None:  # traverse over the linked list and correct the order
        next_cur = cur.next  # the previous node
        cur.next = next_node  # correct the cur.next to the node after current node
        next_node = cur  # current node will be the .next value for the previous node
        cur = next_cur  # change the cur to the previous node of the currren
    return head


####### DO NOT EDIT CODE BELOW THIS LINE ########


def traversal(head):
    """
    :param head: ListNode, the first node to a linked list
    -------------------------------------------
    This function prints out the linked list starting with head
    """
    cur = head
    while cur.next is not None:
        print(cur.val, end='->')
        cur = cur.next
    print(cur.val)


def main():
    args = sys.argv[1:]
    if not args:
        print('Error: Please type"python3 add2.py test1"')
    else:
        if args[0] == 'test1':
            l1 = ListNode(2, None)
            l1.next = ListNode(4, None)
            l1.next.next = ListNode(3, None)
            l2 = ListNode(5, None)
            l2.next = ListNode(6, None)
            l2.next.next = ListNode(4, None)
            ans = add_2_numbers(l1, l2)
            print('---------test1---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test2':
            l1 = ListNode(9, None)
            l1.next = ListNode(9, None)
            l1.next.next = ListNode(9, None)
            l1.next.next.next = ListNode(9, None)
            l1.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next.next = ListNode(9, None)
            l2 = ListNode(9, None)
            l2.next = ListNode(9, None)
            l2.next.next = ListNode(9, None)
            l2.next.next.next = ListNode(9, None)
            ans = add_2_numbers(l1, l2)
            print('---------test2---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test3':
            l1 = ListNode(0, None)
            l2 = ListNode(0, None)
            ans = add_2_numbers(l1, l2)
            print('---------test3---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        else:
            print('Error: Please type"python3 add2.py test1"')


if __name__ == '__main__':
    main()
