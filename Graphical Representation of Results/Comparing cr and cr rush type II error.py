import numpy as np
import matplotlib.pyplot as plt
import pylab as P

cr_rush = np.genfromtxt("C:\Users\Alexander\Dropbox\St Georges\Mathematics\Exploration\crossroads_analytics_rush.txt")
cr = np.genfromtxt("C:\Users\Alexander\Dropbox\St Georges\Mathematics\Exploration\Crossroad Output.txt")

"""
        b: blue
        g: green
        r: red
        c: cyan
        m: magenta
        y: yellow
        k: black
        w: white

"""



numberterms=5
bingraduation = 0.4
linewidths = 1.0

def get_average_cr(x,ram):
    number_terms_averaged = x
    number_of_averages = 100000 / number_terms_averaged
    average=np.zeros((number_of_averages,))
    for n in range(number_of_averages):  
        average[n] = np.mean(ram[((number_terms_averaged)*n):(number_terms_averaged*(n+1))])      
    return average

def get_average_cr_rush(x,ram):
    number_terms_averaged = x
    number_of_averages = 16410 / number_terms_averaged
    average=np.zeros((number_of_averages,))
    for n in range(number_of_averages):  
        average[n] = np.mean(ram[((number_terms_averaged)*n):(number_terms_averaged*(n+1))])      
    return average


average = get_average_cr_rush(numberterms,cr_rush)
mu_rush = np.mean(average)
sigma_rush = np.std(average)
r_detailed = (np.arange(70,90,0.001))
y = P.normpdf(r_detailed, mu_rush, sigma_rush)
plt.plot(r_detailed, y, linewidth=linewidths, color = 'b')


print "CR Rush"
print mu_rush
print sigma_rush
print sigma_rush**2


average = get_average_cr(numberterms,cr)
mu_cr = np.mean(average)

print "CR"
print mu_cr


plt.plot([((mu_rush+mu_cr)/2),((mu_rush+mu_cr)/2)], [0,P.normpdf(((mu_rush+mu_cr)/2),((mu_rush+mu_cr)/2), sigma_rush)],'b--',  linewidth=3.0)

            
mu_p=((mu_rush+mu_cr)/2)   

r_detailed = (np.arange(82.5000,90,0.0001))  
y = P.normpdf(r_detailed, mu_p, sigma_rush)
plt.plot(r_detailed, y, linewidth=6, color = 'r')
r_detailed = (np.arange(70,82.5000,0.0001))  
y = P.normpdf(r_detailed, mu_p, sigma_rush)
plt.plot(r_detailed, y, linewidth=6, color = 'g')

fill = (np.arange(82.4999,90,0.0001))
y_fill = P.normpdf(fill, mu_p, sigma_rush)
plt.fill_between(fill,y_fill, y2=0, where=None, color = 'r')

fill = (np.arange(70,82.5000,0.0001))
y_fill = P.normpdf(fill, mu_p, sigma_rush)
plt.fill_between(fill,y_fill, y2=0, where=None, color = 'g')

plt.annotate('Proposed Actual Mean, $\mu_1 = 82.26$', xy=(mu_p , P.normpdf(mu_p,mu_p,sigma_rush)), 
             xytext=(mu_p*0.967 , P.normpdf(mu_p,mu_p,sigma_rush)+0.07),
            arrowprops=dict(facecolor='black', shrink=0.1),
            )
            
plt.annotate('CR Rush: $(\mu = 83.93 , \sigma = 0.869)$', xy=(mu_rush , P.normpdf(mu_rush,mu_rush,sigma_rush)),
             xytext=(mu_rush*0.988 , P.normpdf(mu_rush,mu_rush,sigma_rush)*1.3),
            arrowprops=dict(facecolor='black', shrink=0.1),
            )


plt.annotate('Type II Error = 0.391 ', xy=(83.05 , 0.166), xytext=(83.72, 0.274),
            arrowprops=dict(facecolor='black', shrink=0), fontsize = 15
            )
            
plt.annotate('Lower Bound = 82.5', xy=(82.5 , 0.55), xytext=(80, 0.55),
            arrowprops=dict(facecolor='black', shrink=0.1),
            )
            
plt.annotate('Upper Bound = 85.4', xy=(85.4 , 0.25), xytext=(86, 0.29),
            arrowprops=dict(facecolor='black', shrink=0.1),
            )
            
            
plt.plot([85.36,85.36], [0,1],'m--',  linewidth=4.0)
plt.plot([82.5,82.5], [0,1],'m--',  linewidth=4.0)

plt.axis([77.3,88.4,0,0.61])

plt.title('Comparing All Distributions, CLT n=5')
plt.grid(True)
plt.ylabel('Relative Frequency')
plt.xlabel('Number of Cars Passed')
plt.show()