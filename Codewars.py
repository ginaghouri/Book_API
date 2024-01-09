#1.Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

def even_or_odd(number):
    if number % 2==0: 
        return "Even"
    else:
        return "Odd"

#2.We need a function that can transform a number (integer) into a string. What ways of achieving this do you know?
#Examples (input --> output): 123  --> "123" 999  --> "999" -100 --> "-100"
    
    def number_to_string(num):
    return str(num) # str() function returns a string, it converts a number into a string

#3.Write function RemoveExclamationMarks which removes all exclamation marks from a given string.

    def remove_exclamation_marks(s):
    return s.replace('!', '')

#4.Grade book.Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade.
#Numerical Score Letter Grade 90 <= score <= 100 'A'80 <= score < 90'B'70 <= score < 80	'C'60 <= score < 70	'D'0 <= score < 60	'F'

def get_grade(s1, s2, s3):
    avg = int((s1 + s2 + s3) / 3)
    
    if avg in range(90, 101):
        return 'A'
    elif avg in range(80, 90):
        return 'B'
    elif avg in range(70, 80):
        return 'C'
    elif avg in range(60, 70):
        return 'D'
    elif avg in range(0, 60):
        return 'F'
    
#5.

#6. Write a function that takes an array of numbers and returns the sum of the numbers. The numbers can be negative or non-integer. If the array does not contain any numbers then you should return 0.
#Examples Input: [1, 5.2, 4, 0, -1] Output: 9.2 Input: [] Output: 0 Input: [-2.398] Output: -2.398 Assumptions You can assume that you are only given numbers. You cannot assume the size of the array.
#You can assume that you do get an array and if the array is empty, return 0.

def sum_array(a):
    return sum(a)
    
#7.    Complete the square sum function so that it squares each number passed into it and then sums the results together. For example, for [1, 2, 2] it should return 9 because 
# For example, for [1, 2, 2] it should return 9 because 1square+2square+2square=9

 def square_sum(numbers):
    return sum([n*n for n in numbers])

#8.Create a function with two arguments that will return an array of the first n multiples of x.Assume both the given number and the number of times to count will be positive numbers greater than 0.
#Return the results as an array or list ( depending on language ).Examples count_by(1,10) #should return [1,2,3,4,5,6,7,8,9,10] count_by(2,5) #should return [2,4,6,8,10]

def count_by(x, n):     
    return [(i + 1) * x for i in range(n)]

#9.Given a list of integers, determine whether the sum of its elements is odd or even. Give your answer as a string matching "odd" or "even". If the input array is empty consider it as: [0] (array with a zero).
#Examples: Input: [0] Output: "even" Input: [0, 1, 4] Output: "odd" Input: [0, -1, -5] Output: "even"

def odd_or_even(arr):
    if sum(arr) % 2==0:
       return "even"
    else: 
       return "odd"
    
#10.You're writing code to control your town's traffic lights. You need a function to handle each change from green, to yellow, to red, and then to green again.
#Complete the function that takes a string as an argument representing the current state of the light and returns a string representing the state the light should change to.
#For example, when the input is green, output should be yellow. 
    
def update_light(current):
    if current=="green":
        return ("yellow")
    if current=="yellow":
        return ("red")
    if current=="red":
        return ("green")    
    
#11.Given an array of integers, return a new array with each value doubled. For example: [1, 2, 3] --> [2, 4, 6]
    
# Step 1: Create a new empty list
# Step 2: Loop through the existing (given) list 
# As you loop through the list, multiply each element by 2 and push to the new list
# Step 3: return the new list

def maps(a):
    newlist=[]
    for x in a:
        newlist.append(x*2)
    return newlist

#12.   Write a function named setAlarm/set_alarm/set-alarm/setalarm (depending on language) which receives two parameters. The first parameter, employed, is true whenever you are employed and the second parameter, vacation is true whenever you are on vacation.
#The function should return true if you are employed and not on vacation (because these are the circumstances under which you need to set an alarm). It should return false otherwise. Examples:
#employed | vacation 
#true     | true     => false
#true     | false    => true
#false    | true     => false
#false    | false    => false

def set_alarm(employed, vacation):
    if employed is True and vacation is True:
        return False
    if employed is True and vacation is False: 
        return True
    if employed is False and vacation is True:
        return False
    if employed is False and vacation is False:
        return False 

#13.We need a function that can transform a string into a number. What ways of achieving this do you know?
#Note: Don't worry, all inputs will be strings, and every string is a perfectly valid representation of an integral number.
#Examples "1234" --> 1234 "605"  --> 605 "1405" --> 1405 "-7" --> -7
    
   def string_to_number(s):
     return int(s) 

#14.Nathan loves cycling.Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.
#You get given the time in hours and you need to return the number of litres Nathan will drink, rounded to the smallest value.
#For example: time = 3 ----> litres = 1 time = 6.7---> litres = 3 time = 11.8--> litres = 5

def litres(time):
    return int(time*0.5)

#15.Write a function that accepts an integer n and a string s as parameters, and returns a string of s repeated exactly n times.
#Examples (input -> output) 6, "I"     -> "IIIIII" 5, "Hello" -> "HelloHelloHelloHelloHello"

def repeat_str(n, s):
    return (s*n)

#16.Return the number (count) of vowels in the given string. We will consider a, e, i, o, u as vowels for this Kata (but not y).
#The input string will only consist of lower case letters and/or spaces.

