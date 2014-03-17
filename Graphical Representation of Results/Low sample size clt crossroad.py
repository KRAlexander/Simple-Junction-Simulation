import numpy as np
import matplotlib.pyplot as plt
import pylab as P

ra = np.genfromtxt ("C:\Users\Alexander\Dropbox\St Georges\Mathematics\Exploration\Crossroad Output.txt")
#print "RA shape: ",  ra.shape
#mu = np.mean(ra) # mu = 76.92
#sigma = np.std(ra) # sigma (standard deviation) = 1.568
def get_average(x):
    number_terms_averaged = x
    number_of_averages = 100000 / number_terms_averaged
    average=np.zeros((number_of_averages,))
    for n in range(number_of_averages):  
        average[n] = np.mean(ra[((number_terms_averaged)*n):(number_terms_averaged*(n+1))])      
    return average
 

plt.figure(1)


plt.subplot(111)

average = get_average(5)
plt.text(78.5,0.45, "n=5")
mu = np.mean(average)
sigma = np.std(average)
print mu
print sigma


plt.title('Crossroad Distribution - Trend towards a normal distribution')
plt.axis([(mu-2.6),(mu+2.6),0,0.51])
r = np.arange(70,90,0.2)
r_detailed = (np.arange(75,85,0.005))
y = P.normpdf(r_detailed, mu, sigma)
plt.hist(average, bins=r, normed = 1)
plt.plot(r_detailed, y, linewidth=5.0)
plt.grid(True)



plt.show()