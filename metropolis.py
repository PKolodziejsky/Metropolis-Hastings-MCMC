import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np


#data
x=100
y=40
a = 2
b=2

#pseudo random numbers generators
np.random.seed(1)
random= np.random.uniform(0,1)


# number of samples and length of markov chain , theta seed to start with , standard deviation
def metropolis(samples_num ,theta_seed ,sd ):

    theta_curr =theta_seed

    posterior_thetas =[]

    for i in range(1,samples_num):
        theta_prop = stats.norm(theta_curr,sd).rvs()

        #if proposed parameter is outside the range , set it equal to current value, otherwise keep it
        if(theta_prop<0 or theta_prop>1):
            theta_prop = theta_curr
        else:
            theta_prop = theta_prop

        #Bayes numerators
        posterior_prop = stats.beta.pdf(theta_prop ,a ,b)*np.random.binomial(n=y , p=theta_prop , size =x)
        posterior_curr = stats.beta.pdf(theta_curr ,a ,b)*np.random.binomial(n=y ,p=theta_curr , size=x)

        #Propability of accepting
        accept_theta_prop = min(1.0, posterior_prop.any()/posterior_curr.any())

        if (accept_theta_prop>random):
            theta_select = theta_prop
        else:
            theta_select = theta_curr

        posterior_thetas.append(theta_select)

        theta_curr = theta_select

    return posterior_thetas

run = metropolis(200 , 0.9, 0.05)


plt.subplot().plot(run)
plt.subplot().set(title="Random walk with standard deviation 0.05" , xlabel ="Number of samples" ,ylabel ="Theta")
plt.show()