#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This loops based on 'n': Linear: O(n)


b) This loops until it's equal to: Polynomial: O(n^2)


c) Recursion is calling on itself: Linear: O(n)

## Exercise II
Determine the value of f in a way that breaks the least amount of eggs (least amount of attempts).

* n = stories in building
* f = the highest floor where the eggs don't break when dropped.
* If at or above floor f, the egg breaks, else egg doesn't break.

A binary search Runtime: O(log(n)) can be used here.

A solution for this:

* Go to floor n/2 (which is the middle of the building).
* Then drop the egg.
* If egg breaks, you the move halfway down the building (halfway between the current floor and the bottom).
* If it didn't break, you'd move halfway up the building (halfway between the current floor and the top).
* Then repeat over and over each time eliminating half the options until you find the exact floor the egg doesn't break.

<!-- Written-Code: The Function Move to n//2 if f == 1 return 1 drop egg if egg breaks repeat at new floor determined by current floor//2 (lower half) if egg not broken repeat at new floor determined by n-current floor//2 (upper half) -->

This could also be a linear search: O(n) How to solve:

* The Person starts at the first floor, then goes to each floor and drops an egg.
* If the egg doesn't break, move to the next floor.
* If the egg breaks, stop and then determine the floor below the current is the last floor where eggs do not break.

<!-- Written-Code: The Function Move to n = 1 if egg does not break, then n = n+1 if egg breaks at n, then f = n -->