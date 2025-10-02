import matplotlib.pyplot as plt
import numpy as np

# Data
months = ["07/2019", "08/2019", "09/2019", "10/2019", "11/2019"]
searches = [50, 53, 50, 56, 62]
direct = [39, 47, 42, 51, 51]
social = [70, 80, 90, 87, 92]

x = np.arange(len(months))  # positions for groups
width = 0.25  # bar width

# Plot
fig, ax = plt.subplots(figsize=(8,6))

bars1 = ax.bar(x - width, searches, width, label='Searches', color='skyblue')
bars2 = ax.bar(x, direct, width, label='Direct', color='violet')
bars3 = ax.bar(x + width, social, width, label='Social Media', color='gold')

# Labels and title
ax.set_ylabel("Visitors (in thousands)")
ax.set_title("Visitors by Web Traffic Sources")
ax.set_xticks(x)
ax.set_xticklabels(months)
ax.legend()

# Add value labels on bars
def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}',
                    xy=(bar.get_x() + bar.get_width()/2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

add_labels(bars1)
add_labels(bars2)
add_labels(bars3)

plt.tight_layout()
plt.show()
