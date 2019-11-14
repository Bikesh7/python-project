#prime number in range
for n in range(1,20):
    ans= True
    for i in range(2, n):
        if n % i == 0:
            ans = False
            break
    if ans == True:
        print(n,"is prime")
    else:
        print(n,"is not a prime")