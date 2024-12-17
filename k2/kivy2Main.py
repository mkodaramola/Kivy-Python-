import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

kivy.require('1.9.0')

Builder.load_file('nl.kv')

class MyGridLayout(Widget):
	name = ObjectProperty(None)
	snack = ObjectProperty(None)
	colour = ObjectProperty(None)

	def press(self):
		name = self.name.text
		colour = self.colour.text
		snack = self.snack.text

		print(f"Hello, {name}, you love {snack} and your best colour is {colour}")

		self.name.text = ""
		self.colour.text = ""
		self.snack.text = ""






class null(App):
	def build(self):
		return MyGridLayout()


	
		

if __name__ == '__main__':
	null().run()	
