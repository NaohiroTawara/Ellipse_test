# -*- coding: utf-8 -*-
import math
import numpy as np
import scipy.linalg
from matplotlib import pyplot as plt

# 楕円を生成し半分だけ消す
# Generate ellipse
X=np.array([2*np.cos(np.arange(0,2*math.pi,0.01)),np.sin(np.arange(0,2*math.pi,0.01))]).T

# 楕円を４５度回転する
# Rotate ellipse
theta=np.array([[np.cos(math.pi/4),-np.sin(math.pi/4)], [np.sin(math.pi/4),np.cos(math.pi/4)]])
XX=np.dot(X[:300,:],theta)

# 楕円が何度回転しているか計算し、変換する
# Revert rotated ellipse to original one
[U,S,V]=scipy.linalg.svd(XX);
Y=np.dot(U[:,:2],np.diag(S))

# Visualize
plt.plot(XX[:,0],XX[:,1],'x');
plt.plot(Y[:,0],Y[:,1],'x');
plt.xlim(-5,5);plt.ylim(-5,5);
plt.legend(['original','estimated'])
plt.show()
