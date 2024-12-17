import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.tabbedpanel import TabbedPanel


#kivy.require('1.9.0')

Window.maximize()



Builder.load_file('main.kv')
	
class Tab(TabbedPanel):
	pass

class myLayout(Widget):
	def sectBtn(self,id):
		print(f"Button Pressed",id.text)


		
					

class mainApp(App):
	def build(self):
		Window.clearcolor = (0.21,0.4,0.21,1)
		return myLayout()

if __name__ == '__main__':
	mainApp().run()
