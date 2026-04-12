import matplotlib.pyplot as plt

labels = ['No Failure', 'Failure']
values = [85, 15]

plt.bar(labels, values)
plt.title("Machine Failure Distribution")
plt.savefig("outputs/failure_graph.png")
plt.show()