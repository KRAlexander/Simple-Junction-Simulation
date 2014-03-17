import numpy as np
import matplotlib.pyplot as plt
import pylab as P

cr =         np.genfromtxt("C:\Users\Alexander\Dropbox\St Georges\Mathematics\Exploration\Crossroad Output.txt")
ra =         np.genfromtxt("C:\Users\Alexander\Dropbox\St Georges\Mathematics\Exploration\Roundabout Output.txt")

def get_average_cr(x):
    number_terms_averaged = x
    number_of_averages = 100000 / number_terms_averaged
    average=np.zeros((number_of_averages,))
    for n in range(number_of_averages):  
        average[n] = np.mean(cr[((number_terms_averaged)*n):(number_terms_averaged*(n+1))])      
    return average

def get_average_ra(x):
    number_terms_averaged = x
    number_of_averages = 100000 / number_terms_averaged
    average=np.zeros((number_of_averages,))
    for n in range(number_of_averages):  
        average[n] = np.mean(ra[((number_terms_averaged)*n):(number_terms_averaged*(n+1))])      
    return average

mu_cr =     np.mean(get_average_cr(5))
sigma_cr =  np.std(get_average_cr(5))
print mu_cr
print sigma_cr
mu_ra =     np.mean(get_average_ra(5))
sigma_ra =  np.std(get_average_ra(5))
print mu_ra
print sigma_ra
plt.text(mu_cr*0.99,P.normpdf(mu_cr,mu_cr,sigma_cr)*1.08, '$\mu=80.64 , \sigma=1.12$',fontsize = 16)      
plt.text(mu_ra*0.99,P.normpdf(mu_ra,mu_ra,sigma_ra)*1.08, '$\mu=76.92 , \sigma=0.81$', fontsize = 16) 

r_detailed = (np.arange(70,85,0.02))

y_cr = P.normpdf(r_detailed, mu_cr, sigma_cr)
line, = plt.plot(r_detailed, y_cr, linewidth=5.0)
line.set_antialiased(True)

y_ra = P.normpdf(r_detailed, mu_ra, sigma_ra)
line, = plt.plot(r_detailed, y_ra, linewidth=5.0)
line.set_antialiased(True)

plt.annotate('Roundabout', xy=(76.6 , 0.48 ), xytext=(74.2 ,0.52 ),
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize = 16
            )
plt.annotate('Crossroad', xy=(81.5 , 0.3 ), xytext=(82.1 ,0.35 ),
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize = 16
            )   
        

        
plt.axis([74,84,0,0.57])

plt.title('Mean Distributions of both Systems Compared, n=5', fontsize=18, fontweight = 'bold')
plt.grid(True)
plt.ylabel('Probability Density')
plt.xlabel('Number of Cars Passed')
plt.show()