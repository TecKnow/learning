#!/usr/bin/env python3
"""
Problem  : Insertion Sort
URL      : http://rosalind.info/problems/ins/
Author   : David P. Perkins
"""

def swap(array, a, b):
    array[a], array[b] = array[b], array[a]
    swap.swapcount += 1
swap.swapcount = 0;

def insertionSort(array):
    for k in range(1, len(array)):
        while k > 0 and array[k] < array[k-1]:
            swap(array, k-1, k)
            k = k-1
if __name__=="__main__":
    with open("insIn.txt", "r") as infile:
        infile.readline()
        array = [int(x) for x in infile.readline().split()]
        insertionSort(array)
        print(swap.swapcount)
    
