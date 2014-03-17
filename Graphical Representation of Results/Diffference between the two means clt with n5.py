import numpy as np
import matplotlib.pyplot as plt
import pylab as P


cr = np.genfromtxt("C:\Users\Alexander\Dropbox\St Georges\Mathematics\Exploration\Crossroad Output.txt")


ra = np.genfromtxt ("C:\Users\Alexander\Dropbox\St Georges\Mathematics\Exploration\Roundabout Output.txt")

diff = cr - ra


def get_average(x):
    number_terms_averaged = x
    number_of_averages = 100000 / number_terms_averaged
    average=np.zeros((number_of_averages,))
    for n in range(number_of_averages):  
        average[n] = np.mean(diff[((number_terms_averaged)*n):(number_terms_averaged*(n+1))])      
    return average



average = get_average(5)
plt.text(75,0.45, "n=5")
mu = np.mean(average)
sigma = np.std(average)

print mu
print sigma
print (sigma*sigma)


r_detailed = (np.arange(-3,0.001,0.0005))
#plt.hist(average, bins=r, normed = 1)
y = P.normpdf(r_detailed, mu, sigma)
plt.plot(r_detailed, y, linewidth=3.0, color = 'r')

fill = r_detailed
y_fill = P.normpdf(fill, mu, sigma)
plt.fill_between(fill,y_fill, y2=0, where=None, color = 'r')

r_detailed = (np.arange(0,10,0.001))
#plt.hist(average, bins=r, normed = 1)
y = P.normpdf(r_detailed, mu, sigma)
plt.plot(r_detailed, y, linewidth=3.0, color = 'g')

fill = r_detailed
y_fill = P.normpdf(fill, mu, sigma)
plt.fill_between(fill,y_fill, y2=0, where=None, color = 'g')

plt.plot( [mu , mu], [0,P.normpdf(mu,mu,sigma)],'m--',  linewidth=4.0)

plt.axis([mu-3.5*sigma,mu+3.5*sigma,0,P.normpdf(mu,mu,sigma)*1.2])

plt.text(mu*0.71,0.31, r'$\mu=3.72, \ \sigma =1.38 $', fontsize = 15)

plt.title('Distribution of Mean Difference = Cr - Ra, n=5 ')
plt.grid(True)
plt.ylabel('Probability Density')
plt.xlabel('Number of Cars Passed')
plt.show()