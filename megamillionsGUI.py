"""
Program: GUItemplate.py
Author: Jessica 6/2/2022

GUI app that draws 5 random numbers between 1 and 70. It includes a 6th Megaball which is only between 1 and 25
"""

from breezypythongui import EasyFrame
import random

class megamillionsGUI(EasyFrame):
	# "ApplicationName" will change from project ot project

	# definiton of the __init__() method which is our class constructor
	def __init__(self):
		# call the EasyFrame version of __init__
		EasyFrame.__init__(self, title = "Play Mega Millions", resizable = "false")
		self.title = self.addLabel(text = "PLAY MEGA MILLIONS", row = 0, column = 0, columnspan = 2, background = "yellow", foreground="lightseagreen", sticky="NEW")

		self.drawOutput1 = self.addIntegerField(value = 0, row = 1, column = 0, state = "readonly")
		self.drawOutput2 = self.addIntegerField(value = 0, row = 1, column = 1, state = "readonly")
		self.drawOutput3 = self.addIntegerField(value = 0, row = 1, column = 2, state = "readonly")
		self.drawOutput4 = self.addIntegerField(value = 0, row = 1, column = 3, state = "readonly")
		self.drawOutput5 = self.addIntegerField(value = 0, row = 1, column = 4, state = "readonly")
		self.megaBallOutput = self.addIntegerField(value = 0, row = 1, column = 5, state = "readonly")

		self.drawButton = self.addButton(text = "DRAW!", row = 3, column = 0, columnspan = 2, command = self.draw)

	def draw(self):
		draw1 = random.randint(1, 70)
		draw2 = random.randint(1, 70)
		draw3 = random.randint(1, 70)
		draw4 = random.randint(1, 70)
		draw5 = random.randint(1, 70)
		megaBall = random.randint(1, 25)

		self.drawOutput1.setNumber(draw1)
		self.drawOutput2.setNumber(draw2)
		self.drawOutput3.setNumber(draw3)
		self.drawOutput4.setNumber(draw4)
		self.drawOutput5.setNumber(draw5)
		self.megaBallOutput.setNumber(megaBall)
		
# definition of the main method which will establish class objects
def main():
	# instantiate an object from the class into mainloop()
	megamillionsGUI().mainloop()

#global call to the main() method
main()