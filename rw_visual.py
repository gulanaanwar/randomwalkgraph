import matplotlib.pyplot as plt 

from random_walk import RandomWalk 

#making a random walk
rw = RandomWalk()
rw.fill_walk()

#making the graph
plt.style.use('classic')
fig, ax = plt.subplots()
point_numbers = range(rw.num_points)
ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, 
	edgecolors='none', s=15)

#emphasising the start/end points
ax.scatter(0,0, c='green', edgecolors='none', s=30)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=30)

#removing axes
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()