from PIL import Image, ImageDraw
import random

class avatar:
	def __init__(self, size=350):
		self.gc = size//7 #grid square cell size.
		self.image = Image.new(
			mode='RGBA', 
			size=(size,)*2, 
			color='white'
		)
		self.draw = ImageDraw.Draw(self.image)
		self.drawPattren()
		self.save()

	def drawPattren(self):
		'''
			draw pattren.
		'''
		grid = self.genGrid()
		color = self.genColor()
		for x in range(5):
			for y in range(5):
				value = grid[x][y]
				if value:
					self.drawCell(coor=(y,x), color=color)

	def genGrid(self):
		'''
			generate 5x5 random grid.
		'''
		while True:
			edge = [
				random.choices(range(2),k=5),
				random.choices(range(2),k=5)
			]
			middle = random.choices(range(2),k=5)
			if True:
				break
		grid = list(zip(*edge, middle, *edge[::-1]))
		return grid

	def genColor(self):
		'''
			generate color.
		'''
		return (
			random.randint(50,255),
			random.randint(50,255), 
			random.randint(50,255)
		)

	def drawCell(self, coor=(0, 0), color='black'):
		'''
			draw a square.
		'''
		self.draw.rectangle(
			xy=[
				self.gc+coor[0]*self.gc,
				self.gc+coor[1]*self.gc,
				self.gc+coor[0]*self.gc+self.gc,
				self.gc+coor[1]*self.gc+self.gc
			],
			fill=color,
			width=2
		)

	def save(self):
		self.image.save(f'avatar {random.randint(1,1000)}.png')

	def show(self):
		self.image.show()

if __name__=='__main__':
	avatar()
	#avatar().show() #generate and show.
