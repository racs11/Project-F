# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Salinas = Character("Salinas")
image SS:
    "images/Salinas.png"
    zoom 1.5
image salon:
    zoom 1.75
    "salon.png"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene salon

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show SS

    # These display lines of dialogue.

    Salinas "Chicos! Sé que esta no es la parte más sexy del bloque...."

    Salinas "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
