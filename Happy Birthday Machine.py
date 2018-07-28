# May Pena

# This program sings happy birthday to all the names the user inputs
# and it outputs the song hugged by a box!

def happyBirthday( length ):
    HBD = "Happy birthday to you!"
    print( "|", HBD.center( length - 2), "|" )

def happyBirthdayDear( name, length ):
    HBD = "Happy birthday, dear " + name + "!"
    print( "|" + HBD.center( length ) + "|" )

def singSong( name, length ):
   bar = "+" + "-" * (length) + "+"
   print( bar )
   happyBirthday(length)
   happyBirthday(length)
   happyBirthdayDear( name, length )    
   happyBirthday(length)
   print( bar )

def main():
    name   = input("Who should we sing for? " ).title()
    print()

    listOfNames = name.split()
    for name in ( listOfNames ):
        length = len( "Happy birthday, dear " + name + "!" )
        singSong( name, length )
        print()
    
main()
