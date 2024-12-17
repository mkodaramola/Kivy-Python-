import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

kivy.require('1.9.0')

Builder.load_file('inherit.kv')


class MyGridLayout(Widget):
	pass


class myApp(App):
	def build(self):
		return MyGridLayout()

if __name__ == '__main__':
	myApp().run()

