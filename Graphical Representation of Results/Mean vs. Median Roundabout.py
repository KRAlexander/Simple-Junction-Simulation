import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import pylab as P

ra = np.genfromtxt("C:\Users\Alexander\Dropbox\St Georges\Mathematics\Exploration\Roundabout Output.txt")
mu = np.mean(ra) # mu = 76.92
sigma = np.std(ra) # sigma (standard deviation) = 1.568
print "MU" , mu
print "Sigma" , sigma
y_mu = P.normpdf(mu, mu, sigma)
yy = mu + sigma * np.random.randn(100000)

r = (np.arange(70,90.5,1))
r_detailed = (np.arange(70,90,0.02))


plt.hist(yy, bins=r, normed=1)
plt.hist(ra, bins=r, normed=1)

y = P.normpdf(r_detailed, mu, sigma)
plt.plot(r_detailed, y, linewidth=5.0)
plt.axis([75.2,78.5,0.23,0.266])

plt.plot([mu], [y_mu], 'yx', ms=30, mew=5)

plt.annotate('Sample Mean = 76.9', xy=(mu, y_mu ), xytext=(mu-1.1, y_mu+0.002),
            arrowprops=dict(facecolor='black', shrink=0.15),
            )
            
median = np.median(ra) # median =  77.0

print "Median: " , median

plt.plot([median], [0.254], 'bx', ms=30, mew=5)

plt.annotate('Sample Median = 77.0', xy=(median , 0.254 ), xytext=(median+0.5, 0.257 ),
            arrowprops=dict(facecolor='black', shrink=0.1),
            )

plt.text(76.4,0.2605, r'$\mu=76.92, \ \sigma =1.57 $', fontsize = 16)

plt.title('Histograms of Roundabout Throughput - Real Data in Green')
plt.grid(True)
plt.ylabel('Relative Frequency')
plt.xlabel('Number of Cars Passed')



plt.show()