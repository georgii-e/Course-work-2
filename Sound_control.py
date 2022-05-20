import pygame
import Config

pygame.init()


class SoundControl:

    def __init__(self):
        self.sounds_on = Config.SOUNDS_ON
        if self.sounds_on:
            self.success_sound = pygame.mixer.Sound("media/success.wav")
            self.sorting_sound = pygame.mixer.Sound("media/sorting.mp3")
            self.presskey_sound = pygame.mixer.Sound("media/presskey.mp3")
            self.mouseclick_sound = pygame.mixer.Sound("media/mouseclick.mp3")

    def play_sounds(self, name):
        if self.sounds_on:
            if name == "success":
                self.success_sound.play()
            elif name == "sorting":
                self.sorting_sound.play(-1)
            elif name == "press key":
                self.presskey_sound.play()
            elif name == "mouse click":
                self.mouseclick_sound.play()

    def stop_sounds(self, name="sorting"):
        if self.sounds_on:
            if name == "sorting":
                self.sorting_sound.stop()
