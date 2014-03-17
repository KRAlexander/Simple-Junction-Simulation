import numpy as np
import matplotlib.pyplot as plt
import pylab as P

cr = np.genfromtxt("C:\Users\Alexander\Dropbox\St Georges\Mathematics\Exploration\Crossroad Output.txt")


ra = np.genfromtxt ("C:\Users\Alexander\Dropbox\St Georges\Mathematics\Exploration\Roundabout Output.txt")


print "Mean Crossroad" , "Mean Roundabout"
print np.mean(cr), np.mean(ra)


mu = np.mean(cr)
sigma = np.std(cr)
r = (np.arange(70,90.5,1))
r_detailed = (np.arange(70,90,0.02))
plt.hist(cr, bins=r, normed=1)
y = P.normpdf(r_detailed, mu, sigma)
plt.plot(r_detailed, y, linewidth=5.0)
plt.axis([72,87,0,0.28])

mu = np.mean(ra)
sigma = np.std(ra)
plt.hist(ra, bins=r, normed=1)
y = P.normpdf(r_detailed, mu, sigma)
line, = plt.plot(r_detailed, y, linewidth=5.0)
line.set_antialiased(True)

plt.annotate('Roundabout', xy=(76 , 0.21 ), xytext=(72.7 ,0.225 ),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )
plt.annotate('Crossroad', xy=(82.4 , 0.18 ), xytext=(83.6 ,0.225 ),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )            

plt.text(72.7,0.25, r'$\mu=76.92, \ \sigma =1.57 $')

plt.text(83,0.25, r'$\mu=80.64, \ \sigma =2.08 $')


plt.title('Histogram of both System Outputs')
plt.grid(True)
plt.ylabel('Relative Frequency')
plt.xlabel('Number of Cars Passed')
plt.show()
#print bins

