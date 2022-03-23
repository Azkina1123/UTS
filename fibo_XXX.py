# contoh fibonacci

A = [0, 5, 7, 12, 15, 17, 19, 22, 25, 27, 32, 35, 37, 40, 45, 53]

FIBO = []

x = 100
F0 = 1
F1 = 1
Fibo = 1

j = 0
while Fibo <= x+1:
    FIBO.append(Fibo)
    Fibo = F0 + F1
    F0 = F1
    F1 = Fibo

    j += 1

print(j)
print(FIBO)

s = j - 1
FK = FIBO[s]

FK1 = FIBO[s-1]
i = FK1

FK2 = FIBO[s-2]
p = FK2

FK3 = FIBO[s-3]
q = FK3

m = (x+1) - FK

if (x > A[i]):
    i += m

Flag = 0

while i!=0 and Flag == 0:
    if x == A[i]:
        Flag = 1
    else:
        if x < A[i]:
            if q == 0:
                i = 0
            else:
                i = i - q
                t = p
                p = q
                q = t - q
        else:
            if p == 1:
                i = 0
            else:
                i += q
                p -= 1
                q -= p

if Flag == 1:
    print("Ketemu!")
else:
    print("Gak ketemu!")


