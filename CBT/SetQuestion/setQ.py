import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import FileChooser,FileChooserListView
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.image import Image
import time
#kivy.require('1.9.0')


Window.maximize()



class FirstWindow(Screen):
	
	def sectionNum(self):
		nos = self.ids.nos.text
		nos = nos.replace("Sections","")
		nos = nos.replace("Section","")
		nos = nos.strip()
		print("FirstWindow:",nos)
		fob = open('nos.dat','w')
		fob.write(nos)
		fob.close()

		

	

	

	
	

class SecondWindow(Screen):
	def setPage(self):
		self.clear_widgets()

		
		fob=open('nos.dat','r')
		sr = fob.read()
		r = int(sr)
		print ("SecondWindow:",r)


		bx1 = BoxLayout(orientation='vertical',padding=5)
		popBox = BoxLayout(orientation='vertical')
		FC = FileChooserListView(ids={'fc':'cf'})
		
		popBox.add_widget(FC)
		popup = Popup(title='Choose logo',content=popBox,size_hint=(0.8,0.7))
		

		imgsrc = 'logo/futa_logo.png'

		



		closeBtn = Button(text='Close',size_hint=(None,None),size=(100,50))
		closeBtn.bind(on_press = popup.dismiss)
		popBox.add_widget(closeBtn)

		def pop(this):
			popup.open()
		



		bx3 = BoxLayout(orientation='horizontal',size_hint=(0.3,0.2))
		logoBtn = Button(text='Choose Logo',size_hint=(None,None),size=(100,100),font_size=15)
		logoBtn.bind(on_press=pop)

		logo = Image(source=imgsrc,size_hint=(None,None),size=(100,100))

		bx3.add_widget(logo)
		bx3.add_widget(logoBtn)

		def logoSel(this):
			imgsrc = FC.selection
			logo = Image(source=imgsrc,size_hint=(None,None),size=(100,100))

		FC.bind(on_selection= logoSel)



		sectBox = BoxLayout(orientation="vertical",size_hint=(0.3,0.2))
		sectBox.add_widget(Label(text="How many Questions"))





		
		acc = Accordion(orientation='vertical',min_space=40)
		for i in range(r):
			item= AccordionItem(title=f'Section {chr(65+i)}')
			#item = AccordionItem(background_normal='pic.jpg',background_selected='imageWhenSelected.jpg')
			item.add_widget(Label(text="Yeh! This Owrked"))
			acc.add_widget(item)
		

		bx1.add_widget(bx3)
		bx1.add_widget(acc)


		self.add_widget(bx1)


		
		

class ThirdWindow(Screen):
	pass

class WindowManager(ScreenManager):
	pass



kv = Builder.load_file('setQ.kv')




class mainApp(App):
	def build(self):
		Window.clearcolor = (0.21,0.4,0.21,1)
		return kv

if __name__ == '__main__':
	mainApp().run()
