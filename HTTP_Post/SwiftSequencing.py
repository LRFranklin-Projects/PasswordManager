import collections
import random

def create_word_list():
    # Open the text file in read mode
    with open('HTTP_Post\\temp.txt', 'r') as file:
        
        # Read the content of the text file
        file_content = file.read()
        
        # Split the content into words, using space as the separator
        words_list = file_content.split()

    # Create a dictionary to store unique words in the order they appear
    # Dictionary is an ordered set
    unique_words_dict = collections.OrderedDict.fromkeys(words_list)

    # Type cast it back into a list
    unique_words_list = list(unique_words_dict)

    # Open the same text file in write mode to overwrite the content
    with open('HTTP_Post\\temp3.txt', 'w') as file:
        # Write the unique words back to the file so I can set a list equal to it
        for word in unique_words_list:
            file.write(f'\"{word}\"' + ", ")

# End of create_word_list function


class SwiftSequencer:
    key_to_edit = ""
    unique_words_list = ["I", "dont", "know", "what", "want", "So", "ask", "me", "Cause", "Im", "still", "trying", "to", "figure", "it", "out", "Dont", "whats", "down", "this", "road", "just", "walking", "Trying", "see", "through", "the", "rain", "coming", "Even", "though", "not", "only", "one", "who", "feels", "way", "do", "alone", "on", "my", "own", "And", "thats", "all", "Ill", "be", "strong", "wrong", "Oh", "but", "life", "goes", "a", "girl", "find", "place", "in", "world", "Got", "radio", "old", "blue", "jeans", "wearing", "heart", "sleeve", "Feeling", "lucky", "today", "got", "sunshine", "Could", "you", "tell", "more", "need", "tomorrows", "mystery", "yeah", "okay", "Maybe", "mission", "But", "ready", "fly", "oh", "Once", "upon", "time", "believe", "was", "Tuesday", "when", "caught", "your", "eye", "we", "onto", "something", "hold", "night", "looked", "and", "told", "loved", "Were", "kidding", "seems", "thing", "is", "breaking", "We", "almost", "never", "speak", "feel", "welcome", "anymore", "Baby", "happened", "Please", "second", "perfect", "now", "youre", "halfway", "door", "stare", "at", "phone", "he", "hasnt", "called", "then", "so", "low", "cant", "nothing", "flashback", "said", "Forever", "always", "rains", "bedroom", "Everything", "It", "here", "gone", "there", "Was", "of", "line", "Did", "say", "too", "honest", "made", "run", "hide", "Like", "scared", "little", "boy", "into", "eyes", "Thought", "knew", "for", "minute", "sure", "heres", "everything", "Heres", "silence", "that", "cuts", "core", "Where", "going", "You", "didnt", "mean", "baby", "think", "back", "up", "forget", "Back", "There", "again", "tonight", "Forcing", "laughter", "faking", "smiles", "Same", "tired", "lonely", "Walls", "insincerity", "shifting", "vacancy", "Vanished", "saw", "face", "All", "can", "enchanting", "meet", "Your", "whispered", "Have", "met", "Cross", "room", "silhouette", "Starts", "make", "its", "The", "playful", "conversation", "starts", "Counter", "quick", "remarks", "passing", "notes", "secrecy", "enchanted", "This", "sparkling", "let", "go", "wonderstruck", "blushing", "home", "spend", "forever", "wondering", "if", "lingering", "question", "kept", "AM", "love", "wonder", "til", "wide", "awake", "pacing", "forth", "Wishing", "were", "Id", "open", "would", "Hey", "That", "flawless", "dancing", "around", "praying", "very", "first", "page", "Not", "where", "story", "ends", "My", "thoughts", "will", "echo", "name", "until", "These", "are", "words", "held", "as", "leaving", "soon", "with", "someone", "else", "have", "somebody", "waiting", "like", "To", "dress", "hipsters", "fun", "our", "exes", "ah", "For", "breakfast", "midnight", "fall", "strangers", "Yeah", "happy", "free", "confused", "same", "Its", "miserable", "magical", "Tonights", "about", "deadlines", "uh", "feeling", "twenty", "two", "alright", "keep", "next", "bet", "If", "those", "nights", "crowded", "Too", "many", "cool", "kids", "Whos", "Taylor", "Swift", "anyway", "Ew", "ditch", "whole", "scene", "end", "dreaming", "instead", "sleeping", "best", "heartbreaks", "ifOoh", "ifAlright", "Twenty", "wont", "look", "bad", "news", "gotta", "Ooh", "ooh", "hey", "dance", "woah", "Stand", "ghost", "Shaking", "from", "insane", "ane", "Say", "been", "long", "six", "months", "afraid", "her", "how", "works", "Thats", "get", "worse", "or", "better", "wait", "ever", "Broke", "put", "together", "Remind", "used", "pictures", "frames", "kisses", "cheeks", "Tell", "mustve", "lost", "mind", "When", "left", "why", "could", "Pictures", "Theres", "glitter", "floor", "after", "party", "Girls", "carrying", "their", "shoes", "lobby", "Candle", "wax", "Polaroids", "hardwood", "before", "read", "last", "stay", "turning", "away", "midnights", "cleaning", "bottles", "New", "Years", "Day", "squeeze", "hand", "three", "times", "taxi", "gonna", "toast", "town", "babe", "Or", "strike", "crawling", "hard", "making", "mistakes", "Hold", "memories", "They", "become", "stranger", "Whose", "laugh", "recognize", "anywhere", "forevermore", "they", "leave", "Christmas", "lights", "January", "rules", "theres", "dazzling", "haze", "mysterious", "dear", "known", "seconds", "years", "Can", "close", "take", "Youre", "Lover", "friends", "crash", "living", "call", "highly", "suspicious", "everyone", "sees", "wants", "Ive", "summers", "honey", "em", "Ladies", "gentlemen", "please", "stand", "With", "every", "guitar", "string", "scar", "magnetic", "force", "man", "lover", "hearts", "borrowed", "yours", "has", "Alls", "well", "Swear", "overdramatic", "true", "youll", "save", "dirtiest", "jokes", "table", "seat", "Darling", "Salt", "air", "rust", "needed", "anything", "Whispers", "Are", "Never", "us", "memory", "August", "slipped", "moment", "mine", "twisted", "bedsheets", "sipped", "bottle", "wine", "beneath", "sun", "Wishin", "write", "Will", "school", "remember", "thinkin", "had", "changin", "Wanting", "enough", "live", "hope", "Cancel", "plans", "case", "youd", "behind", "mall", "much", "summer", "saying", "Us", "werent", "lose", "no", "Remember", "pulled", "Get", "car", "canceled", "livin", "Meet", "sit", "watch", "reading", "Head", "wake", "breathing", "Eyes", "closed", "notice", "older", "wiser", "by", "kid", "Use", "colors", "portrait", "Lay", "fancy", "tolerate", "head", "somehow", "should", "celebrated", "greet", "battle", "heros", "indiscretions", "good", "listen", "polish", "plates", "gleam", "glisten", "While", "building", "other", "worlds", "Wheres", "whod", "throw", "blankets", "over", "barbed", "wire", "temple", "mural", "sky", "Now", "begging", "footnotes", "Drawing", "byline", "Always", "taking", "space", "assume", "fine", "Break", "ruins", "Took", "dagger", "removed", "Gain", "weight", "Believe", "Midnights", "afternoons", "depression", "graveyard", "shift", "people", "ghosted", "devices", "come", "prices", "vices", "crisis", "tale", "screaming", "One", "day", "scheming", "hi", "problem", "At", "tea", "everybody", "agrees", "directly", "mirror", "must", "exhausting", "rooting", "anti", "hero", "Sometimes", "sexy", "monster", "hill", "big", "hang", "slowly", "lurching", "toward", "favorite", "city", "Pierced", "killed", "hear", "covert", "narcissism", "disguise", "altruism", "some", "kind", "congressman", "Tale", "meaning", "dream", "daughter", "law", "kills", "money", "She", "thinks", "them", "family", "gathers", "round", "reads", "screams", "Shes", "laughing", "whos", "poised", "attack", "bare", "hands", "paved", "paths", "sad", "wanted", "dead", "shouldve", "Nothing", "makes", "alive", "leap", "gallows", "levitate", "street", "Crash", "record", "scratch", "scream", "scandal", "contained", "bullet", "grazed", "costs", "Is", "broke", "Lets", "joke", "Then", "cry", "tame", "gentle", "till", "circus", "worry", "folks", "took", "teeth", "Well", "hurt", "did", "wanna", "snarl", "show", "disturbed", "wouldnt", "an", "hour", "asylum", "raised", "sneak", "house", "cobwebs", "drunk", "tears", "isnt", "sue", "step", "lawn", "fearsome", "wretched", "Put", "narcotics", "songs", "singing", "along", "lured", "taught", "caged", "crazy", "am", "cause", "trained"]
    

    def __init__(self, key_string):
        self.key_to_edit = key_string # Initialize the class with your key to encrypt/decrypt

    def encrypt_key(self) -> str:
        encrypted_key = ""
        for char in self.key_to_edit: # For loop to go through each char in the key
            ascii_value = ord(char) # Changing each char into an ascii value
            encrypted_key += self.unique_words_list[ascii_value] # Finding the ascii value corresponding word in the list and adding it to return string
            encrypted_key += str(random.randint(0, 10)) # Using an integer to seperate words

        # End of char in key to edit For Loop
        return encrypted_key # Returning encrypted key string
    
    def decrypt_key(self) -> str:
        decrypted_key = ""
        curr_word = ''
        curr_char = ''
        for char in self.key_to_edit: # For loop to go through each char in the key to edit 
            if char.isdigit(): # Checking if the current character is an int
                for i in range(len(self.unique_words_list)): # Looping through all words in words_list to find the accumulated word
                    if curr_word == self.unique_words_list[i]: # If it is an integer, the word breaks
                       ascii_letter = chr(i) # Changing the index of the found word back into it's original value
                       decrypted_key += ascii_letter # Adding the original char to the return
                # End of char in Uniq word list For Loop
                curr_char = '' # Resetting the current char
                curr_word = '' # Resetting the current word
                continue # Go to next char in key to edit
            # End of char being an int If Statement

            # If it is not an integer run below:
            curr_char = char # Getting the current char
            curr_word += char # Adding the char to an increasing string

        # End of char in key to edit For Loop
        return decrypted_key # Returning decrpyted key string


    
if __name__ == '__main__':
    # Actual key value
    key = 'PRBT0vrzqlKHG80x-HMqmm_B4F1gqEwjl-RiWIClo_w='

    # Create an object and encrypt the key
    swifty = SwiftSequencer(key)
    var = swifty.encrypt_key()
    print(f'{var}')

    # Create another object and decrypt the encrypted key
    swifty2 = SwiftSequencer(var)
    var2 = swifty2.decrypt_key()
    print(f'{var2}')

    # Print if the key matches
    if key == var2:
        print('Key matches original')
    