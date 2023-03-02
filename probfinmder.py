import scipy.stats as stats

# prompt the user for the problem type and input values
print("Choose a problem type:")
print("1. Find P(Z < z)")
print("2. Find P(Z > z)")
print("3. Find P(z1 < Z < z2)")
problem_type = int(input("Enter the problem type: "))
z1 = None
z2 = None
if problem_type == 1 or problem_type == 2:
    z = float(input("Enter z: "))
elif problem_type == 3:
    z1 = float(input("Enter lower bound z1: "))
    z2 = float(input("Enter upper bound z2: "))
else:
    print("Invalid problem type")
    exit()

# calculate the probability based on the problem type and input values
if problem_type == 1:
    prob = stats.norm.cdf(z)
elif problem_type == 2:
    prob = 1 - stats.norm.cdf(z)
elif problem_type == 3:
    prob = stats.norm.cdf(z2) - stats.norm.cdf(z1)

# print the result
print(f"The probability is {prob:.4f}")
