import numpy as np
import matplotlib.pyplot as plt
import pylab as P
import math

cr_rush =    np.genfromtxt("C:\Users\Alexander\Dropbox\St Georges\Mathematics\Exploration\crossroads_analytics_rush.txt")
cr =         np.genfromtxt("C:\Users\Alexander\Dropbox\St Georges\Mathematics\Exploration\Crossroad Output.txt")
ra =         np.genfromtxt("C:\Users\Alexander\Dropbox\St Georges\Mathematics\Exploration\Roundabout Output.txt")
ra_rush =    np.genfromtxt("C:\Users\Alexander\Dropbox\St Georges\Mathematics\Exploration\oundabout_analytics_rush.txt")

print "Size of Data:"
print np.size(cr_rush)
print np.size(cr)
print np.size(ra)
print np.size(ra_rush)

numberterms=5
bingraduation = 0.4
linewidths = 6.0

def get_average_rush(x,ram):
    number_terms_averaged = x
    number_of_averages = 16410 / number_terms_averaged
    average=np.zeros((number_of_averages,))
    for n in range(number_of_averages):  
        average[n] = np.mean(ram[((number_terms_averaged)*n):(number_terms_averaged*(n+1))])      
    return average
def get_average(x,ram):
    number_terms_averaged = x
    number_of_averages = 100000 / number_terms_averaged
    average=np.zeros((number_of_averages,))
    for n in range(number_of_averages):  
        average[n] = np.mean(ram[((number_terms_averaged)*n):(number_terms_averaged*(n+1))])      
    return average


average = get_average_rush(numberterms,cr_rush)
mu = np.mean(average)
sigma = np.std(average)
r_detailed = (np.arange(70,90,0.02))
y = P.normpdf(r_detailed, mu, sigma)
plt.plot(r_detailed, y, linewidth=linewidths)


r = np.arange(70,90,bingraduation)
plt.hist(average, bins=r, normed = 1)
plt.annotate('CR Rush: $(\mu = 83.93 , \sigma = 0.869)$', xy=(mu , P.normpdf(mu,mu,sigma)), xytext=(mu-1.8 , P.normpdf(mu,mu,sigma)+0.07),
            arrowprops=dict(facecolor='black', shrink=0.2),
            )

print "CR Rush"
print mu
print sigma
print sigma*sigma

average = get_average(numberterms,cr)
mu = np.mean(average)
sigma = np.std(average)
r_detailed = (np.arange(70,90,0.02))
y = P.normpdf(r_detailed, mu, sigma)
plt.plot(r_detailed, y, linewidth=linewidths)

r = np.arange(70,90,bingraduation)
plt.hist(average, bins=r, normed = 1)
plt.annotate('CR: $(\mu = 80.59 , \sigma = 0.904)$', xy=(mu , P.normpdf(mu,mu,sigma)), xytext=(mu-2 , P.normpdf(mu,mu,sigma)+0.05),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )
print "CR"
print mu
print sigma
print sigma*sigma
average = get_average(numberterms,ra)
mu = np.mean(average)
sigma = np.std(average)
r_detailed = (np.arange(70,90,0.02))
y = P.normpdf(r_detailed, mu, sigma)
plt.plot(r_detailed, y, linewidth=linewidths)
r = np.arange(70,90,bingraduation)
plt.hist(average, bins=r, normed = 1)
plt.annotate('RA: $(\mu = 76.92 , \sigma = 0.800)$', xy=(mu , P.normpdf(mu,mu,sigma)), xytext=(mu+1 , P.normpdf(mu,mu,sigma)+0.025),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )
print "RA"
print mu
print sigma
print sigma*sigma
average = get_average_rush(numberterms,ra_rush)
mu = np.mean(average)
sigma = np.std(average)
r_detailed = (np.arange(70,90,0.02))
y = P.normpdf(r_detailed, mu, sigma)
plt.plot(r_detailed, y, linewidth=linewidths)
r = np.arange(70,90,bingraduation)
plt.hist(average, bins=r, normed = 1)
plt.annotate('RA Rush: $(\mu = 76.56 , \sigma = 0.731)$', xy=(mu , P.normpdf(mu,mu,sigma)), xytext=(mu-2 , P.normpdf(mu,mu,sigma)+0.018),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )

print "RA Rush"
print mu
print sigma
print sigma*sigma

plt.axis([73.8,87.6,0,0.61])

plt.title('Comparing All Distributions, CLT n=5')
plt.grid(True)
plt.ylabel('Relative Frequency')
plt.xlabel('Number of Cars Passed')
plt.show()