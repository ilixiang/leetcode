#!/usr/bin/python3

def selectionSort(nums):
    for i in range(0, len(nums)):
        minIndex = i
        for j in range(i, len(nums)):
            minIndex = minIndex if nums[minIndex] < nums[j] else j
        tmp = nums[minIndex]
        nums[minIndex] = nums[i]
        nums[i] = tmp

def bubbleSort(nums):
    for i in range(0, len(nums) - 1):
        swapped = False
        for j in range(0, len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                tmp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = tmp
                swapped = True
        if swapped == False:
            return

def insertionSort(nums):
    for i in range(1, len(nums)):
        for j in range(i, 1, -1):
            if nums[j] < nums[j - 1]:
                tmp = nums[j]
                nums[j] = nums[j - 1]
                nums[j - 1] = tmp
            else:
                break
            

def mergeSort(nums):
    mergeSortPartition(nums, 0, len(nums))

def mergeSortPartition(nums, start, end):
    if start == end or start == end - 1:
        return
    mid = (start + end) // 2
    mergeSortPartition(nums, start, mid)
    mergeSortPartition(nums, mid, end)

    mergedNums = merge(nums[start:mid], nums[mid:end])
    for i in range(start, end):
        nums[i] = mergedNums[i - start]

def merge(nums1, nums2):
    if len(nums1) == 0:
        return list(nums2)

    if len(nums2) == 0:
        return list(nums1)

    result = []
    i1 = 0
    i2 = 0
    while i1 < len(nums1) and i2 < len(nums2):
        if nums1[i1] > nums2[i2]:
            result.append(nums2[i2])
            i2 = i2 + 1
        elif nums1[i1] <= nums2[i2]:
            result.append(nums1[i1])
            i1 = i1 + 1
    while i1 < len(nums1):
        result.append(nums1[i1])
        i1 = i1 + 1
    while i2 < len(nums2):
        result.append(nums2[i2])
        i2 = i2 + 1

    return result

def quickSort(nums):
    quickSortPartition(nums, 0, len(nums))

def quickSortPartition(nums, start, end):
    if start == end or start == end - 1:
        return
    partition = nums[end - 1]
    boudary = start - 1
    for i in range(start, end - 1):
        if nums[i] <= partition:
            tmp = nums[i]
            nums[i] = nums[boudary + 1]
            nums[boudary + 1] = tmp
            boudary = boudary + 1
    tmp = nums[boudary + 1]
    nums[boudary + 1] = nums[end - 1]
    nums[end - 1] = tmp

    quickSortPartition(nums, start, boudary + 1)
    quickSortPartition(nums, boudary + 2, end)

def heapSort(nums):
    heapSize = 0
    heap = [0] * len(nums)
    for num in nums:
        heapInsert(heap, heapSize, num)
        heapSize = heapSize + 1

    for i in range(0, len(nums)):
        nums[i] = heap[0]
        heap[0] = heap[heapSize - 1]
        heapSize = heapSize - 1
        heapify(heap, heapSize, 0)

def heapInsert(heap, heapSize, num):
    heap[heapSize] = num
    index = heapSize
    while index > 0 and heap[index] > heap[(index - 1) // 2]:
        tmp = heap[index]
        heap[index] = heap[(index - 1) // 2]
        heap[(index - 1) // 2] = tmp
        index = (index - 1) // 2

def heapify(heap, heapSize, index):
    if heapSize == 0 or heapSize == 1 or index >= heapSize:
        return
    leftChildIndex = 2 * index + 1
    rightChildIndex = 2 * index + 2
    while leftChildIndex < heapSize or rightChildIndex < heapSize:
        swapIndex = leftChildIndex
        if leftChildIndex >= heapSize or (rightChildIndex < heapSize and heap[leftChildIndex] < heap[rightChildIndex]):
            swapIndex = rightChildIndex
        if heap[swapIndex] <= heap[index]:
            break

        tmp = heap[swapIndex]
        heap[swapIndex] = heap[index]
        heap[index] = tmp

        index = swapIndex
        leftChildIndex = 2 * index + 1
        rightChildIndex = 2 * index + 2

def radixSort(nums):
    pass

nums = [4, 3, 5, 1, 7]
heapSort(nums)
print(nums)

