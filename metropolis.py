import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#data
x=47
y=17
a =2
b=2

#pseudo random numbers generators

random= np.random.uniform(0,1)
np.random.seed(1)

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
        posterior_prop = stats.beta(a,b).pdf(theta_prop)*stats.binom(n=x,p=theta_prop).pmf(y)
        posterior_curr = stats.beta(a,b).pdf(theta_curr)*stats.binom(n=x,p=theta_curr).pmf(y)

        #Propability of accepting
        accept_theta_prop = min(1.0, posterior_prop/posterior_curr)

        if (accept_theta_prop>random):
            theta_select = theta_prop
        else:
            theta_select = theta_curr

        posterior_thetas.append(theta_select)

        theta_curr = theta_select


    return posterior_thetas

run = metropolis(10000, 0.9, 0.05)

#First plot for kde and the other one for markov chain represantation
plt.figure(1)
sns.kdeplot(run)
plt.subplot().set(title="Kernel density for theta" , ylabel = "Density" , xlabel = "Theta")


plt.figure(2)
plt.subplot().plot(run)
plt.subplot().set(title="Markov Chain with standard deviation 0.05" , xlabel ="Number of samples" ,ylabel ="Theta")

plt.show()