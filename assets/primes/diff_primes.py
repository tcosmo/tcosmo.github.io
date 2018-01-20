"""
MIT License

Copyright (c) 2017 Tristan Cosmo Stérin

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

'''
You should create a directory frames/ in the same directory than the code in order to save the frames.
In order to generate the video you can use:
	
	ffmpeg -framerate 25 -i %d.png -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p output.mp4

'''


import numpy as np
from sympy import sieve
import matplotlib.pyplot as plt

sieve._reset()
sieve.extend(10000)

primes = list(sieve._list)

def diff_list(l):
	diff = []
	for i in range(1,len(l)):
		diff.append(l[i]-l[i-1])
	return diff

def iterate_diff(l):
	curr_diff = l[:]

	yield curr_diff
	while len(curr_diff) != 1:
		curr_diff = diff_list(curr_diff)
		yield curr_diff

print("\n\nThis code should crash when matplotlib cannot handle big numbers anymore (around 1e304).\n\n")

i = 0
for curr_diff in iterate_diff(primes):
	plt.figure(figsize=(20,10))
	plt.plot(curr_diff, 'o')
	plt.savefig('frames/'+str(i))
	plt.close()
	i += 1

	if i%200 == 1:
		print("{} frame(s) generated...".format(i))