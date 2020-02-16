sm=0
fibo0 = 0
fibo1 = 1
fibo = 0
while True:
    fibo = fibo0+fibo1
    
    if fibo%2 ==0:
        print(fibo)
        sm = sm+fibo

    fibo0=fibo1
    fibo1=fibo
    if (fibo > 4000000):
        break

print("sum of even fibonacci numbers up to 4000000: ")
print(sm)

#finished