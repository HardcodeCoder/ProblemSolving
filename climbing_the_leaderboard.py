"""
  @Author: HardcodeCoder
  @Created on:  18:41:00  Thursday 16 07 2020

"""

"""
  Problem is taken from Hackerrank: https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
"""

def climbingLeaderboard(scores_temp, alice):
    # stores the rank of alice for alice[i] score
    ranks = []

    # stores the current unique score in leaderboard
    # since scores in leaderboard is in descending order
    # this helps get the rank for a given score easily
    # rank for a given score is 1 + the index of that score
    scores = []

    # add the first score
    scores.append(scores_temp[0])
    # add the unique score in current leaderboard to scores
    for i in range(1, len(scores_temp)):
        if not scores_temp[i] == scores_temp[i-1]:
            scores.append(scores_temp[i])

    n = len(scores)

    # iterate over all scores of alice
    for i in range(len(alice)):
        # alice's score is greater than the largest score 
        # in the leaderboard append the rank (1) and continue
        if alice[i] >= scores[0]:
            ranks.append(1)
            continue
        else:
            # alice's score lies somewhere in the leaderboard
            start = 0
            end = n-1
            ans = -1
            f = 0
            alice_score = alice[i]

            # find the strictly largest score greater than alice_score
            while start <= end:
                mid = (start + end)//2

                if scores[mid] == alice_score:
                    # alice's score is similar to that 
                    # already in the leaderboard
                    rank = mid + 1
                    ranks.append(rank)
                    f = 1
                    break
                elif alice_score > scores[mid]:
                    end = mid - 1
                else:
                    ans = mid
                    start = mid+1

            if f == 1:
                continue
            # ans donotes the index of the strictly largest score
            # adding 1 to it gives the rank for that score
            # adding 1 to the previous rank gives the new rank
            rank = ans + 2
            ranks.append(rank)

    return ranks


n = int(input("Enter the number of players: "))
print("Enter the scores in the leaderboard in decreasing order: ")
scores_leaderboard = [int(i) for i in input().split()]

m = int(input("Enter the number of game alice played: "))
print("Enter the scores of alice in ascending order: ")
alice_scores = [int(i) for i in input().split()]

res = climbingLeaderboard(scores_leaderboard, alice_scores)
print("Alice's rank after each game: ")
for i in res:
    print(i)