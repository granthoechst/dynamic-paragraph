import math
import sys

if (len(sys.argv) != 3):
	print("Usage: python paragraph.py [INPUT FILE] [LINE CHARACTER LIMIT]")
	exit()

input_text = open(sys.argv[1], 'r')

M = int(sys.argv[2])

words = []

for line in input_text:
	for word in line.split():
		words.append(word)
n = len(words)

def char_on_line(words, end_word, start_word):
	sum = 0
	for i in range(start_word - 1, end_word):
		sum += len(words[i])
	return end_word - start_word + sum

def penalty_calc(words, j):
	return math.pow((M - char_on_line(words, j, 1)), 3)

def build_dyna_array(words):
	dyna_array = []
	for i in range(0, n):
		dyna_array.append(float("inf"))
		if M >= char_on_line(words, n, (n - i)):
			dyna_array[i] = 0
	return dyna_array


breaks = []
for i in range(0,n):
	breaks.append(0)

def dynamic_recursion(n, words, f):
	if (f[n - 1] < float("inf")):
		return f[n - 1]
	else:
		minimum = float("inf")
		j_final = 0
		for j in range(1, n + 1):
			if (M >= char_on_line(words, j, 1)):
				val = dynamic_recursion(n - j, words[j:n], f) + penalty_calc(words, j)
				if (val < minimum):
					j_final = j
					minimum = val
		f[n - 1] = minimum
		breaks[n - 1] = j_final
		return f[n - 1]


f = build_dyna_array(words)

g = dynamic_recursion(n, words, f)

print("")

final_breaks = []
final_breaks.append(breaks[n - 1])
while(sum(final_breaks) < (n - 1)):
	x = breaks[(n - 1) - sum(final_breaks)]
	if(x == 0):
		break
	final_breaks.append(x)
final_breaks.append(n - sum(final_breaks))


for i in range(0, len(final_breaks)):
	line = ""
	for j in range(0, final_breaks[i]):
		line = line + words[j] + " "
	print(line)
	words = words[final_breaks[i]:len(words)]
print("")
print("Penalty:")
print(f[n - 1])
print("")

