
from kivy.lang import Builder
from kivymd.app import MDApp





#kivy.require('1.9.0')



	

class MyApp(MDApp):
	def build(self):
		self.theme_cls.theme_style = "Light"
		self.theme_cls.primary_palette = "Amber"
		self.theme_cls.accent_palette = "Red"
		return Builder.load_file('main.kv')


MyApp().run()

