


def check():
    s1=input('Enter a string')
    s2=input('Enter another string')
    
    if(sorted(s1)== sorted(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")        
         

check()
