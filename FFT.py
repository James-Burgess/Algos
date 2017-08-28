#!/usr/bin/python3
import numpy as np 

def numpy_FFT(x):
	return np.fft.fft(x)

def slow_FT(x):
	x = np.asarray(x, dtype=float)
	size = x.shape[0]
	n = np.arange(size)
	k = n.reshape((size, 1))
	M = np.exp(-2j * np.pi * k * n / size)
	return np.dot(M, x)

def turkey_FFT(x):
    #A recursive implementation of the 1D Cooley-Tukey FFT
    x = np.asarray(x, dtype=float)
    size = x.shape[0]
    
    if size % 2 > 0:
        raise ValueError("size of x must be a power of 2")
    elif size <= 32:  # this cutoff should be optimized
        return slow_FT(x)
    else:
        X_even = (numpy_FFT(x[::2]))
        X_odd = (numpy_FFT(x[1::2]))
        factor = np.exp(-2j * np.pi * np.arange(size) / size)
        try:
	        return np.concatenate([X_even + factor[:size / 2] * X_odd,
	                               X_even + factor[size / 2:] * X_odd]) 
        except TypeError:
        	print("latest version of numpy does not support indexing on floats, reccomend downgrading to numpy 1.11.1")    
def slow_iFT():
	pass




def populateArray():
	#put the code to calcualte the 1d Arrays here
	#im just unsing random numbers to test for now
	return np.random.random(1024)


def main():
	x = populateArray()
	if turkey_FFT(x).all()== numpy_FFT(x).all():
		print("winner")


if __name__ == '__main__':
	main()