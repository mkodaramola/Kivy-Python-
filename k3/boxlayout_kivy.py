from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivymd.app import MDApp
from kivy.garden.matplotlib.backend_kivy import FigureCanvasKivy
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


# Sample data
x = [1, 2, 3, 4, 5]  # x-axis values
y = [2, 4, 6, 8, 10]  # y-axis values

# Plot the graph
plt.plot(x, y)

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Graph Example')


class Box(FloatLayout):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		box = self.ids.graphBox
		box.add_widget(FigureCanvasKivy(plt.gcf()))




class MainApp(MDApp):
	def build(self):
		self.theme_cls.theme_style = "Dark"
		self.theme_cls.primary_palette = "BlueGray"
		Builder.load_file('box.kv')
		return Box()


MainApp().run()

