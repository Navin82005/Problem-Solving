import random

fact = int(input())
r, c = list(map(int, input().split()))
mat = [input().split() for _ in range(r)]

while True:
    mats = list(map(int, input().split()))
    for i in mats:
        for j in range(fact):
            print()