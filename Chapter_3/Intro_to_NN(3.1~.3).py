#3.1~ NNの例

#3.2.2 ステップ関数の実装（仮）
def step_function(x):
    if x > 0:
        return 1
    else:
        return 0
    
#3.2.3 ステップ関数のグラフ
import numpy as np
import matplotlib.pylab as plt

def step_function2(x):
    return np.array(x > 0,dtype=np.int)

x = np.arange(-5.0,5.0,0.1)
y = step_function2(x)
plt.plot(x,y)
plt.ylim(-0.1,1.1)
plt.show

#3.2.4 シグモイド関数の実装
def sigmoid(x):
    return 1/(1 + np.exp(-x))

x = np.array([-1.0,1.0,2.0])
print(sigmoid(x))

t = np.array([1.0,2.0,3.0])
print(1.0 + t)
print(1.0 / t)

x = np.arange(-5.0,5.0,0.1)
y = sigmoid(x)
plt.plot(x,y)
plt.ylim(-0.1,1.1)
plt.show

#3.2.7 ReLU関数
def relu(x):
    return np.maximum(0,x)

#3.3.1 多次元配列
A = np.array([1,2,3,4])
print(A)
print(np.ndim(A),A.shape,A.shape[0])

B = np.array([[1,2],[3,4],[5,6]])
print(B)
print(B.ndim,B.shape)
#3.3.2 行列の積
A = np.array([[1,2],[3,4]])
print(A.shape)
B = np.array([[5,6],[7,8]])
print(B.shape)

print(np.dot(A,B))

A = np.array([[1,2,3],[4,5,6]])
print(A.shape)
B = np.array([[1,2],[3,4],[5,6]])
print(B.shape)

print(np.dot(A,B))

C = np.array([[1,2],[3,4]])
print(C.shape)

print(A.shape)
print(np.dot(C,A))#np.dot(A,C)はエラー

A = np.array([[1,2],[3,4],[5,6]])
print(A.shape)
B = np.array([7,8])
print(B.shape)
print(np.dot(A,B))

#3.3.3 NNの行列の積
X = np.array([1,2])
W = np.array([[1,3,5],[2,4,6]])
print(X.shape)
print(W)
print(W.shape)
Y = np.dot(X,W)
print(Y)

#以上が関数、行列の基本、
