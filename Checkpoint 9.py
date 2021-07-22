#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1
def binary_search(lis, find):
    compteur= 0
    for i in lis:
        if i == find:
            return True
        else:
            compteur += 1
            if compteur == len(lis):
                return False
binary_search([1,2,3,5,8], 3)


# In[2]:


# 2
import math
def power(a,b):
    return int(math.pow(a,b))
power(3,4)


# In[3]:


# 3
def bubble_sort(nlist):
    for passnum in range(len(nlist)-1, 0, -1):
        for i in range(passnum):
            if nlist[i]> nlist[i+1]:
                temp = nlist[i]
                nlist[i]= nlist[i+1]
                nlist[i+1]= temp
    return nlist

bubble_sort([29,13,22,37,52,49,46,71,56])


# In[4]:


# 4
def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
              # The value from the left half has been used
              myList[k] = left[i]
              # Move the iterator forward
              i += 1
            else:
                myList[k] = right[j]
                j += 1
            k += 1

        # For all the remaining values
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1

myList = [29,13,22,37,52,49,46,71,56]
mergeSort(myList)
print(myList)


# In[5]:


# 5
def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1


        while low <= high and array[low] <= pivot:
            low = low + 1


        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:

            break

    array[start], array[high] = array[high], array[start]

    return high

def quick_sort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)

array = [29,13,22,37,52,49,46,71,56]
quick_sort(array, 0, len(array) - 1)
print(array)


# In[ ]:




