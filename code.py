# guessing_word
 ges_limit = 3
ges_cont = 0
out_of_gess = False
name = input("username : ")
s_word = "London"
user_gess = ""
while user_gess != s_word and not(out_of_gess) :
    if ges_cont < ges_limit :
        user_gess = input("Ur Word : ")
        ges_cont += 1
        if user_gess == s_word:
            print("You win " + name + " !")
        if (ges_cont == 1 or ges_cont == 2) and (user_gess != s_word) :
            print("incorrect Answer, try again "+name+" !")

    else:
        out_of_gess = True
if out_of_gess:
    print("sorry you lose the game "+name+" !")
