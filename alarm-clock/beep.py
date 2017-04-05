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
import os
#
# Here, I am Using Ubuntu
# that's why current function is working for me
# but if you are using any other operating system
# then, you need to customize below function as 
# your operating system supports.
#
# Check This Links
#
# http://askubuntu.com/questions/19906/beep-in-shell-script-not-working
# http://stackoverflow.com/questions/6537481/python-making-a-beep-noise
# http://stackoverflow.com/questions/16573051/python-sound-alarm-when-code-finishes
#
#
# Beep Creating Function
def beep(sec):
	for i in range(sec):
		os.system("beep -f 555 -l 460")
	return

# Trigger Function
if __name__ == '__main__':
	beep(5)