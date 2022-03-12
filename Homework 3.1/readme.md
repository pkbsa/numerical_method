Write the following programs to solve equation f(x) = 0.  Your answer must be precise up to 4 significant figures.

1.  Solve function f(x) = x^3 -6x^2 + 4x + 12 = 0 (find all x's that makes f(x) = 0) using the divide and conquer method between region [-2, 6]  together with interval search (search for the intervals that should contain the root of the function).  Check your answer using wolframalpha.com.

2. Solve function f(x) = x^3 -6x^2 + 4x + 12 = 0 (find all x's that makes f(x) = 0) between region [-2, 6] using the Bisection method implemented as a recursive function.  Since the region [-2, 6] has multiple roots, you should use the interval search method to locate small intervals that contains single roots first and then apply bisection method.  Check your answer using wolframalpha.com.

3.  Solve function f(x) = x^3 -6x^2 + 4x + 12 = 0 (find all x's that makes f(x) = 0) between region [-2, 6] using the False Position method implemented as a simple while loop and a recursive function.   Since the region [-2, 6] has multiple roots, you should use the interval search method to locate small intervals that contains single roots first and then apply the False Position method.  Check your answer using wolframalpha.com.

4. Find at least 2 mathematical functions that Bisection method performs better than False Position method (less number of search step until epa < eps) and vice versa (Find at least 2 mathematical functions that False Position method performs better than the Bisection method).  Confirm your claims with a program.
