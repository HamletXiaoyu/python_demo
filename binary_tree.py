#!/usr/bin/env python
#coding=utf-8
#title        :
#description  :
#author       :
#email        :
#date         :
#notes        :

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def build_tree(arr, idx):
    if arr[idx] != 'null':
        root=TreeNode(arr[idx])
        if idx*2+1 > 14:
            return root
        root.left  = build_tree(arr, idx*2+1)
        root.right = build_tree(arr, idx*2+2)
        return root
    else:
        return None

def pre_order(root):
    if not root:
        return
    print(root.val)
    pre_order(root.left)
    pre_order(root.right)
        
def find_path(root, path):
    if not root:
        return
    path.append(root.val)
    if not root.left and not root.right:
        print path
        path.pop()
        return
    if root.left:
        find_path(root.left, path)
    if root.right:
        find_path(root.right, path)
    path.pop()
        
####
arr = [5,4,8,11,'null',13,4,7,2,'null','null','null','null',5,1]

root = build_tree(arr, 0)

pre_order(root)
path = []
find_path(root, path)
