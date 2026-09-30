import random
credits=int(5000)
multiplier=1.0
cred=0
print(f"WELCOME TO THE DIGITAL CASINO\nYour Starting CREDITS={credits}")
#Selecting Game mode
def gameselection(credits):
    print("\n------------------------------------------------------------------")
    if credits>0:
        print("Which game do you want to play")
        a=input("Type 'S' to play Slot machine ,'R' to play Roulette ,'B' to play Blackjack or 'Q' to exit:")
        if a.upper()=='S':
            credits=slot(credits)
            gameselection(credits)
        if a.upper()=='R':
            credits=roulette(credits)
            gameselection(credits)
        if a.upper()=='B':
            credits=Blackjack(credits)
            gameselection(credits)
        if a.upper()=='Q':
            print("THANKS FOR PLAYING")
            return
    else:
        print("OUT OF CREDITS, THANKS FOR PLAYING")
#Roulette Betting function
def Betting(*bets):
    length=len(bets)
    x=random.randrange(1,36)
    if x in bets:
        print("Bet won!")
        multiplier=1.0*(36/length)
        print("The Bet landed on:",x)
        return multiplier
    else:
        multiplier=0.0
        print("Bet lost!")
        print("The Bet landed on:",x)
        return multiplier
#Slot Machine        
def slot(credits):
    symbols = ("🔔", "🍒", "7️⃣", "🚀", "📱", "💻")
    while credits> 0:
        print("\n------------------------------------------------------------------")
        print(f"you have {credits} credits")
        cred=int(input("Enter credits you want to bet:"))
        credits-=cred
        result = []
        print("spinning in progress")

        for i in range(3):
            pick = random.choice(symbols)
            result.append(pick)

        print(" ".join(result))

        if result[0] == result[1] == result[2]:
            print("congratulations! you won the jackpot")
            multiplier=10.0
        elif result[0] == result[1] or result[1] == result[2] or result[0] == result[2]:
            print("congratulations! you Matched the slots!")
            multiplier=2.5
        else:
            print("better luck next time")
            multiplier=0.0
        credits+=cred*multiplier
        print(f"credits left: {credits}")
        temp=(input("Want to spin again?(y for yes, n for no):"))
        if temp.lower()=='y':
            pass
        else:
            return credits
    if credits <= 0:
        print("out of credits")
        return credits

    print("thanks for playing slot game")
#Roulette
def roulette(credits):
    while credits>0:
        print("\n------------------------------------------------------------------")
        print("ROULETTE GAME: PLACE BETS ON NUMBERS AND WIN CREDITS")
        for i in range (1,37):
            if i<10:
                if(i%2==0):
                    print(f"\033[40m0{i}\033[0m",end=" ")
                else:
                    print(f"\033[41m0{i}\033[0m",end=" ")
            elif i%2==0:
                print(f"\033[40m{i}\033[0m",end=" ")
            else:
                print(f"\033[41m{i}\033[0m",end=" ")
            if i%3==0:
                print()
        cred=int(input("How many credits do you want to bet: "))
        credits-=cred 
        if(credits>=0):
            print(f"Credits left:{credits}")
            print("which type of inside bet do you wanna place")
            Type_bet=input("Type '1' for straight bet, '2' for split, '3' for street, '4' for corner, '5' for double street:\n(Enter numbers space seperated):")
            if(Type_bet.upper()=='1'):
                n=input("Bet on a single number:")
                multiplier=Betting(n)
            if(Type_bet.upper()=='2'):
                n1,n2=map(int,input("Bet on vertically/horizontally adjacent numbers (eg.8-9)").split())
                if(n2==(n1+1) or n2==(n1+3)):
                    multiplier=Betting(n1,n2)
                else:
                    print("invalid bet for bet type")
            if(Type_bet.upper()=='3'):
                n1,n2,n3=map (int,input("Bet on three consecutive numbers in a horizontal line(eg. 1-2-3 ): ").split())
                multiplier=Betting(n1,n2,n3)
            if(Type_bet.upper()=='4'):
                n1,n2,n3,n4= map(int,input("Bet on four numbers that meet at one corner(eg. 1-2-4-5): ").split())
                multiplier=Betting(n1,n2,n3,n4)
            if(Type_bet.upper()=='5'):
                n1,n2,n3,n4,n5,n6= map(int,input("Bet on six consecutive numbers that form two horizontal lines(eg. 1-2-3 & 4-5-6): ").split())
                multiplier=Betting(n1,n2,n3,n4,n5,n6)
        else:
            print("Invalid input")
            return credits
        credits+=cred*multiplier
        print(f"Credits left:{credits}")
        again=input("Play Roulette again?(y or n): ")
        if again.lower()=='y':
                pass
        else:
                return credits
    if(credits<=0):
            print("Insufficient credits")
            return credits


