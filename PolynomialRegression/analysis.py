import numpy as np
import matplotlib.pyplot as plt

regression_methods = ["Linear", "Quadratic", "Cubic"]
r2_scores = [0.942251, 0.942252, 0.943709]
complexities = [2, 3, 3] 

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.bar(regression_methods, r2_scores, color=['red', 'green', 'blue'], alpha=0.8)
plt.title("R² Scores for Regression Methods", fontsize=14)
plt.ylabel("R² Score", fontsize=12)
plt.ylim(0.94, 0.945)
plt.grid(axis='y', linestyle='--', alpha=0.3)

plt.subplot(1, 2, 2)
plt.bar(regression_methods, complexities, color=['red', 'green', 'blue'], alpha=0.8)
plt.title("Computational Complexity (Order of Growth)", fontsize=14)
plt.ylabel("Complexity (O)", fontsize=12)
plt.xticks(fontsize=10)
plt.yticks([2, 3], ["O(n²)", "O(n³)"], fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.3)

plt.tight_layout()
plt.show()
