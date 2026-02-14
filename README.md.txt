
Project Documentation: Personal Information Manager
1. Project Overview
This project is a Python-based Personal Information Manager. It is designed to act as a digital profile card. The program combines "static" data (information already saved in the code) with "dynamic" data (information collected from the user) to generate a clean, formatted summary.
The goal of this project was to practice the core foundations of Python: variables, user input, mathematical operations, and data validation.

2. Setup Instructions
To get this program running on your local machine, follow these steps:
Install Python: Download and install the latest version of Python from python.org.
Create Project Folder: Create a folder named week1-personal-info.
Add the Script: Create a file named personal_info.py inside that folder and paste the program code.
Open Terminal: Open your Command Prompt (Windows) or Terminal (Mac/Linux).
Navigate: Use the cd command to enter your project folder:
Example: cd Desktop/week1-personal-info
Run the Program: Type the following command and press Enter:
python personal_info.py

3. Code Structure
The project is organized in a clean, flat hierarchy to ensure simplicity and ease of navigation:
Plaintext
week1-personal-info/
│
├── personal_info.py    # Main Python script containing the logic
├── README.md           # This documentation file
├── test_inputs.txt     # Log of manual test cases
└── .gitignore          # Rules for Git version control






4. Technical Details
Algorithms & Logic
Data Storage: Information is stored using Variables. We use strings for text and integers for numerical data.
Age Calculation: The program uses a simple arithmetic expression to convert years to months: $age\_months = age \times 12$.
Validation Loop: To prevent the program from accepting blank answers, I used a while loop. This loop checks if the input is empty or just spaces using the .strip() method.
Formatting: I utilized f-strings (formatted string literals), which allow us to embed variables directly into text for a clean UI.

5. Testing Evidence
I performed manual testing to ensure the program handles different user behaviors correctly:
Test Scenario
User Input
Expected Behavior
Result
Normal Use
"chicken", "red"
Profile prints successfully
PASS
Empty Input
[Just pressed Enter]
Program asks for input again
PASS
Numeric Food
"123"
Program accepts it as a string
PASS
Long Text
"Home-made Spicy Chicken"
Formatting remains aligned
PASS









6. Visual Documentation
Note: To complete this section for your submission, run your program, take a screenshot of the window, and save it as screenshot.png in your folder.
Sample Output from Terminal:
Plaintext
===================================
     PERSONAL INFORMATION
===================================
Name: Aman Kumar
Age: 21 (252 months old)
City: Ramgarh
Hobby: Cooking

Favorite Food: mutton
Favorite Color: black
===================================
Thank you for using the program!




