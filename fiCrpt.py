import math
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder	
from kivy.core.window import Window
import random





kivy.require('1.9.0')

Builder.load_file('fiCrpt.kv')

#Window.size = (1300,600)
Window.maximize()
class MyGridLayout(Widget):

	def Decrypt(self, bin):
		try:

			if bin[0:3] == ">|<":

				bin = bin.replace(">|<","",1)
				deBin = ""
				for i in bin:
					if i == '#' or i =='%' or i =='!' or i =='&' or i == '<' or i =='~':
						i = '0'
					elif i == '*' or i =='^' or i =='$' or i =='?' or i =='@' or i =='(':
						i = '1'
					deBin += i

				b = ""
				bl = []
				text = ""
				ct = 0
				for i in deBin:
					b+= i
					ct +=1
					if ct % 8 == 0:
						bl.append(chr(int(b,2)))
						b = ""
				return text.join(bl)
				print("Decryption Complete!")
			else:
				return "File Already Decrypted!"
		except:
			return "Failed to Decrypt. (Encrypted file might have been tampered with)"


	def Encrypt(self, text):
		try:
			
			if text[0:3] != ">|<":
				fe = ""
				etxt = ""
				netxt = ""
				for i in text:
					e = bin(ord(i))
					e = e.replace('0b','')
					e = list(e)
					while len(e) < 8:
						e.insert(0,'0')
					for j in e:
						fe +=j
					etxt += fe
					fe = ""

				for i in etxt:
					
					if (i == '0'):
						r = random.randint(0,5)
						if r == 0:
							i = "#"
						elif r == 1:
							i = "%"
						elif r == 2:
							i = "!"
						elif r == 3:
							i = "<"
						elif r == 4:
							i = "~"
						else:
							i = "&"
					elif (i == '1'):
						r = random.randint(0,5)
						if r == 0:
							i = "*"
						elif r == 1:
							i = "^"
						elif r == 2:
							i = "$"
						elif r == 3:
							i = "@"
						elif r == 4:
							i = "("
						else:
							i = "?"
					netxt += i

				netxt = netxt.replace("",">|<",1)

				return netxt
				print("Encryption Complete!")

			else:
				return "File Already Encrypted!"

		except:
			return "Failed to Encrypt!"





	def perform(self):
		opty = self.ids.opTy.text
		t = self.ids.tb1.text

		if opty == "Encrypt":
			self.ids.tb2.text = self.Encrypt(t)
		else:
			self.ids.tb2.text = self.Decrypt(t)


					

class fiCrptApp(App):
	def build(self):
		Window.clearcolor = (0.1,.1,0.1,1)
		return MyGridLayout()

if __name__ == '__main__':
	fiCrptApp().run()