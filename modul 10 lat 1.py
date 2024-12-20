#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 10:04:20 2024

@author: adesintia
"""

def bubbleSort(array):
    n = len(array)
 
    for i in range(n):
 
        for j in range(0, n-i-1):
 
            if array[j] > array[j+1] :
                array[j], array[j+1] = array[j+1], array[j]
                
def binarySearch(array, l, r, x):
 
    # Check base case
    if r >= l:
 
        mid = l + (r - l) // 2
 
        if array[mid] == x:
            return mid
 
        elif array[mid] > x:
            return binarySearch(array, l, mid-1, x)
 
        else:
            return binarySearch(array, mid + 1, r, x)
 
    else:
        return -1

array = [87, 56, 34, 23, 89, 15, 2, 200, 28, 31]
x = input("masukan yang dicari: ")
x = int(x)

bubbleSort(array)

result = binarySearch(array, 0, len(array)-1, x)
result = int(result)
print("Diurutkan jadi:", array)


if result != -1:
    print("Ada nih bang, ada di ", (result)+1)
else:
    print("Gak ada bang")
