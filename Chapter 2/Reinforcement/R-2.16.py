"""
R-2.16 
Our Range class, from Section 2.3.5, relies on the formula
max(0, (stop − start + step − 1) // step)
to compute the number of elements in the range. It is not immediately evident
why this formula provides the correct calculation, even if assuming
a positive step size. Justify this formula, in your own words.
"""

"""
The first thing the formula does is to obtain the numbers between start and stop.
If you divide the number with step, it will be 1 number minor than the actual result.
So to assure that you add step to the last substraction and to be sure that 
it does not show any larger number than the actual result, yo substract 1.
However, I found another formula while I was trying to understad the one given
in the exercise:

max(0, ((stop-step)//step)+1)
"""