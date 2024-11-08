#For this project, I did research online about how to use TextBlob for the NLP purposes of this program.
#Most information came from analyticsvidya.com, and I watched a couple YouTube videos explaining different parts of TextBlob. 
import random #importing random module 
from textblob import TextBlob #importing TextBlob module for its Natural Language Processing features

# the collection of 25 verses into a dictionary for the program to use
print("Welcome to the Bible Verse Memorization Game!")
print("You will have three tries to correctly input the Bible verse that is given to you.")
print("Try to get the highest score you can!\n")

verses_dictionary = {
    "John 3:16" : "For God so loved the world that he gave his one and only Son, that whoever believes in him shall not perish but have eternal life",
    "Genesis 1:1" : "In the beginning God created the heavens and the earth",
    "1 Corinthians 13:4-5" : "Love is patient, love is kind. It does not envy, it does not boast, it is not proud. It does not dishonor others, it is not self-seeking, it is not easily angered, it keeps no record of wrongs",
    "Matthew 6:34" : "Therefore do not worry about tomorrow, for tomorrow will worry about itself. Each day has enough trouble of its own",
    "Philippians 4:6-7" : "Do not be anxious about anything, but in every situation, by prayer and petition, with thanksgiving, present your requests to God. And the peace of God, which transcends all understanding, will guard your hearts and your minds in Christ Jesus",
    "1 Corinthians 16:14" : "Do everything in love",
    "Proverbs 16:3" : "Commit to the Lord whatever you do, and he will establish your plans",
    "Isaiah 41:10" : "So do not fear, for I am with you; do not be dismayed, for I am your God. I will strengthen you and help you; I will uphold you with my righteous right hand",
    "Jeremiah 29:11" : "For I know the plans I have for you, declares the Lord, plans to prosper you and not to harm you, plans to give you hope and a future",
    "Proverbs 17:17" : "A friend loves at all times, and a brother is born for a time of adversity",
    "2 Corinthians 5:7" : "For we live by faith, not by sight",
    "1 Thessalonians 5:16-18" : "Rejoice always, pray continually, give thanks in all circumstances; for this is God’s will for you in Christ Jesus",
    "Romans 12:2" : "Do not conform any longer to the pattern of this world, but be transformed by the renewing of your mind. Then you will be able to test and approve what God’s will is—his good, pleasing and perfect will",
    "Proverbs 21:21" : "Whoever pursues righteousness and love finds life, prosperity and honor",
    "Mark 11:24" : "Therefore I tell you, whatever you ask for in prayer, believe that you have received it, and it will be yours",
    "Philippians 4:13" : "I can do all this through him who gives me strength",
    "Matthew 28:19" : "Therefore, go and make disciples of all nations, baptizing them in the name of the Father and of the Son and of the Holy Spirit",
    "1 Corinthians 13:13" : "And now these three remain: faith, hope and love. But the greatest of these is love",
    "Psalm 42:11" : "Why, my soul, are you downcast? Why so disturbed within me? Put your hope in God, for I will yet praise him, my Savior and my God",
    "1 Peter 5:7" : "Throw all your anxiety onto him, because he cares about you",
    "1 John 4:19" : "We love because He first loved us",
    "Matthew 11:28" : "Come to me, all you who are weary and burdened, and I will give you rest ",
    "Proverbs 3:5" : "Trust in the Lord with all your heart and lean not on your own understanding",
    "Romans 15:13" : "May the God of hope fill you with all joy and peace as you trust in him, so that you may overflow with hope by the power of the Holy Spirit",
    "Psalm 23:1-3" : "The Lord is my shepherd; I shall not want. He makes me lie down in green pastures. He leads me beside still waters. He restores my soul",
    }

#beginning function that starts the game
def want_to_play():
    """Asking the user if they want to play or not
    Parameters:
    __________
    None
    If the user chooses “Yes”, the function will proceed to randomize_verse()
        If the user chooses “No”, the program will end
        Else: raises ValueError
    Returns:
    __________
    None

    """
    attempts = 0 #counts attempts
    while attempts < 3: #while loop to get a correct user response after three tries
        try:
            user_response = input("Do you want to play? Please enter 'Y' or 'N': ").strip().lower()
            if user_response == 'y':
                randomize_verse(verses_dictionary) #if yes, running the rest of the program
                break
            elif user_response == 'n': # if no, ending the game
                print("Game ended. See you next time!")
                break
            else:
                raise ValueError("Invalid input. Please enter 'Y' or 'N'.")
        except ValueError as err:
            attempts += 1
            print(err)
            if attempts == 3:
                print("You reached the maximum for invalid responses. Game ended.")
                break
            
    return 

def randomize_verse(verses_dictionary): #function to randomize verse
    """Randomly choosing Bible verse and randomizing the words with their POS
    Parameters:
    __________
    verses_dictionary 
    Returns:
    __________
    tuple 
    the randomized Bible verse’s words and their parts of speech
    """
    renamed_pos = { #renaming the textblob POS tags to something more understandable
        'CC': 'conjunction',
        'JJ': 'adj',
        'NN': 'noun',
        'VB': 'verb',
        'IN': 'preposition',
        'DT': 'determiner',
        'JJS': 'adjective',
        'RB': 'adverb',
        'VBZ': 'verb',
        'VBN': 'verb',
        'NNP': 'noun',
        'NNS': 'noun',
        'PRP': 'pronoun',
        'TO': 'prepositon',
        'WRB': 'adverb',
        'PRP$': 'pronoun',
        'WP': 'pronoun',
        'MD': 'verb',
        'CD': 'number',
        'WDT': 'determiner',
        'VBP': 'verb',
        'VBD': 'verb',
        'VBG': 'verb'
        }
    
    
    verses = list(verses_dictionary.items()) #making dictionary a tuple 
    verse_index = random.randint(0,24) #choosing index from random integer
    key,value = verses[verse_index] #assigning to random key and value pair
    
    random_verse = (key,value)
    
    #splitting the verse into individual words
    words = value.split()

    # Shuffle the words
    random.shuffle(words) #randomizing the word order

    # Print the verse in randomized order
    print('\nReconstruct the verse based on its words and their parts of speech') #header
    
    print("Verse:", key)
    print()
    for word in words:
        pos_word = TextBlob(word)
        word_tag = pos_word.tags[0][1] #tagging each word with its closest part of speech 
        pos_word_word = renamed_pos.get(word_tag, word_tag) #renaming words' POS
        print(f"{word} [{pos_word_word}]", end=" ")
    
    reconstruct_verse(verses_dictionary,3,random_verse) #moving to reconstruct the verse with a max of 3 tries
    return key,value
    
    
def reconstruct_verse(verses_dictionary,max_tries,random_verse):
    """Prompts the user to reconstruct the verse 
    Parameters:
    __________
    verses_dictionary
    max_tries: integer 3
    randomized_verse : the tuple with words and parts of speech 

    Returns:
    __________
    str 
        User’s input (which is a string)

    """
    key,value = random_verse
    print()
    user_verse_input = input('Reconstructed verse: ')
    if user_verse_input.lower().strip() == value.lower().strip():
        print("Correct!")
        print(f'Your verse was: {random_verse}')
        input_result = "correct"
        keep_score(input_result,3) #adds 1 to score
    else:
        print("Wrong! Try again! (Don't forget to include the proper punctuation!)")
        input_result ='incorrect'
        tries_remaining = keep_score(input_result, max_tries) #max of 3 tries to get correct 
        if tries_remaining != 0:
            reconstruct_verse(verses_dictionary, tries_remaining,random_verse)
        else:
            print()
            print("Sorry, you have used all of your tries.")
            print(f'Your verse was: {random_verse}')
            print(f'Your score was: {score}')
            print("Game over!")
            
    return

def keep_score(user_answer, max_tries):
    """ Adds 1 to score if correct. If incorrect after max tries, program quits

    Parameters:
    __________
    user_anwer 
        the string that the user is guessing is the correct answer
    max_tries: integer 3

    Returns:
    __________
    score
        if correct, score += 1
        if incorrect, max_tries += 1 (cannot = 3 or else program ends)
    """
    global score #ability to increment score
    if user_answer == "correct":
        score += 1
        print(f'Your score is {score}')
        play_again = input("Do you want to play again? Enter Y or N ").lower().strip()
        if play_again == 'y':
            randomize_verse(verses_dictionary) #playing again
        elif play_again == 'n':
            print("Thank you for playing!")
            print(f'Your score was {score}.')
        else: 
            attempts = 0 
            while attempts < 2: #while loop to get a correct user response after three tries
                try:
                    user_response = input("Do you want to play? Please enter 'Y' or 'N': ").strip().lower()
                    if user_response == 'y':
                        randomize_verse(verses_dictionary) #if yes, running the rest of the program
                        break
                    elif user_response == 'n': # if no, ending the game
                        print("Game ended. See you  next time!")
                        break
                    else:
                        raise ValueError("Invalid input. Please enter 'Y' or 'N'.")
                except ValueError as err:
                    attempts += 1
                    print(err)
                    if attempts == 3:
                        print("You reached the maximum for invalid responses. Game ended.")
                        break
            
    else:
        max_tries -= 1 
        print(f'Remaining tries: {max_tries}')
    return max_tries




score = 0
want_to_play() #starting game
