#Import get_top_headlines from news module
from news import get_top_headlines

#Define Main Function
def main():
#Write Try/Except code for error Handling
    try:
        category = input("Enter category Ex: business, entertainment etc ...\n")
        
        if not category:
            raise
            
        status, response = get_top_headlines(category=category)
#Handle API response
        if status:
            for article in response['articles']:
                print(article['title'])
                print("\n")
        else:
            print("Error")
    except:
        print("Invalid input!. Please enter correct category")

if __name__ == "__main__":
    main()
