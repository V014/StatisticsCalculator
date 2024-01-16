import statistics # The standard python class

data = [2,4,2,3,6,1] # values in use
sample_std = statistics.stdev(data) # to calculate standard deviation for a sample
population_std = statistics.pstdev(data) # to calculate standard deviation for a population

print('Sample standard deviation:', sample_std) # display the result
print('Population standard deviation:', population_std) # display the result