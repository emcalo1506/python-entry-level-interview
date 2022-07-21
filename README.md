# Python Interview

## Instructions
Fork the repo and create a MR to provide a solution for the problems. \
Each problem has a corresponding folder, except 3 and 4 which need to be together.

All the problems should not take more than a day.

You will be evaluated on your software best practices, problem-solving skills and the quality of the solutions:
- Performance
- Maintainability
- Scalability
- Coding standards, data structures, OOP, etc...
- Git: MR/Branch/commits

## Problems

### 1. Improve the code

Code contains a program to build figures and its properties.
Specifically, its purpose is to calculate:
- circle/square area and perimeter 
-  cube volume.

Improve the code of the program. 
The code should still be able to run.

This problem should not take more than 2h.

---

### 2. Find the :bug:
Upon running the program you'll verify the program is not fully functional.\
Find the bug(s) and fix the code so all functionalities work.

This problem should not take more than 1h.

Bonus points if you implement an alternative solution (`better-counter-with-tracker.py`) which would improve the code.

---

### 3. Implement a solution
Create a simple program that performs actions according to the user input.

Program specification:
- It should require initial input (username and password) to setup an admin account.

- After initial setup, the program allows **anyone** to input username and password to register as a user.

- It should verify the validity of usernames and password input by the user or users.
Usernames must be at least 5 characters and contain only letters.
Passwords must follow the industry standards.

- All registered user is are allowed to login.
- All logged-in users are allowed to logout.
- All logged-in users can change their passwords.
- Logged in Admin users can delete other users but not themselves.
- Logged in Admin users can list users and their passwords.

You can use any libraries/tools that you want.

Provide instructions on how to run your program.

This problem should not take more than 3h.

Tip: You don't need to connect to a real DB, in memory or filesystem memory is sufficient. \
Tip: **KISS!** For user input, a simple scripting solution with `input()`, or a library like Click CLI is sufficient.

---

###  4. Don't forget tests!
Implement a couple unit tests for your program using pytest.
This problem should not take more than 2h.

Bonus points if you use unittest mock library.

