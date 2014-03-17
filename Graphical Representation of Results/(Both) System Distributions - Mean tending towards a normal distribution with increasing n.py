import numpy as np
import matplotlib.pyplot as plt
import pylab as P
import math
#from scipy import stats

cr_rush =    np.genfromtxt("C:\Users\Alexander\Dropbox\St Georges\Mathematics\Exploration\crossroads_analytics_rush.txt")
cr =         np.genfromtxt("C:\Users\Alexander\Dropbox\St Georges\Mathematics\Exploration\Crossroad Output.txt")
ra =         np.genfromtxt("C:\Users\Alexander\Dropbox\St Georges\Mathematics\Exploration\Roundabout Output.txt")
ra_rush =    np.genfromtxt("C:\Users\Alexander\Dropbox\St Georges\Mathematics\Exploration\oundabout_analytics_rush.txt")

def get_average(x,ram):
    number_terms_averaged = x
    number_of_averages = 100000 / number_terms_averaged
    average=np.zeros((number_of_averages,))
    for n in range(number_of_averages):  
        average[n] = np.mean(ram[((number_terms_averaged)*n):(number_terms_averaged*(n+1))])      
    return average
 


fig=plt.figure(1)
fig.suptitle('System Distributions - Mean tending towards a normal distribution with increasing n', fontsize=14,fontweight='bold')



r_detailed = (np.arange(70,90,0.01))



for n in range(5):
    
    plt.subplot(521+(2*n))
    
    average = get_average(((60*(int(round(n**1.5,0))))+1),ra)
    mu = np.mean(average)
    sigma = np.std(average)
    print ((60*(int(round(n**1.5,0))))+1)
    print mu
    print sigma
    
    if n==0:
         r = np.arange(np.min(average),np.max(average),1) 
         plt.axis([(mu-3.5*sigma),(mu+3.5*sigma),0,(P.normpdf(mu, mu, sigma)*1.2)])
    else:
        size = np.size(average)
        n_bins = math.log(size,2)+1
        r = np.arange(np.min(average),np.max(average), ( (np.max(average)-np.min(average)) / n_bins) )
        plt.axis([(mu-3.5*sigma),(mu+3.5*sigma),0,(P.normpdf(mu, mu, sigma)*1.2)])
   
    y = P.normpdf(r_detailed, mu, sigma)
    plt.hist(average, bins=r, normed = 1, color = 'b')
    plt.plot(r_detailed, y, linewidth=5.0, color = 'g')
   
    plt.ylabel('Relative Frequency')
    

    if n==0: 
        plt.text(mu-3*sigma,(P.normpdf(mu, mu, sigma)*1), 'n=1')
        plt.text(mu-3*sigma,(P.normpdf(mu, mu, sigma)*0.8), '$\mu$=76.92')
        plt.text(mu-3*sigma,(P.normpdf(mu, mu, sigma)*0.6), '$\sigma$=1.57')
    elif n==1: 
        plt.text(mu-3*sigma,(P.normpdf(mu, mu, sigma)*1), 'n=61')
        plt.text(mu-3*sigma,(P.normpdf(mu, mu, sigma)*0.8), '$\mu$=76.92')
        plt.text(mu-3*sigma,(P.normpdf(mu, mu, sigma)*0.6), '$\sigma$=0.21')
    elif n==2: 
        plt.text(mu-3*sigma,(P.normpdf(mu, mu, sigma)*1), 'n=181')
        plt.text(mu-3*sigma,(P.normpdf(mu, mu, sigma)*0.8), '$\mu$=76.92')
        plt.text(mu-3*sigma,(P.normpdf(mu, mu, sigma)*0.6), '$\sigma$=0.11')
    elif n==3: 
        plt.text(mu-3*sigma,(P.normpdf(mu, mu, sigma)*1), 'n=301')
        plt.text(mu-3*sigma,(P.normpdf(mu, mu, sigma)*0.8), '$\mu$=76.92')
        plt.text(mu-3*sigma,(P.normpdf(mu, mu, sigma)*0.6), '$\sigma$=0.09')
    elif n==4: 
        plt.text(mu-3*sigma,(P.normpdf(mu, mu, sigma)*1), 'n=481')
        plt.text(mu-3*sigma,(P.normpdf(mu, mu, sigma)*0.8), '$\mu$=76.92')
        plt.text(mu-3*sigma,(P.normpdf(mu, mu, sigma)*0.6), '$\sigma$=0.07')
   
    if n==0:
        plt.title('Roundabout Distribution')
    if n==4:
        plt.xlabel('Number of Cars Passed')    

    plt.grid(True)
    
