"""
  @Author: HardcodeCoder
  @Created on:  19:36:46  Saturday 18 07 2020
"""

"""
  Problem description: https://www.hackerrank.com/challenges/bigger-is-greater/problem

  Algorithm reference: https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
"""

# input number of test cases
t = int(input())

# iterate to process each test case
for i in range(t):
    word = input()
    l = len(word)
    #base case
    if l == 1:
        print("no answer")
        continue

    # Find the weekly non-increasing suffix start index
    start = 0
    for i in range(1, l):
        if ord(word[i-1]) < ord(word[i]):
            start = i
    pivot = start - 1

    # Word is already in largest permutation possible
    if pivot < 0:
        print("no answer")
        continue

    # find smallest character in the non-increasing suffix 
    # which is greater than pivot character
    pivot_element = ord(word[pivot])
    smallest = l - 1
    for j in range(l - 1, start - 1, -1):
        if ord(word[j]) > pivot_element:
            smallest = j
            break
    
    # create temp suffix string with smallest character swapped with the pivot character
    temp = word[start:smallest] + word[pivot] + word[smallest+1:]

    # reverse the suffix to get the smallest possible suffix 
    # because we will change the prefix
    suffix = temp[::-1]

    # add all the word parts together swapping pivot element with the smallest character in suffix
    answer = word[:pivot] + word[smallest] + suffix
    print(answer)