#!/usr/bin/python3
##Love you gabi
import numpy as np 

def sinewave():
	fs = 100 # sample rate 
	f = 1 # the frequency of the signal

	x = np.arange(0, 2*np.pi, 0,1) # the points on the x axis for plotting
	# compute the value (amplitude) of the sin wave at the for each sample
	y = [ np.sin(2*np.pi*f * (i/fs)) for i in np.arange(fs)]

	return (x,y)