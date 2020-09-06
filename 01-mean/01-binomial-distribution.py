"""
rating

! what?
TB rates the same stuff for different scores.
- 10 out of 10, 100% recommendation
- 48 out of 50, 96% recommendation
- 186 out of 200, 93% recommendation

if all socres are authentic(NOT rigged), which one is your best choice?

! why?
Laplace's rule of succession

The Rule of Succession gives a simple formula for “enumerative induction”: 
reasoning from observed instances to unobserved ones. 

If you’ve observed 8 ravens and they’ve all been black, 
how certain should you be the next raven you see will also be black? 
According to the Rule of Succession, 90%. 

In general, the probability is (k+1)/(n+2) that the next observation will be positive,
given k positive observations out of n total.

! how?
how to read a rating?
(k+1)/(n+2)

P(k=48, b=2|s=0.95) = (50 48)(0.95)^48(1-0.95)^2
=> Binomial Distribution
NOTE: P(data|success rate) -> P(success rate|data)

"""
import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def read_rating(k: int, n: int) -> float:
    _k = 1
    _n = 2
    if not k and not n:
        raise ValueError('k or n must be > 0')
    else:
        return (k + _k) / (n + _n)



if __name__ == "__main__": 
    ratings = [
        (10, 10),
        (48, 50),
        (186, 200),
    ]
    for rating in ratings:
        r = read_rating(*rating)
        logging.debug(f'10 out of 10, means {r:.1%} success rate') 