for n in range(5):
    if n==4:
        plt.subplot(520)
    else:
        plt.subplot(522+(2*n))
    
    average = get_average(((60*(int(round(n**1.5,0))))+1),cr)
    mu = np.mean(average)
    sigma = np.std(average)
    print ((60*(int(round(n**1.5,0))))+1)
    print mu
    print sigma
    
    if n==0:
         r = np.arange(np.min(average),np.max(average),1) 
         plt.axis([(mu-3.5*sigma),(mu+3.5*sigma),0,(P.normpdf(mu, mu, sigma)*1.2)])
    else:
        size = np.size(average)
        n_bins = math.log(size,2)+1
        r = np.arange(np.min(average),np.max(average), ( (np.max(average)-np.min(average)) / n_bins) )
        plt.axis([(mu-3.5*sigma),(mu+3.5*sigma),0,(P.normpdf(mu, mu, sigma)*1.2)])
   
    y = P.normpdf(r_detailed, mu, sigma)
    plt.hist(average, bins=r, normed = 1, color = 'r')
    plt.plot(r_detailed, y, linewidth=5.0, color = 'g')
    
    if n==0: 
        plt.text(mu-3*sigma,(P.normpdf(mu, mu, sigma)*1), 'n=1')
        plt.text(mu-3*sigma,(P.normpdf(mu, mu, sigma)*0.8), '$\mu$=80.64')
        plt.text(mu-3*sigma,(P.normpdf(mu, mu, sigma)*0.6), '$\sigma$=2.08')
    elif n==1: 
        plt.text(mu-3*sigma,(P.normpdf(mu, mu, sigma)*1), 'n=61')
        plt.text(mu-3*sigma,(P.normpdf(mu, mu, sigma)*0.8), '$\mu$=80.64')
        plt.text(mu-3*sigma,(P.normpdf(mu, mu, sigma)*0.6), '$\sigma$=0.30')
    elif n==2: 
        plt.text(mu-3*sigma,(P.normpdf(mu, mu, sigma)*1), 'n=181')
        plt.text(mu-3*sigma,(P.normpdf(mu, mu, sigma)*0.8), '$\mu$=80.64')
        plt.text(mu-3*sigma,(P.normpdf(mu, mu, sigma)*0.6), '$\sigma$=0.17')
    elif n==3: 
        plt.text(mu-3*sigma,(P.normpdf(mu, mu, sigma)*1), 'n=301')
        plt.text(mu-3*sigma,(P.normpdf(mu, mu, sigma)*0.8), '$\mu$=80.64')
        plt.text(mu-3*sigma,(P.normpdf(mu, mu, sigma)*0.6), '$\sigma$=0.13')
    elif n==4: 
        plt.text(mu-3*sigma,(P.normpdf(mu, mu, sigma)*1), 'n=481')
        plt.text(mu-3*sigma,(P.normpdf(mu, mu, sigma)*0.8), '$\mu$=80.64')
        plt.text(mu-3*sigma,(P.normpdf(mu, mu, sigma)*0.6), '$\sigma$=0.10')
    
    if n==0:
        plt.title('Crossroad Distribution')
    if n==4:
        plt.xlabel('Number of Cars Passed')    
    
    plt.grid(True)


plt.show()