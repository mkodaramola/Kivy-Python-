import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

#kivy.require('1.9.0')

Builder.load_file('layout.kv')

class MyGridLayout(Widget):
	pass			

class MyApp(App):
	def build(self):
		Window.clearcolor = (1,1,1,0)
		return MyGridLayout()

if __name__ == '__main__':
	MyApp().run()

