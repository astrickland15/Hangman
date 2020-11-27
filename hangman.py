import re
import random



def play_again():
     again=input("Play again? (y/n) ")
     if again=="y":
          lets_play()
     else:
          print("Goodbye.")



          

def create_random_word():
     words=["mississippi",
            "anthony",
          "adult",
"aeroplane",
"air",
"aircraftcarrier",
"airforce",
"airport",
"album",
"alphabet",
"apple",
"arm",
"army",
"baby",
"baby",
"backpack",
"balloon",
"banana",
"bank",
"barbecue",
"bathroom",
"bathtub",
"bed",
"bed",
"bee",
"bible",
"bible",
"bird",
"bomb",
"book",
"boss",
"bottle",
"bowl",
"box",
"boy",
"brain",
"bridge",
"butterfly",
"button",
"cappuccino",
"car",
"carrace",
"carpet",
"carrot",
"cave",
"chair",
"chessboard",
"chief",
"child",
"chisel",
"chocolates",
"church",
"church",
"circle",
"circus",
"circus",
"clock",
"clown",
"coffee",
"coffeeshop",
"comet",
"compactdisc",
"compass",
"computer",
"crystal",
"cup",
"cycle",
"database",
"desk",
"diamond",
"dress",
"drill",
"drink",
"drum",
"dung",
"ears",
"earth",
"egg",
"electricity",
"elephant",
"eraser",
"explosive",
"eyes",
"family",
"fan",
"feather",
"festival",
"film",
"finger",
"fire",
"floodlight",
"flower",
"foot",
"fork",
"freeway",
"fruit",
"fungus",
"game",
"garden",
"gas",
"gate",
"gemstone",
"girl",
"gloves",
"god",
"grapes",
"guitar",
"hammer",
"hat",
"hieroglyph",
"highway",
"horoscope",
"horse",
"hose",
"ice",
"icecream",
"insect",
"jetfighter",
"junk",
"kaleidoscope",
"kitchen",
"knife",
"leatherjacket",
"leg",
"library",
"liquid",
"magnet",
"man",
"map",
"maze",
"meat",
"meteor",
"microscope",
"milk",
"milkshake",
"mist",
"money",
"monster",
"mosquito",
"mouth",
"nail",
"navy",
"necklace",
"needle",
"onion",
"paintbrush",
"pants",
"parachute",
"passport",
"pebble",
"pendulum",
"pepper",
"perfume",
"pillow",
"plane",
"planet",
"pocket",
"postoffice",
"potato",
"printer",
"prison",
"pyramid",
"radar",
"rainbow",
"record",
"restaurant",
"rifle",
"ring",
"robot",
"rock",
"rocket",
"roof",
"room",
"rope",
"saddle",
"salt",
"sandpaper",
"sandwich",
"satellite",
"school",
"sex",
"ship",
"shoes",
"shop",
"shower",
"signature",
"skeleton",
"slave",
"snail",
"software",
"solid",
"spaceshuttle",
"spectrum",
"sphere",
"spice",
"spiral",
"spoon",
"sportscar",
"spot light",
"square",
"staircase",
"star",
"stomach",
"sun",
"sunglasses",
"surveyor",
"swimmingpool",
"sword",
"table",
"tapestry",
"teeth",
"telescope",
"television",
"tennisracquet",
"thermometer",
"tiger",
"toilet",
"tongue",
"torch",
"torpedo",
"train",
"treadmill",
"triangle",
"tunnel",
"typewriter",
"umbrella",
"vacuum",
"vampire",
"videotape",
"vulture",
"water",
"weapon",
"web",
"wheelchair",
"window",
"woman",
"worm",
"xray"

            ]
     selection=random.choice(words)
     return selection

def display_incorrect_guesses(text):
     return "/" +text + "/"

def current_score(s, i, gl, igl):
     s=" ".join(gl)
     i=" ".join(igl)
     return s + "       " + i


def original_clue(gl):
     gl=" ".join(gl)
     return gl

def draw_gallows():
     print("______")
     print("|    |")
     print("     |")
     print("     |")
     print("     |")
     print("     |")
     print("_____|_")



def strike_one():
     print("______")
     print("|    |")
     print("O    |")
     print("     |")
     print("     |")
     print("     |")
     print("_____|_")


def strike_two():
     print("______")
     print("|    |")
     print("O    |")
     print("|    |")
     print("|    |")
     print("     |")
     print("_____|_")

def strike_three():
     print(" _____")
     print(" |    |")
     print(" O    |")
     print("\|    |")
     print(" |    |")
     print("      |")
     print("______|_")

def strike_four():
     print(" _____")
     print(" |    |")
     print(" O    |")
     print("\|/   |")
     print(" |    |")
     print("      |")
     print("______|_")

def strike_five():
     print(" _____")
     print(" |    |")
     print(" O    |")
     print("\|/   |")
     print(" |    |")
     print("/     |")
     print("______|_")


def game_over():
     print(" _____")
     print(" |    |")
     print(" O    |")
     print("\|/   |")
     print(" |    |")
     print("/ \   |")
     print("______|_")
     print("\n\nGame over!!  You lost.")
     

def add_strikes(_inc_guess):
     if _inc_guess==1:
          strike_one()
     elif _inc_guess==2:
          strike_two()
     elif _inc_guess==3:
          strike_three()
     elif _inc_guess==4:
          strike_four()
     elif _inc_guess==5:
          strike_five()
     elif _inc_guess==6:
          game_over()
          
          








def lets_play():
     
     guessed_letters=[]
     word=create_random_word()
     print("Welcome to Hangman! \n\n\n  ") 
     
     incorrect_guesses=0
     solution=""
     incorrect=""
     inc_guess_list=[]
     
     #create a new list and add hyphen for each character in chosen word

     new_word=[]
     for letter in word:
          
          guessed_letters.append("-")
          new_word.append(letter)
     print (original_clue(guessed_letters))
     draw_gallows()
     
     while guessed_letters.__contains__("-") :

          guess=input("Guess a letter: ")
          guess=guess.lower()
          
          if not re.match("^[a-z]*$", guess):
               print("Please enter a letter.")
               continue

          if solution.__contains__(guess):
               print("you have already guessed this letter.")
               continue
          #check occurrence of guess and add to a new list   
          index=[i for i in range(len(new_word)) if new_word[i]==guess]

          #add each occurrence of letter to the solution
          for ind in index:
               if new_word[ind]==guess:
                    guessed_letters[ind]=guess

          solution=" ".join(guessed_letters)
          
          if guess not in word:
               print("Incorrect guess.  Please try again.")
               inc_guess_list.append(display_incorrect_guesses(guess))
               incorrect_guesses+=1
               add_strikes(incorrect_guesses)
               
               if incorrect_guesses==6:
                    break
                    

               print(current_score(solution, incorrect, guessed_letters, inc_guess_list))
               continue     

          print("correct guess!!!")
          print(current_score(solution, incorrect, guessed_letters, inc_guess_list))
          
          
     play_again()
          
                        
          
     

if  __name__ == "__main__":


     lets_play()          

     


    
     





