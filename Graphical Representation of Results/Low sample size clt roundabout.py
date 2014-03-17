import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
import pylab as P
import math

ra = np.genfromtxt ("C:\Users\Alexander\Dropbox\St Georges\Mathematics\Exploration\Roundabout Output.txt")

def get_average(x):
    number_terms_averaged = x
    number_of_averages = 100000 / number_terms_averaged
    average=np.zeros((number_of_averages,))
    for n in range(number_of_averages):  
        average[n] = np.mean(ra[((number_terms_averaged)*n):(number_terms_averaged*(n+1))])      
    return average
 
fig = plt.figure(1)
fig.suptitle('Roundabout Distribution - Trend towards a normal distribution', fontweight = 'bold')


average = get_average(5)

plt.text(75,0.45, "n=5", fontsize = 16)
mu = np.mean(average)
sigma = np.std(average)
print mu
print sigma
print math.sqrt((sigma**2)*1)

r = np.arange(np.min(average),np.max(average), 0.2  )
r_detailed = (np.arange(60,85,0.005))
y = P.normpdf(r_detailed, mu, sigma)

plt.hist(average, bins=r, normed = 1)


plt.plot(r_detailed, y, linewidth=5.0)

plt.axis([(mu-3.5*sigma),(mu+3.5*sigma),0,P.normpdf(mu, mu, sigma)*1.1])



plt.show()
