#1.6.1 単純なグラフの描画
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,6,0.1)
y = np.sin(x)

plt.plot(x,y)
plt.show

#1.6.2 pyplotの機能
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x,y1,label='sin')
plt.plot(x,y2,linestyle='--',label='cos')
plt.xlabel('x')
plt.ylabel('y')
plt.title('sin&cos')
plt.legend()
plt.show()

#1.6.3 画像の表示
from matplotlib.image import imread

img = imread(r"C:\Users\Learn\OneDrive\画像\カメラ ロール\photo0000-5555.jpg")
plt.imshow(img)
plt.show()

#以上で第1章終了
