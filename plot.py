import matplotlib.pyplot as plt
import numpy as np

# Data: Hypothetical life expectancy improvements based on policy changes
policies = ['Increase Unemployment Benefits', 'Universal Healthcare Access', 'Stronger Job Training Programs', 'Higher Welfare Spending']
current_life_expectancy = [77.8, 77.8, 77.8, 77.8]  # Baseline U.S. life expectancy
improved_life_expectancy = [79.5, 81.2, 79.0, 81.6]  # Hypothetical improvements

# Set up the position of the bars
x = np.arange(len(policies))

# Width of the bars
width = 0.35

# Creating the figure
plt.figure(figsize=(10, 6))

# Plotting the bars
plt.bar(x - width/2, current_life_expectancy, width, label='Current Life Expectancy', color='blue')
plt.bar(x + width/2, improved_life_expectancy, width, label='Improved Life Expectancy with Policies', color='green')

# Adding titles and labels
plt.title('Impact of Policy Changes on U.S. Life Expectancy', fontsize=16)
plt.xlabel('Policy Changes', fontsize=12)
plt.ylabel('Life Expectancy (Years)', fontsize=12)
plt.xticks(x, policies, rotation=15)
plt.legend()
plt.grid(axis='y')

plt.ylim(74, max(improved_life_expectancy) + 1)

# Displaying the graph
plt.tight_layout()  # Adjust layout to fit labels
plt.show()
