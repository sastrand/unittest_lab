## A lab for unit testing in Python

We want the code in `cap.py` to take a string and capitalize the first letter
in each word in the string.   

Leading symbols can be ignored, so the input "@maya" should return "@Maya".    
Leading numbers should be considered the first character, and left unchanged, so the input "49ers" should return "49ers".

Based on this problem specification, add two more unit tests to `test.py`.

And try this workflow
  * Run `python3 tests.py` 
  * Observe failures/errors
  * Modify the code in `cap.py` to address the error
  * Repeat until all the tests pass

> Test code from Bill Lubanovic, *Introducing Python* 
[github](https://github.com/madscheme/introducing-python)