def get_count(sentence):
    numberOfVowels = 0
    numberOfVowels += sentence.count('a')
    numberOfVowels += sentence.count('e')
    numberOfVowels += sentence.count('i')
    numberOfVowels += sentence.count('o')
    numberOfVowels += sentence.count('u')
    return numberOfVowels

#17.Write a function that takes an array of words and smashes them together into a sentence and returns the sentence. You can ignore any need to sanitize words or add punctuation, but you should add spaces between each word. Be careful, there shouldn't be a space at the beginning or the end of the sentence!
#Example ['hello', 'world', 'this', 'is', 'great']  =>  'hello world this is great'

def smash(words):
    x = " ".join(words)
    
    return(x)
    
#18.Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.
#Examples input/output: XO("ooxx") => true XO("xooxx") => false XO("ooxXm") => true XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true XO("zzoo") => false

def xo(s):
    s = s.lower()
    if s.count('x') == s.count ('o'):
        return True
    else: return False

#19.Deoxyribonucleic acid, DNA is the primary information storage molecule in biological systems. It is composed of four nucleic acid bases Guanine ('G'), Cytosine ('C'), Adenine ('A'), and Thymine ('T').
#Ribonucleic acid, RNA, is the primary messenger molecule in cells. RNA differs slightly from DNA its chemical structure and contains no Thymine. In RNA Thymine is replaced by another nucleic acid Uracil ('U').
#Create a function which translates a given DNA string into RNA. For example: "GCAT"  =>  "GCAU"
    
def dna_to_rna(dna):
    return dna.replace("T", "U" )

#20.You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.

#Examples: Kata.getMiddle("test") should return "es" Kata.getMiddle("testing") should return "t" Kata.getMiddle("middle") should return "dd" Kata.getMiddle("A") should return "A"
#Input A word (string) of length 0 < str < 1000 (In javascript you may get slightly more than 1000 in some test cases due to an error in the test cases). You do not need to test for this. This is only here to tell you that you do not need to worry about your solution timing out.
#Output The middle character(s) of the word represented as a string.

def get_middle(s):
    half = int(len(s) / 2)
    if len(s) % 2 == 0:
        return s[half - 1 : half + 1]
    else:
        return s[half]
    
 #21.Your classmates asked you to copy some paperwork for them. You know that there are 'n' classmates and the paperwork has 'm' pages.
#Your task is to calculate how many blank pages do you need. If n < 0 or m < 0 return 0. Example: n= 5, m=5: 25 n=-5, m=5:  0
    
    def paperwork(n, m):
    if n < 0 or m < 0:
        return 0
    else:
        return n*m
    
#22.Character recognition software is widely used to digitise printed texts. Thus the texts can be edited, searched and stored on a computer.
#When documents (especially pretty old ones written with a typewriter), are digitised character recognition softwares often make mistakes.

#Your task is correct the errors in the digitised text. You only have to handle the following mistakes: #S is misinterpreted as 5 O is misinterpreted as 0
#I is misinterpreted as 1  The test cases contain numbers only by mistake.
    
    def correct(s):
    fixedSentence = s.replace ('5',"S")
    fixedSentence = fixedSentence.replace ('0', "O")
    fixedSentence = fixedSentence.replace ('1', "I")
    return fixedSentence

#23.Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0. Your function only needs to return the result, what is shown between parentheses in the example below is how you reach that result and it's not part of it, see the sample tests.
#For example (Input -> Output): 2 -> 3 (1 + 2) 8 -> 36 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8)  

def summation(num):
    return sum(range(1, num+1))

#24.Implement a function which convert the given boolean value into its string representation. Note: Only valid inputs will be given.

def boolean_to_string(b):
    return str (b)

#25.Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

def even_or_odd(number):
    if number % 2==0: 
        return "Even"
    else:
        return "Odd"

 #26. 
    


#27.Grade book.Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade.
#Numerical Score	Letter Grade 90 <= score <= 100	'A' 80 <= score < 90	'B' 70 <= score < 80	'C' 60 <= score < 70	'D' 0 <= score < 60	'F'

def get_grade(s1, s2, s3):
    avg = int((s1 + s2 + s3) / 3)
    
    if avg in range(90, 101):
        return 'A'
    elif avg in range(80, 90):
        return 'B'
    elif avg in range(70, 80):
        return 'C'
    elif avg in range(60, 70):
        return 'D'
    elif avg in range(0, 60):
        return 'F'
    
#28.Make a function that will return a greeting statement that uses an input; your program should return, "Hello, <name> how are you doing today?".
# Make sure you type the exact thing I wrote or the program may not execute properly]
    
    def greet(name):
    return "Hello, " + name + " how are you doing today?"

#29.Write a function that takes an array of numbers and returns the sum of the numbers. The numbers can be negative or non-integer. If the array does not contain any numbers then you should return 0.
#Examples Input: [1, 5.2, 4, 0, -1] Output: 9.2 Input: [] Output: 0 Input: [-2.398] Output: -2.398 Assumptions You can assume that you are only given numbers.
#You can assume that you do get an array and if the array is empty, return 0. We're testing basic loops and math operations. This is for beginners who are just learning loops and math operations.
#Advanced users may find this extremely easy and can easily write this in one line.

def sum_array(a):
    return sum(a)

#30.