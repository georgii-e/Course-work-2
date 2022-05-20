import pygame

pygame.init()


class SoundControl:
    SOUNDS_ON = True

    def __init__(self):
        if self.SOUNDS_ON:
            self.success_sound = pygame.mixer.Sound("media/success.wav")
            self.sorting_sound = pygame.mixer.Sound("media/sorting.mp3")
            self.presskey_sound = pygame.mixer.Sound("media/presskey.mp3")
            self.mouseclick_sound = pygame.mixer.Sound("media/mouseclick.mp3")

    def play_sounds(self, name):
        if self.SOUNDS_ON:
            if name == "success":
                self.success_sound.play()
            elif name == "sorting":
                self.sorting_sound.play(-1)
            elif name == "press key":
                self.presskey_sound.play()
            elif name == "mouse click":
                self.mouseclick_sound.play()


    def stop_sounds(self, name="sorting"):
        if self.SOUNDS_ON:
            if name == "sorting":
                self.sorting_sound.stop()
