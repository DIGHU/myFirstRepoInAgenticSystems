# Import libraries
import numpy as np
import matplotlib.pyplot as plt

# 1. Create epochs list (1 to 10)
epochs = list(range(1, 11))

# 2. Generate synthetic training loss values
np.random.seed(42)
loss = np.linspace(1.0, 0.2, 10) + np.random.rand(10) * 0.1

# 3A. Line Plot (Loss vs Epoch)
plt.figure(figsize=(8,5))
plt.plot(epochs, loss, marker='o')
plt.title("Loss vs Epoch (Line Plot)")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.grid(True)
plt.show()

# 3B. Scatter Plot (Epoch vs Loss)
plt.figure(figsize=(8,5))
plt.scatter(epochs, loss)
plt.title("Epoch vs Loss (Scatter Plot)")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.grid(True)
plt.show()

# 4. Bar Chart (Model Accuracy)
models = ['Model A', 'Model B', 'Model C']
accuracy = [0.85, 0.90, 0.88]

plt.figure(figsize=(8,5))
plt.bar(models, accuracy)
plt.title("Model Accuracy Comparison")
plt.xlabel("Models")
plt.ylabel("Accuracy")
plt.show()