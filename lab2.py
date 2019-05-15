import numpy
import threading

A = numpy.array([[4,2],[1,3]])
B = numpy.array([[2,3],[2,1]]) 
C = numpy.array([[0,0],[0,0]])

def Mult_mat(a,b,i):
    for j in range (len(A)):
        C[i][j] = sum(map(lambda x,y: x*y, a[i], b[j]))

for i in range (len(A)):
     threading.Thread(target=Mult_mat, args=(A,B,i)).start()
        
print("Результат перемножения матриц:")
print(C)
