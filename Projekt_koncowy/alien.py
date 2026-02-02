import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
	"""Klasa reprezentująca pojedynczego obcego we flocie."""

	def __init__(self, invasion_game):
		# Inicjalizacja obcego + położenia początkowego
		super().__init__()
		self.screen = invasion_game.screen
		self.settings = invasion_game.settings
		self.image = pygame.image.load('images/Nave.bmp')
		self.image = pygame.transform.smoothscale(self.image, (70, 40))
		self.rect = self.image.get_rect()
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		self.x = float(self.rect.x)

	def check_edges(self):
		screen_rect = self.screen.get_rect()
		return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

	def update(self):
		# Przesunięcie obcego w prawo
		self.x += self.settings.alien_speed * self.settings.fleet_direction
		self.rect.x = self.x