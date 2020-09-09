import tkinter as tk
import tkinter.font as tkFont

from util import string_is_float, string_is_int


class IntEntry(tk.Entry):
	def __init__(self, master=None, **kwargs):
		self.var = tk.StringVar()
		tk.Entry.__init__(self, master, textvariable=self.var, **kwargs)
		self.old_value = ''
		self.var.trace('w', self.check)
		self.get, self.set = self.var.get, self.var.set

	def check(self, *args):
		if string_is_int(self.get()) or len(self.get()) == 0: 
			self.old_value = self.get()
		else:
			self.set(self.old_value)
	
	def get_int(self):
		if string_is_int(self.get()):
			return int(self.get())
		return 0


class FloatEntry(tk.Entry):
	def __init__(self, master=None, **kwargs):
		self.var = tk.StringVar()
		tk.Entry.__init__(self, master, textvariable=self.var, **kwargs)
		self.old_value = ''
		self.var.trace('w', self.check)
		self.get, self.set = self.var.get, self.var.set

	def check(self, *args):
		if string_is_float(self.get()) or len(self.get()) == 0: 
			self.old_value = self.get()
		else:
			self.set(self.old_value)

	def get_float(self):
		if string_is_float(self.get()):
			return float(self.get())
		return 0