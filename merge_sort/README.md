
Requirements
General

    Allowed editors: vi, vim, emacs
    All your files will be compiled on Ubuntu 14.04 LTS
    Your programs and functions will be compiled with gcc 4.8.4 using the flags -Wall -Werror -Wextra and -pedantic
    All your files should end with a new line
    A README.md file, at the root of the folder of the project, is mandatory
    Your code should use the Betty style. It will be checked using betty-style.pl and betty-doc.pl
    You are not allowed to use global variables
    No more than 5 functions per file
    Unless specified otherwise, you are not allowed to use the standard library. Any use of functions like printf, puts, … is totally forbidden.
    In the following examples, the main.c files are shown as examples. You can use them to test your functions, but you don’t have to push them to your repo (if you do we won’t take them into account). We will use our own main.c files at compilation. Our main.c files might be different from the one shown in the examples
    The prototypes of all your functions should be included in your header file called sort.h
    Don’t forget to push your header file
    All your header files should be include guarded
    A list/array does not need to be sorted if its size is less than 2.

More Info

For this project you are given the following print_array function:

alexa@ubuntu-xenial:merge_sort$ cat print_array.c
#include <stdlib.h>
#include <stdio.h>

/**
* print_array - Prints an array of integers
*
* @array: The array to be printed
* @size: Number of elements in @array
  */
  void print_array(const int *array, size_t size)
  {
  size_t i;

  i = 0;
  while (array && i < size)
  {
  if (i > 0)
  printf(", ");
  printf("%d", array[i]);
  ++i;
  }
  printf("\n");
  }
  alexa@ubuntu-xenial:merge_sort$

  Our file print_array.c (containing the print_array function) will be compiled with your functions during the correction.
  Please declare the prototype of the function print_array in your sort.h header file
  Please, note this format is used for Big O notation:
  O(1)
  O(n)
  O(n!)
  n square -> O(n^2)
  log(n) -> O(log(n))
  n * log(n) -> O(nlog(n))

