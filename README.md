# Toeplitz-Matrix
A Toeplitz matrix is a matrix where every left-to-right-descending diagonal has the same element.
Given a non-empty matrix arr, the function returns true if and only if it is a Toeplitz matrix.
(The matrix can be any dimensions, not necessarily square).

For example:
```
[[1,2,3,4],
[5,1,2,3],
[6,5,1,2]]
```
is a toeplitz matrix, the function will return true.

while,
```
[[1,2,3,4],
 [5,1,9,3],
 [6,5,1,2]]
 ```
isn’t a Toeplitz matrix, the function will return false.
