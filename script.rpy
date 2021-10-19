# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define w = Character("will")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene coolbg

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show will_happpy

    # These display lines of dialogue.

    w "hi."

    w "this is an test build for this game."

    w "for what?"

    w "testing if the images work."

    w "so if you see me right now, i guess the images work."

    # This ends the game.

    return
