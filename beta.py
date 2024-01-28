import statistics as st# The standard python class
import matplotlib.pyplot as pp

x = [76,84,69,92,58,89,73,97,85,77] # values in use

mean = st.mean(x) # to calculate mean
sample_std = st.stdev(x) # to calculate standard deviation for a sample
population_std = st.pstdev(x) # to calculate standard deviation for a population
sample_variance = st.variance(x) # to calculate variance
population_variance = st.pvariance(x) # to calculate population variance
standard_deviations = tuple(x-mean for x in x)
variances = tuple(x*x for x in standard_deviations)

# display the results
print('Mean:', mean)
print('Sample standard deviation:', sample_std) 
print('Population standard deviation:', population_std)
print('Sample variance:', sample_variance)
print('Population variance:', population_variance)
print('Standard deviations:', standard_deviations)
print('Variances:', variances)
pp.bar(tuple(str(x) for x in x), standard_deviations)