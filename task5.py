def rotate(Ax,Ay,Bx,By,Cx,Cy):
  if(Bx-Ax)*(Cy-By)-(By-Ay)*(Cx-Bx)<0:
    return -1
  elif (Bx-Ax)*(Cy-By)-(By-Ay)*(Cx-Bx)>0:
    return 1
  else:
    return 0

def v(A,n):
  s=rotate(A[0][0],A[1][0],A[0][1],A[1][1],A[0][2],A[1][2])
  for i in range(n-2):
    if rotate(A[0][i],A[1][i],A[0][i+1],A[1][i+1],A[0][i+2],A[1][i+2])!=s:
      return False
  if (rotate(A[0][n-1],A[1][n-1],A[0][0],A[1][0],A[0][1],A[1][1])!=s) or (rotate(A[0][n-2],A[1][n-2],A[0][n-1],A[1][n-1],A[0][0],A[1][0])!=s):
    return False
  else:
    return True

def sort(A,n):
  for i in range(n):
    if A[0][i]<A[0][0]: 
      A[0][i], A[0][0] = A[0][0], A[0][i]
      A[1][i], A[1][0] = A[1][0], A[1][i]
  for i in range(1,n): 
    j = i
    while j>1 and (rotate(A[0][0],A[1][0],A[0][j-1],A[1][j-1],A[0][j],A[1][j])<0):
      A[0][j], A[0][j-1] = A[0][j-1], A[0][j]
      A[1][j], A[1][j-1] = A[1][j-1], A[1][j]
      j -= 1
  return A

def m(A,n):
  for i in range (n-2):
    if rotate(A[0][i],A[1][i],A[0][i+1],A[1][i+1],A[0][i+2],A[1][i+2])==0:
      return False
  if (rotate(A[0][n-1],A[1][n-1],A[0][0],A[1][0],A[0][1],A[1][1])==0) or (rotate(A[0][n-2],A[1][n-2],A[0][n-1],A[1][n-1],A[0][0],A[1][0])==0):
    return False
  return True

print("колво точек")
n=int(input())
if n<3:
  print("мало точек")
A = [[0] * n for i in range(2)]
print("точки")
for j in range(n):
    for i in range(2):
        A[i][j]=int(input())
A=sort(A,n)
if m(A,n)==False:
  print("не многоуголник")
else:
  if v(A,n):
    print("выпуклый")
  else:
    print ("не выпуклый")
