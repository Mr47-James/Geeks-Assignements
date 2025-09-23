# NOTE THESE IS SCRIPT IS UPGRADED IT TAKE THE USER INPUT FOR BETTER HANDLING AND, THE FUNCTION CALL DOESN'T NEED TO BE CALLED WITH THE KEYWORD ARGS, SINCE THE FUNCTION INTERNALLY PARSES THE USER COMMANDS.

def make_shirt(size=None, text=None):
    
    if size is None:
        size = input("Put in your size (default L): ") or "L"
    
    if text is None:
        text = input("Put in your text (default 'I love Python'): ") or "I love Python"

    
    if size == "L":
        print("\nDefault Size chosen: L")
    else:
        print(f"\nSize Chosen: {size}")

    if text == "I love Python":
        print("\nText Chosen is: I love Python")
    else:
        print(f"\nText Chosen is: {text}")

    print(f"\nThe size of the shirt is {size} and the text is {text}")    


make_shirt()                     
      



