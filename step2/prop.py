# 正規分布の累積分布関数-Cumulative Distribution Function, CDF-（あるxまでの値の積分値）を求めることができる。
import os
import numpy as np
from scipy.stats import norm


path = os.path.join(os.path.dirname(__file__), 'height.txt')
xs = np.loadtxt(path)
mu = np.mean(xs)
sigma = np.std(xs)

p1 = norm.cdf(160, mu, sigma)
print('p(x <= 160):', p1)

p2 = norm.cdf(180, mu, sigma)
print('p(x > 180):', 1-p2)
