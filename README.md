# Metropolis-Hastings-MCMC

Simple implementation of Bayesian models in Markov Chain Monte Carlo algorithm development.

# About bayes theorem

Bayes formula:

![alt text](https://wikimedia.org/api/rest_v1/media/math/render/svg/87c061fe1c7430a5201eef3fa50f9d00eac78810)

Two events A and B are given. This formula shows conditional probability of A given B (B must be true and P(B) not equal to 0).

P(A) is the prior probability of A before any data is taken into account. It is independent of B. 

P(B/A) is the probability of event B happening given A is true.

P(A/B) is the probability of event A occuring given B is true .

Posterior is proportional to:

![alt text](https://wikimedia.org/api/rest_v1/media/math/render/svg/e1a83fc9b2788b4a72bbc4c90d06c67bb7e0fdae)

The maximum a posteriori is the mode (value that apperas the most often in data set) of the posterior and is usually calculated using mathemtical optimazation.

MCMC enables us to approximate posterior even without calcualting P(B).

# Monte Carlo method

It relies on repeated random sampling to achieve some numerical results.

Monte Carlo method is widely used to work with probability distribution , but also integration and optimazation.

# Markov Chain
Markov Chain is a sequence ("chain") in which probability of the event depends only on the state of the previous event.

# Markov Chain Monte Carlo 
It is used in sampling from probaility distribution and connects both methods presented above.

By creating a markov chain we can get a sample from desired distribution after number of steps in the right direction (accepting and rejecting values explained below). The more the steps , the closer distribution of our sample is to desired distribution.

# Functions used in the algorithm

θ
prop is our candidate step. The Metropolis algorithm calls for
θ
prop
to be sampled from a symmetric proposal distribution centered at the current parameter value,
θ
curr.

θ
prop
∼
Normal
(
θ
curr
,σ
2)

Normal distribution as proposal distribution and sigma squared as standard deviation.

The proposal distribution’s sole purpose is to give candidate parameter values to
try
and
potentially accept as a valid sample from the posterior distribution of
θ.

p
(
accept θ
prop
) =
min
(
Bayes
′
numerator at θ
prop
Bayes
/
numerator at θ
curr
,
1
.
0)

Function that decides whether to accept or reject θ
prop.

Bayes’ numerator is simply the product of the likelihood,
l
(
Data
|
θ
)
, and the prior distribution,
p
(
θ
).

p
(
accept θ
prop
) =
min
(
l
(
Data
|
θ
prop
)
p
(
θ
prop
)
/
l
(
Data
|
θ
curr
)
p
(
θ
curr
)
,
1
.
0)
