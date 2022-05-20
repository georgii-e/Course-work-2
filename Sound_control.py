import pygame
import Config

pygame.init()


class SoundControl:
    """Клас для вмикання/вимикання звукових ефектів"""
    def __init__(self):
        """Оголошення mp3 доріжок"""
        self.sounds_on = Config.SOUNDS_ON
        if self.sounds_on:
            self.__success_sound = pygame.mixer.Sound("media/success.wav")
            self.__sorting_sound = pygame.mixer.Sound("media/sorting.mp3")
            self.__presskey_sound = pygame.mixer.Sound("media/presskey.mp3")
            self.__mouseclick_sound = pygame.mixer.Sound("media/mouseclick.mp3")

    def play_sounds(self, name):
        """Вмикання звуків"""
        if self.sounds_on:
            if name == "success":
                self.__success_sound.play()
            elif name == "sorting":
                self.__sorting_sound.play(-1)
            elif name == "press key":
                self.__presskey_sound.play()
            elif name == "mouse click":
                self.__mouseclick_sound.play()

    def stop_sounds(self, name="sorting"):
        """Вимикання звуків"""
        if self.sounds_on:
            if name == "sorting":
                self.__sorting_sound.stop()
