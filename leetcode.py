#!/usr/bin/env python
#coding=utf-8
#title        : leetcode
#description  : 
#author       :
#email        :
#date         :
#notes        :

'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret = self.add(l1, l2, 0)
        return ret
        
    def add(self, l1, l2, ten):
        if l1 and l2:
            a = (l1.val + l2.val + ten) % 10
            ret = ListNode(a)
            ret.next = self.add(l1.next, l2.next, (l1.val + l2.val + ten) / 10)
            return ret
        elif l1:
            ret = ListNode((l1.val + ten) %10)
            ret.next = self.add(l1.next, None, (l1.val + ten) /10)
            return ret
        elif l2:
            ret = ListNode((l2.val + ten) %10)
            ret.next = self.add(None, l2.next, (l2.val + ten) /10)
            return ret
        else:
            if ten != 0:
                return ListNode(ten)
            return None
