import statistics as st# The standard python class
import matplotlib.pyplot as pp

x = [2,4,2,3,6,1] # values in use

m = st.mean(x) # to calculate mean
sample_std = st.stdev(x) # to calculate standard deviation for a sample
population_std = st.pstdev(x) # to calculate standard deviation for a population
population_variance = st.pvariance(x) # to calculate population variance


print('Sample standard deviation:', sample_std) # display the result
print('Population standard deviation:', population_std) # display the result