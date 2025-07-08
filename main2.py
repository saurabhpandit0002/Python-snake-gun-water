# Snake Gun Water Game
#This game is played between two players. and 2nd player is computer 

import random
computer =random.choice([-1,0,1])
your_Dict={'s':1,'g':0,"w":-1}
reverseDict={1:"Snake🐍",0:"Gun🔫",-1:"Water💧"}
Your_score=0
Computer_score=0
for i in range(3):
    print(f"\n🎮 Round {i+1} of 3 🎮")
    
    your_choice=input( "Enter your Choice (S= Snake🐍, G=Gun🔫 ,W=Water💧):").lower()
    if your_choice not in your_Dict:
        print(" ❌  invalid choices kindly enter s,g or w")
    else:
        your=your_Dict[your_choice]
        print(f" 🧑 Your choice is {reverseDict[your]}")
        print(f" 💻 Computer choice is {reverseDict[computer]}")
    if your==computer:
        print("🤝 it is a tie")
    elif(your==1 and computer==-1) or \
            (your==0 and computer==-1) or \
            (your==0 and computer==1) :
            print("✅ You win")
            Your_score+=1
    elif(your==1 and computer==0) or \
        (your==-1 and computer==1) or \
         (your==-1 and computer==0) :    
         print(" ❌ You Lose")
         Computer_score+=1
print("Game Over! Final Results" )
print(f"Your Score:{Your_score}")
print(f"Computer Score:{Computer_score}")
if Your_score > Computer_score:
    print("🎉 Congratulations! You are the overall winner!")
elif Your_score < Computer_score:
    print("😞 Sorry! Computer wins the game.")
else:
    print("🤝 It's a tie game!")



