from fpdf import FPDF
 
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Python Roadmap: Beginner to Advanced", ln=True, align="C")
 
    def chapter_title(self, title):
        self.set_font("Arial", "B", 12)
        self.set_text_color(0, 0, 128)
        self.cell(0, 10, title, ln=True, align="L")
        self.ln(2)
    
    def chapter_body(self, body):
        self.set_font("Arial", "", 11)
        self.set_text_color(0, 0, 0)
        self.multi_cell(0, 8, body)
        self.ln()
 
    def add_chapter(self, title, body):
        self.add_page()
        self.chapter_title(title)
        self.chapter_body(body)

print('File Generation Start') 
# Roadmap content
roadmap = {
    "Beginner Level": """
1. Python Basics
   - Installing Python & Setting up IDE (VSCode, PyCharm, Jupyter)
   - Hello World, Comments
   - Variables and Data Types
   - Input and Output
   - Basic Operators (Arithmetic, Assignment, Comparison, Logical)
 
2. Control Flow
   - if, elif, else
   - for and while loops
   - break, continue, pass
 
3. Data Structures
   - Lists, Tuples, Sets, Dictionaries
   - Comprehensions: list, set, dict
 
4. Functions
   - Defining and calling functions
   - Arguments (*args, **kwargs)
   - Lambda functions, Scope
 
5. Basic Error Handling
   - try, except, finally, else
""",
    "Intermediate Level": """
6. Modules and Packages
   - Importing modules, Creating packages, pip
 
7. Object-Oriented Programming (OOP)
   - Classes, Objects, Inheritance, Polymorphism, Encapsulation
   - Magic methods (__init__, __str__, etc.)
 
8. File Handling
   - Reading/Writing files, Modes, Context manager
 
9. Advanced Functions & Concepts
   - Decorators, Generators, Iterators, Closures, Recursion
 
10. Working with Libraries
   - requests, json, datetime, os, shutil
""",
    "Advanced Level": """
11. Advanced OOP
   - Abstract Classes, Mixins, Multiple Inheritance, Property Decorators
 
12. Functional Programming
   - map, filter, reduce, Higher-order functions
 
13. Concurrency and Parallelism
   - Threading, Multiprocessing, Asyncio (async/await)
 
14. Testing
   - unittest, pytest, TDD, Mocking
 
15. Logging and Debugging
   - logging module, pdb
 
16. Design Patterns
   - Singleton, Factory, Observer, etc.
""",
    "Specializations": """
- Web Development: Flask, Django, REST APIs, ORM
- Data Science: pandas, numpy, matplotlib, scikit-learn
- Automation: selenium, pyautogui, beautifulsoup
- DevOps: Docker, CI/CD, virtual environments
- AI & NLP: transformers, spacy, nltk, openai
 
Practice Platforms:
- LeetCode, HackerRank, Codewars, Project Euler
- Projects: CLI tools, APIs, dashboards, games
"""
}
 
# Create PDF
pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)
 
for title, content in roadmap.items():
    pdf.add_chapter(title, content)
 
# Output file
# pdf.output("Python_Roadmap_Deep_Dive.pdf")
print('File Generation End. Please Check file in your folder!')
# user_input = input('Enter something: ')
# print('Lo ji bata diya-'+user_input)

# a = input('Enter first number: ')
# b = input('Enter second number: ')
# print(a+b)

divyansh = 5.88
print(type(divyansh))
divyansh = "divya"
print(type(divyansh))
print(divyansh[4])
divyansh = 5
print(type(divyansh))
divyansh = True
print(type(divyansh))
divyansh = 'C'
print(type(divyansh))

divyansh = None
print(type(divyansh))
"""
Data type operations
"""
#sum of two number
a = "5"
b = "True"
print(a+b)

"""Operators"""
#1. Arithmatic Operators (+,-,*,/)
"""
| Operator | Description         | Example  |
| -------- | ------------------- | -------- |
| `+`      | Addition            | `a + b`  |
| `-`      | Subtraction         | `a - b`  |
| `*`      | Multiplication      | `a * b`  |
| `/`      | Division (float)    | `a / b`  |
| `//`     | Floor Division      | `a // b` |
| `%`      | Modulus (remainder) | `a % b`  |
| `**`     | Exponentiation      | `a ** b` |

"""
#2. Assignment Operators
"""
| Operator | Example   | Equivalent To |
| -------- | --------- | ------------- |
| `=`      | `a = b`   | Assign        |
| `+=`     | `a += b`  | `a = a + b`   |
| `-=`     | `a -= b`  | `a = a - b`   |
| `*=`     | `a *= b`  | `a = a * b`   |
| `/=`     | `a /= b`  | `a = a / b`   |
| `//=`    | `a //= b` | `a = a // b`  |
| `%=`     | `a %= b`  | `a = a % b`   |
| `**=`    | `a **= b` | `a = a ** b`  |

"""
#3 Comparision Operators
"""
| Operator | Description      | Example  |
| -------- | ---------------- | -------- |
| `==`     | Equal to         | `a == b` |
| `!=`     | Not equal to     | `a != b` |
| `>`      | Greater than     | `a > b`  |
| `<`      | Less than        | `a < b`  |
| `>=`     | Greater or equal | `a >= b` |
| `<=`     | Less or equal    | `a <= b` |

"""
#4 Logical Operators
"""
and ,or, not
ex:- a==b and b==a,    a==b or b==a,  nor(a>b)
"""

#5 Bitwise Operators
"""
| Operator | Description | Example (a = 5, b = 3) |     |         |
| -------- | ----------- | ---------------------- | --- | ------- |
| `&`      | AND         | `a & b` → `1`          |     |         |
| \`       | \`          | OR                     | \`a | b`→`7\` |
| `^`      | XOR         | `a ^ b` → `6`          |     |         |
| `~`      | NOT         | `~a` → `-6`            |     |         |
| `<<`     | Left Shift  | `a << 1` → `10`        |     |         |
| `>>`     | Right Shift | `a >> 1` → `2`         |     |         |

"""
#6 Membership Operators
"""
| Operator | Description      | Example            |
| -------- | ---------------- | ------------------ |
| `in`     | Value exists     | `'a' in 'cat'`     |
| `not in` | Value not exists | `'x' not in 'dog'` |

"""
#7 Identity Operators
"""
| Operator | Description     | Example      |
| -------- | --------------- | ------------ |
| `is`     | Same object     | `a is b`     |
| `is not` | Not same object | `a is not b` |

"""

#8 Ternary Operator (Conditional Expression)
"""
result = a if a > b else b

"""


##Type Conversion
"""
It is a automatic conversion in python 
it convert into its convenient type 
it is called Implicit conversion
"""

#Type Casting 

"""
It has happend Explicitly 
It works only if conversion is possible 

a = "5"
b = 6
sum = int(a)+b
"""

##Taking Input from the user
Name = input('Enter Your Name: ')
print('Your name is '+Name)

#Need type casting if you want to take input except String
#If you are not type casting then it will convert it in string

#example

a = input('enter a ')
b = input('enter b ')
print ("Output",a+b)
"""
enter a 5
enter b 2
Output:52
"""
a = int(input('enter a '))
b = int(input('enter b '))
print ("Output",a+b)
"""
enter a 6
enter b 6
Output 12
"""