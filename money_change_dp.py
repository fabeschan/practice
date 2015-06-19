'''
Assume there are 3 kinds of notes whose values are $1, $2, and $5.
If I have $1000, how many ways I can change that amount into  $1, $2, and $5 notes.
For example, we have 2 ways to change $3, either 3 notes of $1 or 1 note of $1 and 1 note of $2.


recurrence:
p[V=v, A=a] = 1 if a=v

    $1  $2  $5
    --  --  --
0   1   1   1
1   1   1   1
2   1   2   2
3   1   2   2
4   1   3   3
5   1   3   5
6   1
7   1
8   1
9   1


'''

amount = 1000
coins = [1, 2, 5]

array = {}

for i in range(len(coins)):
    array[0, i] = 1

for i in range(amount+1):
    array[i, 0] = 1

for i in range(1, amount+1):
    array[i, 0] = 1
    for k in range(1, len(coins)):
        array[i, k] = array[i, k-1]
        if i-coins[k] >= 0:
            array[i, k] += array[i - coins[k], k]

print array[1000, 2]

