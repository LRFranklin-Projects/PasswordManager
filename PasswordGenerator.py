import random

class PasswordGenerator:
    # Tuple that contains characters for the password to hold
    valid_chars = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
                  '1', '2', '3', '4', '5', '6', '7', '8', '9',
                  '!', '@', '$', '?'
                  )
    length = 0

    # Object initialization with optional length setting
    def __init__(self, length=8):
        self.length = length # Setting the default length to 8

    # Function to generate a password and guarantee a capital, special character, and number
    def get_random_password(self) -> str:
        strength_checker = {'Upper': False, 'SpecialChar': False, 'Number': False} # Create key value pair for requirements
        random_password = ""

        # While loop will keep repeating until the password meets the requirements
        while not all(strength_checker.values()):
            # Resetting requirements and password
            strength_checker = {'Upper': False, 'SpecialChar': False, 'Number': False}
            random_password = ""
            
            for i in range(self.length): # For loop to generate a random password with object length
                pick = random.randint(0, len(self.valid_chars) - 1)

                # Picking a  random int and then deciding if it will be capital
                if random.randint(0, 10) < 2 and pick < 26:
                    # 2/10 Chance for the character to be uppercase
                    curr_char = self.valid_chars[pick].upper()
                    strength_checker['Upper'] = True
                else:
                    curr_char = self.valid_chars[pick]

                # Ensuring there is a number
                if 26 <= pick <= 34:
                    strength_checker['Number'] = True
                
                # Ensuring there is a special character
                if pick > 34:
                    strength_checker['SpecialChar'] = True

                random_password += curr_char
            # End of the for loop
        # End of the while loop

        print(f'Here is the random password: {random_password}')
        print(f'Here is the length of the password: {len(random_password)}')
        return random_password
# End of ClassS

if __name__ == "__main__":
    pg = PasswordGenerator(18)
    pg.get_random_password()
