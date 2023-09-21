n = int(input())
lst1 = [2**i for i in range(1,n) if 2**i < n]
print(lst1)