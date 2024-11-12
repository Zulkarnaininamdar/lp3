import numpy as np
import matplotlib.pyplot as plt

# Define the function y = (x + 3)^2
def f(x):
    return (x + 3)**2

# Define the gradient of the function f(x) = 2 * (x + 3)
def gradient(x):
    return 2 * (x + 3)

# Gradient descent algorithm
def gradient_descent(starting_x, learning_rate, num_iterations):
    x = starting_x
    x_values = [x]  # Track x values for visualization
    y_values = [f(x)]  # Track function values for visualization
    
    for i in range(num_iterations):
        grad = gradient(x)  # Calculate the gradient at the current point
        x = x - learning_rate * grad  # Update x by moving opposite to the gradient
        x_values.append(x)
        y_values.append(f(x))
    
        # Stop if the change in x is very small (convergence)
        if abs(grad) < 1e-6:
            break
    
    return x, x_values, y_values

# Parameters for gradient descent
starting_x = 2  # Initial point
learning_rate = 0.1  # Learning rate
num_iterations = 50  # Number of iterations

# Perform gradient descent
min_x, x_values, y_values = gradient_descent(starting_x, learning_rate, num_iterations)

# Print the result
print(f"The local minimum occurs at x = {min_x}, f(x) = {f(min_x)}")

# Plotting the function and the gradient descent path
x_plot = np.linspace(-6, 4, 100)
y_plot = f(x_plot)

plt.figure(figsize=(10, 6))
plt.plot(x_plot, y_plot, label="y = (x + 3)^2", color="blue")
plt.scatter(x_values, y_values, color="red", label="Gradient Descent Steps")
plt.plot(x_values, y_values, color="red", linestyle="--", alpha=0.6)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Gradient Descent on f(x) = (x + 3)^2")
plt.legend()
plt.grid(True)
plt.show()
