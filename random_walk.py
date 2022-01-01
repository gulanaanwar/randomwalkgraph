from random import choice

class RandomWalk():
	"""Generating a graph for a random walk"""

	def __init__(self, num_points=5000):
		"""initializing attributes of the walk"""
		self.num_points = num_points

		#starting each walk at 0,0
		self.x_values = [0]
		self.y_values = [0]

	def get_step(self):
		"""Calculating each new step"""
		direction = choice([1, -1])
		distance = choice([0, 1, 2, 3, 4])
		step = direction * distance
		return step

	def fill_walk(self):
		"""Calculating new distance relatvie to 0,0"""
		while len(self.x_values) < self.num_points:

			x_step = self.get_step()
			y_step = self.get_step()

			if x_step == 0 and y_step == 0:
				continue

			x = self.x_values[-1] + x_step
			y = self.y_values[-1] + y_step

			self.x_values.append(x)
			self.y_values.append(y)
