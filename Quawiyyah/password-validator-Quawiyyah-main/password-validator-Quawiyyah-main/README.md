## Password Validator

In this project, you are going to implement a program that validates a password 
entered by a user.

## Steps

The program should start by asking the user to enter a password with these criteria:

- Length must be between 9 and 12 characters
- At least 3 special characters
- At least 5 alphabetic characters 

You may then use a loop to check password characters one at a time. 

The special characters for this project are: **&, #, $, !, ?, ", (, )**

## Hints

- It may be helpful to initialize counter variables outside the loop to count 
  different types of characters you need.
- A success message should display if all conditions are met.
- The program should exit when it encounters the first failed condition. Print a 
  message explaining the condition that was not met.
- Define your constants at the beginning of the program, so you can use them 
  later on without changing every occurrence within the script.

## Sample Runs

Failed Validation:

![image](assets/failure_case.PNG)

Successful Validation:

![image](assets/success_case.PNG)

## Starter Code

Check the file called `validator.py`, and start writing your code there.

## Bonus Task

Add the condition where the password needs to have at least 3 numbers.
