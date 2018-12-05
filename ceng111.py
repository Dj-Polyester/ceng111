print "This is an unofficial test for the ceng111 midterm. For the statements with question marks (?) please write the answer without any prepositions (a,an,the) and only write the first word of the answer (Instead of the functional programing ->Functional). For the statements with (T/F) at the end, write True or False. Always start with uppercase letter. If you have any feedback regarding the bugs, questions etc, you can inform me via whatsapp. Good luck!"
"""Questions are below. If you want to add your questions, add listq[number of the question]="question? $Answer" 
below other questions."""
listq=range(26)
listq[0]="What is the program that translates the source code to the object code? $Compiler"
listq[1]="What is the program that creates an executable code from the object code using the information in the library? $Linker"
listq[2]="What is the programming paradigm that is used by writing a sequence of statements? $Imperative"
listq[3]="Which programming paradigm necessitates decomposition of the problem into functions or is a mathematical approach? $Functional"
listq[4]="In what programming paradigm, the relations between the facts or rules are stated? $Logical"
listq[5]="In which programming paradigm, the problem is solved using methods? $Object"
listq[6]="Which programming paradigm involves inheritance? $Object"
listq[5]="In which programming paradigm, multiple processors partially solve the problem? $Concurrent"
listq[6]="What is the program that can be commanded interactively? $Interpreter"
listq[7]="In compilative approach, the programmer can locate errors interactively.(T/F) $False"
listq[8]="Compilative approach is slow relatively to the interpretive approach.(T/F) $False"
listq[9]="In white box testing, only the input and output can be tested.(T/F) $False"
listq[10]="The tester using the black box can overlook some minor details which the programmer also did.(T/F) $False"
listq[11]="The assignment Area==l x l has only one Syntax error.(T/F) $False"
listq[12]="To denote multiplication in python, * symbol is used.(T/F) $True"
listq[13]="sqrt(b*b - 4*a*c),when returned in function, doesn't give error because it doesn't have any syntax error.(T/F) $False"
listq[14]="What is the structured data type that is used to organize data indexingly? $Array"
listq[15]="The pointers are used commonly in Arrays(data structures).(T/F) $False"
listq[16]="If the data is structured in arrays, one can definitely jump the address they are looking for quickly.(T/F) $True"
listq[17]="Insertion is extremely time consuming when it is implemented into arrays, because it is executed by the hard disk.(T/F) $False"
listq[18]="The CPU works faster with integers than with floating points.(T/F) $True"
listq[19]="In python, del is used as a statement to remove multiple datas from a list.(T/F) $True"
listq[19]="In python, L.pop([index]) doesn't return a value after removing the indexed number from the list L.(T/F): $False"
listq[20]="What is the term used to describe the lifetime of a variable? $Extent"
listq[20]="What is the term used to describe the parts that are accessible by a variable? $Scope"
listq[21]="In Python, the variable cannot access to the outer bounds of the function it is defined in.(T/F) $False"
listq[21]="In Python, the aliasing problem only occurs in lists, because they are mutable.(T/F) $False"
listq[22]="If reduction system of an operation results in a single result,the operation can be said to possess Church-Rosser property.(T/F) $True"
listq[23]="2 3 + is a postfix notation.(T/F) $True"
listq[24]="Given 7 bits, please write -4 in two's complement notation. $1111100"
listq[25]="Write -23,625 in IEEE 32 bit notation. Write as shown in parantheses(sign,exponent,mantissa). $1,10000011,0111101"
p=0
import random
random.shuffle(listq)
n=len(listq)
for i in range(n):
	no=i+1
	print "Question "+str(no)+":"
	index=listq[i].find("$")
	q=str(raw_input(listq[i][:index:]))
	if q.lower()==listq[i][index+1::].lower():
		print "Correct answer"
		p=p+1
	else:
		print "Incorrect answer"
		print "The correct answer is:"+ listq[i][index+1::]
print "Test has been finished."+str(p)+"out of "+str(n)+"questions are correctly answered"
