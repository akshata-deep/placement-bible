# Create a program capable of displaying question to the user like KBC
# Use List data type to store the questions and their answers 
# Display the final amount the person is taking home after playing the game 




question = ["Which of these celestial bodies is closest to the Earth?","In the context of standard computer keyboards, what does the 'Q' in QWERTY represent?","Which Indian state or Union Territory is known as the \"Land of High Passes\"?","Which prominent Indian scientist founded the Indian Space Research Organisation (ISRO)?","Which international currency features a symbol that incorporates two parallel vertical lines cutting through a letter, similar to the US Dollar symbol ($), but uses a different letter?"]
answers = ["A) Mars B) Venus C) The Moon D) Mercury","A) The first letter of the top row of alphabet keys B) The name of the keyboard's inventor C) \"Quick Electronic Response Typewriter\" D) The rarest used letter in the English language","A) Jammu & Kashmir B) Himachal Pradesh C) Ladakh D) Sikkim","A) Dr. Homi J. Bhabha B) Dr. Vikram Sarabhai C) Dr. A.P.J. Abdul Kalam D) Dr. Satish Dhawan","A) British Pound (£) B) Euro (€) C) Japanese Yen (¥) D) Nicaraguan Córdoba (C$)"]
correct = ["c","a","c","b","d"]
print("========== Kaun Banega Crorepati ==========\n")
winner_money = 0
num = 0
for i in question:
    print(f"{i}\n"
          f"OPTION : \n"
          f"{answers[num]}\n")
    user_answer = input("ANSWER : ")
    if user_answer == correct[num]:
            print("CONGRAJULATION !")
            winner_money += 100000
            print(f"The money you won : {winner_money}\n\n")
            num +=1
    else:
            print("wrong answer !")
            print(f"The money you won : {winner_money}")
            break
if  winner_money == 500000:
       print("YOU ARE THE CROREPATI !.........\n"
             "============= CONGRAJULATIONS ==============")