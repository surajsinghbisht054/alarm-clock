#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Written By:
#		S.S.B
#		surajsinghbisht054@gmail.com
#		bitforestinfo.blogspot.com
#
#	
#
#
##################################################
######## Please Don't Remove Author Name #########
############### Thanks ###########################
##################################################
#
#
# Import Module
try:
	import Tkinter
	import ttk
except:
	import tkinter as Tkinter
	import tkinter.ttk as ttk
import datetime
import beep
import os

# Creating Clock Main Root Sub Class
class Clock(Tkinter.Tk):
	def __init__(self, *args, **kwargs):
		Tkinter.Tk.__init__(self, *args, **kwargs)
		self['padx']=20
		self['pady']=20
		# Creating Variables
		self.waiting_string_variable = Tkinter.IntVar()
		self.show_alarm_time = Tkinter.StringVar()
		self.show_alarm_time.set(datetime.datetime.now().ctime())
		self.alarm_delta_time = None
		self.create_first_label()
		self.create_second_box()

	# Creating Set Alarm time Showing Label
	def create_first_label(self):
		ttk.Label(self, textvariable=self.show_alarm_time, font = ("arial 20 bold")).grid(row=0, column=1, columnspan=2, padx=10,pady=10)
		return

	# Creating Keypad
	def create_second_box(self):
		ttk.Label(self, text="Wait For Seconds : ").grid(row=1, column=1, padx=10,pady=10)
		ttk.Entry(self, textvariable = self.waiting_string_variable).grid(row=1, column=2, padx=10,pady=10)
		ttk.Button(self, text="Exit", command=self.destroy).grid(row=3, column=1, padx=10,pady=10)
		ttk.Button(self, text="Set Alarm!", command=self.set_alarm_button).grid(row=3, column=2, padx=10,pady=10)
		return

	# Set Alarm Function 
	def set_alarm_button(self):
		try:
			sec = self.waiting_string_variable.get()
			self.alarm_delta_time = datetime.datetime.now()+datetime.timedelta(seconds=sec)
			self.show_alarm_time.set(self.alarm_delta_time.ctime().__str__())
		except:
			self.waiting_string_variable.set(0)
		return

	# Updating Loop
	def regular_update(self):
		self.update()
		self.update_idletasks()
		if self.alarm_delta_time:
			if datetime.datetime.now() > self.alarm_delta_time:
				beep.beep(5)


		return

# Main Function
def main():
	root = Clock(className = " Simple Alram Clock By Bitforestinfo")
	while True:
		root.regular_update()
	return

# Main trigger Function
if __name__ == '__main__':
	main()