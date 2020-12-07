def sort(A,n):
    for i in range(n):
        for j in range(n-1,i,-1):
            if A[0][j-1]>A[0][j]: 
              A[0][j-1], A[0][j] = A[0][j], A[0][j-1]
              A[1][j-1], A[1][j] = A[1][j], A[1][j-1]
    
    return A

def con(A,n,B):
    b0=[]
    b1=[]
    b0.append(A[0][0])
    b1.append(A[1][0])
    j=0
    k=1
    for i in range (1,n):
        if A[0][i]<=b1[j]:
            if A[1][i]>b1[j]:
                b1[j]=A[1][i]
        else:
            b0.append(A[0][i])
            b1.append(A[1][i])
            j=j+1
            k=k+1
    B.append(b0)
    B.append(b1)
    return k

print("Колво отрезков")
n=int(input())
print("отрезки")
if n<1:
  print("мало")
A = [[0] * n for i in range(2)]
for j in range(n):
    for i in range(2):
        A[i][j]=int(input())
        if i==1 and A[1][j]<=A[0][j]:
            print("не то")
A=sort(A,n)
for i in range(2):
    for j in range(n):
        print(A[i][j])
    print()
B=[]
k=con(A,n,B)
for i in range(2):
    for j in range(k):
        print(B[i][j])
    print()
print("Отрезок:")
a=int(input())
b=int(input())
if b<=a:
    print("не то")
boo=False
for i in range(k):
    if a>=B[0][i] and b<=B[1][i]:
        boo=True
if boo:
    print("да")
else:
    print("нет")
