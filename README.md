# Dynamic Programming Paragraph Formatting

This code uses a dynamic programming algorithm to quickly and efficiently format a paragraph of text such that it minimizes the
total amount of white space at the ends of the lines. This "penalty" is the difference between the number of characters on a line
and the character limit specified by the user. No line will ever exceed the character limit, and any extra space on the last line 
is not included in the penalty count.

To run the code, download the files into a directory and run:

	python paragraph.py [INPUT FILE (.txt)] [CHARACTER LIMIT (INT)]

This will print to the terminal an aesthetically formatted paragraph, and will also print out the total penalty across all lines. You can use any input text file you choose, but I've included a sample here for you as well (a personal favorite, Robin Williams's monologue from Good Will Hunting).


The code works by using a dynamic lookup table to determine the best way to pack words onto a given line whereby by the sum of
the penalties on the remaining lines is minimized.

Since our recursion takes only one variable, our lookup table is an array of length n, for which each index i will correspond to the minimum penalty of packing i + 1 words into a paragraph (“i + 1” because we go from 1 to n instead of from 0 to n − 1). We initialize all elements to infinity, so that our minimums will never be interrupted by an existing start value. Our base cases involve the words that could be on the last line, which receive no penalty:

For all words *l_b* such that the sum of the words from *l_b* to the end is less than M, we initialize the f[n − b] to be 0. This ensures that any words that could end up on the last line carry no penalty, and if we arrive at a 0 element in our recursion we know we’ve gotten to the end.

Now we have an array of length n where the first *b* indices, where *b* is the number of words that could be on the last line, are initialized to 0. Now we can build up the array using the recursive equation described above, filling each element with the minimum penalty of packing that many words into paragraph form, and building all the way until the end, where we find our desired penalty. If we wanted to actually print the words, we could simply create another array to store the j values at each stage, and trace the proper path through that array to reconstruct the number of words on each line, and print them as such. This is what my Python file does.