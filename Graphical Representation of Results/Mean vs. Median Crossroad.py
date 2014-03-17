import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import pylab as P

cr = np.genfromtxt("C:\Users\Alexander\Dropbox\St Georges\Mathematics\Exploration\Crossroad Output.txt")
mu = np.mean(cr) # mu = 80.64
sigma = np.std(cr) # sigma (standard deviation) = 2.08

print mu
print sigma


y_mu = P.normpdf(mu, mu, sigma)
yy = mu + sigma * np.random.randn(100000)

r = (np.arange(70,90.5,1))
r_detailed = (np.arange(70,90,0.02))


plt.hist(yy, bins=r, normed=1, color= 'b')
plt.hist(cr, bins=r, normed=1, color= 'g')
y = P.normpdf(r_detailed, mu, sigma)

plt.plot(r_detailed, y, linewidth=5.0, color = 'r')
plt.axis([78.5,83.5,0.165,0.205])

plt.plot([mu], [y_mu], 'yx', ms=30, mew=5)

plt.annotate('Sample Mean = 80.6', xy=(mu, y_mu ), xytext=(mu-1.6, y_mu+0.002),
            arrowprops=dict(facecolor='black', shrink=0.15),
            )
            
median = np.median(cr) # median = 81.0          
plt.plot([median], [0.195], 'rx', ms=30, mew=5)

plt.annotate('Sample Median = 81.0', xy=(median , 0.195 ), xytext=(median+0.6, 0.197 ),
            arrowprops=dict(facecolor='black', shrink=0.15),
            )
            
plt.text(80.2,0.2, r'$\mu=80.64, \ \sigma =2.08 $', fontsize = 16)

plt.title('Histograms of Crossroad Throughput - Real Data in Green')
plt.grid(True)
plt.ylabel('Relative Frequency')
plt.xlabel('Number of Cars Passed')
plt.text(75.3,0.15, r'$\mu=80.64, \ \sigma =2.08 $')

plt.show()