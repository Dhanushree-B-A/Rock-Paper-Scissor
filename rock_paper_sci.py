import random
rock='''
  *-*-*
*       *
  *-*-*
'''

paper='''
*-*-*-*
*-*-*-*
*-*-*-*
'''

scissor='''
* *       * *
 * *    * *
  * --- *
    * *
    * *
    * *
     *
     '''

user_score = 0
computer_score =0

while True:
    game_img=[rock,paper,scissor]    
    print("1.Enter 0 for rock\n2.Enter 1 for paper\n3.Enter 2 for scissor.")
    user_choice=int(input("enter your choice: "))
   
    if(user_choice>2 or user_choice<0):
        print("Invalid choice")

    else:
        print("Your choice: ",user_choice)
        print(game_img[user_choice])
        comp_choice=random.randint(0,2)
        print("Computer choice:",comp_choice)
        print(game_img[comp_choice])
       
        if(comp_choice==0 and user_choice==2):
            result = "You lose"
            print(result)
            computer_score += 1
    
        elif(comp_choice==2 and user_choice==0):
            result = "You wins"
            print(result) 
            user_score += 1   
    
        elif(comp_choice>user_choice):
            result = "You lose"
            print(result) 
            computer_score += 1
           
        elif(user_choice>comp_choice):
            result = "You wins"
            print(result) 
            user_score += 1
            
        elif(comp_choice==user_choice):
            result = "Its a draw!!"
            print("It's a draw!!")

        print("Your score is: ",user_score)
        print("Computer score is: ",computer_score)

        #option to continue  or quit the game
        #if user typed y/Y the game will continue
        #otherwise it will terminate the game and gives the final scores
        play_agian = input("Do you want to play again? (y/n): ").lower()
        if(play_agian != 'y'):
            print("You quit the game")
            print("Final scores")
            print(f"Your score is: {user_score}")
            print(f"Computer score is: {computer_score}")
            break
       
        




    
    


    

