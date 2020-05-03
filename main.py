import pygame # Load the popular external library

pygame.mixer.init()


options = ['sound.mp3','Applause.mp3', 'boo.mp3', 'itu.mp3']

while True:
    print("\nselect song")
    opt = int(input(">>>"))
    if (opt != 0):
        if (opt == 9):
            pygame.mixer.music.play()
        else:
            try:
                pygame.mixer.music.load(options[opt-1])
                pygame.mixer.music.play()
            except:
                print("ta deg sammen")
                print("format:")
                print("1: defying, 2: applause, 3: boo, 4: itu, 0: pause")
                print("['sound.mp3','Applause.mp3', 'boo.mp3', 'itu.mp3']")
    else:
        pygame.mixer.music.pause()