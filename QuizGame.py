print("_____WELCOME TO THE QUIZ GAME_____")
ans=input("To Start the game Enter YES otherwise EXIT:")
ans1=ans.upper()
if ans1=="YES":
    print("Some Information and Rules about the game are below:")
    print(f"1.Each question carries 2 marks.\n2.There is no negative marks.\n3.Answering all the questions is mandotary.\n4.Choose One of the otion given below.\n5.Score DIsplay at Last.")
    print("Lets's Start")
    count=0
    print(f"Question 1: What is the value of (6**3)?")
    print("A.36 B.18 C.216 D.729")
    a1=input()
    if(a1=='C' or a1=='c'):
        print("Correct")
        count+=2
    else:
        print("Wrong,The Correct Option is C")
    print(f"Question 2: Which of the following are immutable? ")
    print("A.List B.Set C.Tuple D.None")
    a2=input()
    if(a2=='C' or a2=='c'):
        print("Correct")
        count+=2
    else:
        print("Wrong,The Correct Option is C")
    print("Question 3: The Arithematic operator that cannot be used with strings is")
    print("A.- B.* c.+ D.All of these")
    a3=input()
    if(a3=='A' or a3=='a'):
        print("Correct")
        count+=2
    else:
        print("Wrong,The Correct Option is A")
    print("Question 4: The method that is used to count the number of times an item occured in the list is")
    print("A.count() B.len() C.length() D.extend()")
    a4=input()
    if (a4=="A" or a4=="a"):
        print("Correct")
        count+=2
    else:
        print("Wrong,The Correct Option is A")
    print("Question 5: Which of the following cannot be used as a key in python Dictionaries?")
    print("A.Strings B.Lists C.Tuples D.Numerical Values")
    a5=input()
    if a5=='B' or a5=='b':
        print("Correct")
        count+=2
    else:
        print("Wrong,The Correct Option is B")
    print(f"Total Score:{count}")
    print("THANK YOU FOR PARTICIPATION")
else:
    print("THANK YOU")
    
