### Daveed A. Sumpter 3 December 2024  Programming Project # 10: PlayList

# For your final programming project, you will develop a program for the music buffs in your family. We will call it The Family Playlist! 
# The program will greet the user with a fun message and then present a menu asking them if they want to add music to the list OR see the list of songs already on the list. 
# If they choose to add, the program will allow them to enter a song one by one and store them in an external file called playlist.dat. 
# Once they are finished adding songs, they will be presented with the main menu of options again. 
# If they choose to see their list of songs, the program will read the records from the playlist.dat file and display them on the screen. 


def enterData():                         # This defines a function named enterData, which asks for input from the user.
    outfile = open("playlist.dat", "a")  # Use "a" to open the playlist.dat file in the append mode in order to  append more information.  Before a file can be used by a program, it must be opened. When a file is opened in the append mode, data will be written at the end of the file's existing contents.
    artist = input("Please enter the artist: ")  # The user will enter the name of the artist.
    song = input("Please enter the song: ")      # The user will enter the name of the song.
    outfile.write(artist+" : ")                  # This is an output file where data is written to. The name of the artist inputted by the user will be written to this output file.
    outfile.write(song+ "\n")   
    print("Data has been written to playlist.dat successfully!")                # This is an output file where data is written to. The name of the song inputted by the user will be written to this output file.
    outfile.close()       # This closes the output file.  We are finished using the file, so it should be closed.
    
    # prompt user if they would like to add another song to playlist
    # The addNewSong variable stores the input of the user in terms of whether they would like to add another artist and song to PLAYLIST.
    addNewSong = input("Would you like to add another artist and song to your PLAYLIST? Y/N?: ")
    # If user inputs 'Y' for yes, call the enterData function.
    if addNewSong == 'Y':
        enterData()
    # Any other input other than 'Y' will thank the user for adding songs to playlist and return to main menu
    else:
        print("Thank you for adding songs to the PLAYLIST. Returning to the main menu...")

def retrieveData():                                     # This defines a function named retrieveData, which asks for input from the user.
    searchInput = input("Please enter the name of an artist or song: ")    # The name of the artist or song inputted by the user is stored in a variable called searchInput, and a new line is created.                      
    playlist = open('playlist.dat', 'r')             # This opens the playlist.dat file in the read mode in order to read data from the file.  In this case, the names of the artists inputted by the user would be read, and stored in a variable called infile, which stands for input file.
    matchesFound = False                      # This boolean variable will indicate whether a match was found in the playlist.

    for match in playlist:                              # This is a for loop that will iterate each line in the playlist.dat file.
        if searchInput in match:                         # Check if the user's search input matches any lines in the playlist.
            print("A match was found for the name of the artist or song.")                              # If the condition is true, inform the user that a match was found.
            print(match)                                                                     # Print the match.
            matchesFound = True
                                                               # Set matchesFound variable to True to indicate a match was found.
    if not matchesFound:
        print("There were no matches found for the name of the artist or song.")                  # If the condition is false, inform the user that there were no matches found.
    playlist.close()                                 # This closes the playlist.dat file.


def main():
    while True:
        print("========================")
        print("Welcome to the FAMILY PLAYLIST. Enter the name of a musical artist or the title of a song to search for your songs.")       # This statement welcomes the user to the program and invites them to enter or search for songs.
        print()
        print("        MENU:")
        print("           1) Enter artist and song")
        print("           2) Retrieve artist music")
        print("           X) EXIT/n")    
        choice = input("Please make your selection: ")                 # The program will prompt the user to make a selection and store their input as a variable called choice.
        if choice == '1':                                                     # If the variable choice == 1, the enterData function will be called.
            enterData()
        elif choice == '2':                                                     # Else if the variable choice == 2, the retrieveData function will be called.
            retrieveData()
        elif choice == 'X' or choice == 'x':                                   # Else if the variable choice == X or x: then a statement will be printed and the program will be exited.
            print("Thank you for using PLAYLIST.")   
        else:                                                                  # If none of the above options are entered by the user, then a print statement will inform the user they have entered an invalid value.
            print("You have entered an invalid value. Please enter '1', '2' or 'X' to continue.")                        

main()                                                               # This calls the main module/function, which will welcome the user to the program again and invite them to enter or search for songs. The user must input 1 to enter name of artist and song. The user must input 2 to retrieve the artist's music. The user must input X to exit the program.