card_values={'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10,'A':11}

def create_deck():
    symbols=['1','2','3','4']
    value=list(card_values.keys())
    deck=[]
    for _ in symbols:
        for i in value:
            deck.append(i)
    return deck

def calculate_hand(hand):
   total= sum([card_values[card] for card in hand])
   aces=hand.count('A')
   while total>21 and aces:
       total-=10
       aces-=1
   return total
def display_game(player_hand,dealer_hand,hide_hand=True):
    if hide_hand == False: # To reveal the Dealers second Card
        print(f"\nDealer Hand: {dealer_hand} ")
        print(f"\nDealer Hand Total: {calculate_hand(dealer_hand)} ")
    elif hide_hand == True: # To Hide the dealer's card
        print(f"\nDealer Hand: {dealer_hand[0]}, ?")

    print(f"\nPlayer Hand: {player_hand}")
    print(f"\nPlayer Hand Total: {calculate_hand(player_hand)} ")
    print("\n------------------------------------------------------------------")

def play_blackjack():
    deck = create_deck()
    random.shuffle(deck) #Randomize the cards from which the cards will be distributed
    player_hand = [deck.pop(), deck.pop()] #Pops first 2 cards to the player
    dealer_hand = [deck.pop(), deck.pop()] #Pops next 2 cards to the dealer
    display_game(player_hand,dealer_hand,hide_hand=True)

    if calculate_hand(player_hand)==21 and calculate_hand(dealer_hand)==21 :
        display_game(player_hand,dealer_hand,hide_hand=False)
        print("Both Have Blackjack! Tie")
        return "Tie"
    elif calculate_hand(player_hand)==21:
        display_game(player_hand,dealer_hand,hide_hand=False)
        print("Player Have Blackjack! Player Won")
        return "Win"
    elif calculate_hand(dealer_hand)==21:
        display_game(player_hand,dealer_hand,hide_hand=False)
        print("Dealer Have Blackjack! Dealer Won")
        return "Lost"
    #Player turn
    while True:

        choice=input("Player wants to 'H' for HIT or 'S' for STAND: ")
        if choice=='H':
            player_hand.append(deck.pop())
            display_game(player_hand, dealer_hand, hide_hand=True)
            if calculate_hand(player_hand)>21:
                print("Player Busts Dealer Won")
                return "Lost"
            elif calculate_hand(player_hand)==21:
                print("Player Has Blackjack ! Player Won")
                return "Win"
        elif choice=='S':
            display_game(player_hand, dealer_hand, hide_hand=True)
            break
        else:
            print("Invalid choice")

    #Dealer Turn
    while calculate_hand(dealer_hand) <17:
        print("Dealer Hits")
        dealer_hand.append(deck.pop())
        display_game(player_hand,dealer_hand,hide_hand=False)

    player_total =calculate_hand(player_hand)
    dealer_total =calculate_hand(dealer_hand)

    if dealer_total>21:
        print("Dealer Busts,Player Won")
        return "Win"
    if dealer_total==21:
        print("Dealer Has Blackjack ! Dealer Won")
        return "Lost"
    elif dealer_total>player_total:
        print("Dealer Win")
        return "Lost"
    elif dealer_total<player_total:
        print("Player Win")
        return "Win"
    else:
        print("Tie")
        return "Tie"

def Blackjack(credits):
    while credits>0:
        print("\n------------------------------------------------------------------")
        print("Welcome to Python Blackjack!") 
        bet = int(input("credits you want to bet: "))
        credits-=bet
        if credits>=0:
            result=play_blackjack()
            if result=="Tie":
                print(f"You Won:0\nYour Credits: {credits}")
            elif result=="Win":
                credits=bet + credits
                print(f"You Won:{2*bet}\nYour credits: {2*bet + credits}")
            elif result=="Lost":
                print(f"You Lost:{bet}\nYour credits: {credits}")
            again = input("\nPlay another round? (Y/N): ")
            if credits>0:
                if again.upper() == 'Y':
                    pass
                else:
                    return credits
            else:
                print("insufficient credits")
                return credits
    if credits<=0:
            print("insufficient credits")
            return credits
gameselection(credits)