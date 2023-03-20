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