#1.5.1　Numpyのインポート
import numpy as np
x = np.array([1.0,2.0,3.0])
print(x)
print(type(x))

#1.5.3　Numpy配列の生成
y = np.array([2.0,4.0,6.0])
print(x+y)
print(x-y)
print(x*y)
print(x/y)
x = np.array([1.0,2.0,3.0])
print(x/2.0)

#1.5.4 NumpyのN次元配列
A = np.array([[1,2],[3,4]])
print(A)
print(A.shape)
print(A.dtype)
B = np.array([[3,0],[0,6]])
print(A+B)
print(A*B)
print(A)
print(A*10)

#1.5.5 ブロードキャスト
A = np.array([[1,2],[3,4]])
B = np.array([10,20])
print(A*B)

#1.5.6 要素へのアクセス
X = np.array([[51,55],[14,19],[0,4]])
print(X)
print(X[0],X[0][1])
for row in X:
    print(row)
X = X.flatten()
print(X)
X[np.array([0,2,4])]
print(X>5)
print(X[X>15])

#