# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 16:33:31 2021

@author: Masanori Akaishi
"""
import matplotlib.pyplot as plt


# 準備資料

# 手寫數字資料
# 請注意，這會需要花點時間
from sklearn.datasets import fetch_openml
mnist = fetch_openml('mnist_784', version=1,)

# 影像資料
image = mnist.data
# 標準答案
label = mnist.target

print(type(mnist.data))

'''
# 指定畫布大小
plt.figure(figsize=(10, 3))

# 繪製 20 張影像
for i in range(20): 
    
    # 取得第 i 個 ax 變數 （共有 2 列 10 行個子圖)
    ax = plt.subplot(2, 10, i+1)
    
    # 取得第 i 筆影像資料並轉換成 28x28
    img = image[i].reshape(28,28)
    
    # 繪製出 img 的影像
    ax.imshow(img, cmap='gray_r')
    
    # 在標題中顯示標準答案
    ax.set_title(label[i])
    
    # 隱藏 x, y 的刻度
    ax.set_xticks([])
    ax.set_yticks([])
    
# 避免與相鄰物件重疊
plt.tight_layout()

# 顯示圖形
plt.show() 
'''