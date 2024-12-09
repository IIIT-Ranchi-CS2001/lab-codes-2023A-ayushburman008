import matplotlib.pyplot as plt

# Data
mp_results = {'BJP': 163, 'INC': 66, 'BSP': 0, 'Others': 1}
rajasthan_results = {'INC': 69, 'BJP': 115, 'BSP': 2, 'Others': 13}

# Calculate percentages for pie charts
def calculate_percentages(results):
    total = sum(results.values())
    return {party: (seats / total) * 100 for party, seats in results.items()}

mp_percentages = calculate_percentages(mp_results)
rajasthan_percentages = calculate_percentages(rajasthan_results)

# Plot pie charts with highest percentage party detached
def plot_pie_with_highlight(ax, percentages, title):
    labels = percentages.keys()
    sizes = percentages.values()
    explode = [0.1 if p == max(sizes) else 0 for p in sizes]
    wedges, texts, autotexts = ax.pie(
        sizes,
        labels=labels,
        explode=explode,
        autopct='%1.1f%%',
        startangle=140,
        textprops={'fontsize': 10}
    )
    ax.set_title(title, fontsize=14)

# Create subplots for pie charts
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
plot_pie_with_highlight(ax1, mp_percentages, "Madhya Pradesh 2023")
plot_pie_with_highlight(ax2, rajasthan_percentages, "Rajasthan 2023")
plt.tight_layout()
plt.show()

# Bar chart for seat comparison
fig, ax = plt.subplots(figsize=(10, 6))
parties = list(set(mp_results.keys()).union(set(rajasthan_results.keys())))
mp_seats = [mp_results.get(party, 0) for party in parties]
rajasthan_seats = [rajasthan_results.get(party, 0) for party in parties]

x = range(len(parties))
ax.bar(x, mp_seats, width=0.4, label="Madhya Pradesh", align='center')
ax.bar([i + 0.4 for i in x], rajasthan_seats, width=0.4, label="Rajasthan", align='center')

# Customize bar chart
ax.set_xticks([i + 0.2 for i in x])
ax.set_xticklabels(parties)
ax.set_ylabel('Seats Won')
ax.set_xlabel('Party')
ax.set_title('Assembly Election Results 2023')
ax.legend()
plt.tight_layout()
plt.show()
