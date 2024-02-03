from scipy.stats import pearsonr

x_data = '1,2,3,4,5'
y_data = '2,4,6,8,10'

# Assuming x and y are your input data as strings
x = [float(val) for val in x_data.split(',')]
y = [float(val) for val in y_data.split(',')]

# Calculate Pearson correlation coefficient and p-value
correlation_coefficient, p_value = pearsonr(x, y)

print(f"Pearson correlation coefficient: {correlation_coefficient}")
print(f"P-value: {p_value}")
