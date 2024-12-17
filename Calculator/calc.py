import math
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

kivy.require('1.9.0')

Builder.load_file('calc.kv')

Window.size = (400,600)
new = False

dot = False
class MyGridLayout(Widget):



	def compute(self):
		try:
			global new
			text = self.ids.calc_input.text
			text = text.replace('x','*')
			text = text.replace(')(','*')
			text = text.replace('^','**')
			text = text.replace('pi','math.pi')
			text = text.replace('sqrt(','math.sqrt(')


			ans = eval (text)

			self.ids.calc_input.text = str(round(ans,10))
		
			new = True
		except:
			self.ids.calc_input.text = "Error"	
		


	

	
	def clear(self):
		global new
		text = '0'
		self.ids.calc_input.text=text
		new = False

	def inverse(self):
		try:
			text = self.ids.calc_input.text

			text = text.replace('x','*')
			text = text.replace('^','**')
			text = text.replace('pi','math.pi')
			text = text.replace('sqrt(','math.sqrt(')

			ans = eval(text)

			self.ids.calc_input.text = str(round(1/ans,10))
		except:
			self.ids.calc_input.text = "Error"


	
		
	def _numPress(self,n):

		try:

			global new
			global dot
			

			if n == 'x' or n == '+' or n == '-' or n == '/' or n == '^':
				dot = False

			

			if (new == True) and (n != 'x' and n != '+' and n != '-' and n != '/' and n != '^'):
				self.ids.calc_input.text = ""


			text = self.ids.calc_input.text	
			if text.startswith('0') and (n != '.'):
				text = text.replace('0','',1)





			if dot == True and n == '.':
				n = ""
				pass

			else:
				
				if n == "abs(" and text != "" and ('x' not in text and '+' not in text and '-' not in text and '/' not in text and '^' not in text):
					text = f'abs({text})'
				elif n == "sqrt(" and text != "" and ('x' not in text and '+' not in text and '-' not in text and '/' not in text and '^' not in text):
					text = f'sqrt({text})'
				elif n == "(" and text != "" and ('x' not in text and '(' not in text and '+' not in text and '-' not in text and '/' not in text and '^' not in text):
					text = f'({text}'
					
				else:
					text+=str(n)
				self.ids.calc_input.text=text

			if n == '.':
				dot = True

			new = False
		except:
			self.ids.calc_input.text = "Error"

	def _pORm(self):
		try:
			text = self.ids.calc_input.text
			text = text.replace('x','*')
			text = text.replace('^','**')
			text = text.replace('pi','math.pi')
			text = text.replace('sqrt(','math.sqrt(')

			if 'x' in text or '+' in text or (text.count('-') > 1) or '/' in text:
				pass
			else:
				text = f'-{text}'
				ans = eval(text)
				self.ids.calc_input.text = str(ans)
		except:
			self.ids.calc_input.text = "Error"


	def percent(self):
		try:
			text = self.ids.calc_input.text
			if (float(text) > 1.0 or float(text) < -1.0):
				pass
			else:
				self.ids.calc_input.text = str(round(float(text)*100,10))
		except:
			self.ids.calc_input.text = "Error"





		
	def backspace(self):
		try:
			global new
			text = self.ids.calc_input.text
			if text.startswith('0'):
				text = text.replace('0','',1)
			text = text[:-1]
			self.ids.calc_input.text=text

			new = False	
		except:
			self.ids.calc_input.text = "Error"				

class CalculatorApp(App):
	def build(self):
		Window.clearcolor = (0.9,.9,0.9,1)
		return MyGridLayout()

if __name__ == '__main__':
	CalculatorApp().run()






# def compute(self,s):
# 		global new
# 		global init_n
# 		global init_operator

# 		def lastSign(t):
# 			nt = list(t)
# 			nt.reverse()
# 			ct = 0
# 			for i in nt:
# 				if i == 'x' or i == '+' or i == '-' or i == '/':
# 					break
# 				ct+=1
# 			return len(t)-(ct+1)

# 		if (s == '+' or s=='-') and new == True:
# 			init_n = 0
# 		elif (s=='x' or s=='/') and new == True:
# 			init_n = 1

# 		text = self.ids.calc_input.text


# 		if s == '+':
		
# 			if lastSign(text) != -1:
# 				t = text[lastSign(text)+1:]
# 			else:
# 				t = text

# 			if init_operator == '+':
# 				init_n += float(t)
# 			elif init_operator == '-':
# 				init_n -= float(t)
# 			elif init_operator == 'x':
# 				init_n *= float(t)
# 			elif init_operator == '/':
# 				init_n /= float(t)

# 			init_operator = '+'

# 		elif s == '=':
# 			if lastSign(text) != -1:
# 				t = text[lastSign(text)+1:]
# 			else:
# 				t = text
			

# 			if init_operator == '+':
# 				init_n += float(t)
# 			elif init_operator == '-':
# 				init_n -= float(t)
# 			elif init_operator == 'x':
# 				init_n *= float(t)
# 			elif init_operator == '/':
# 				init_n /= float(t)

# 			init_operator = '+'
			
# 		elif s == '-':
# 			if lastSign(text) != -1:
# 				t = text[lastSign(text)+1:]
# 			else:
# 				t = text
			

# 			if init_operator == '+':
# 				init_n += float(t)
# 			elif init_operator == '-':
# 				init_n -= float(t)
# 			elif init_operator == 'x':
# 				init_n *= float(t)
# 			elif init_operator == '/':
# 				init_n /= float(t)

# 			init_operator = '-'


# 		elif s == 'x':
# 			if lastSign(text) != -1:
# 				t = text[lastSign(text)+1:]
# 			else:
# 				t = text
			
# 			if init_operator == '+':
# 				init_n += float(t)
# 			elif init_operator == '-':
# 				init_n -= float(t)
# 			elif init_operator == 'x':
# 				init_n *= float(t)
# 			elif init_operator == '/':
# 				init_n /= float(t)

# 			init_operator = 'x'
# 			init_n = init_n-1

# 		elif s == '/':
# 			if lastSign(text) != -1:
# 				t = text[lastSign(text)+1:]
# 			else:
# 				t = text
			

# 			if init_operator == '+':
# 				init_n += float(t)
# 			elif init_operator == '-':
# 				init_n -= float(t)
# 			elif init_operator == 'x':
# 				init_n *= float(t)
# 			elif init_operator == '/':
# 				init_n /= float(t)

# 			init_operator = '/'
# 			init_n = init_n-1



# 		print(init_n)


# 		if text.startswith('0'):
# 			text = text.replace('0','',1)			
# 		if s=='=':
# 			self.ids.calc_input.text=str(init_n)
# 			init_operator = '+'
# 			new = True
# 		else:
# 			text+=str(s)
# 			self.ids.calc_input.text=text

# 			new = False