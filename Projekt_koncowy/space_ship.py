import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
	"""Klasa do obsługi statku kosmicznego."""

	def __init__(self, invasion_game):
		super().__init__()
		self.screen = invasion_game.screen
		self.settings = invasion_game.settings
		self.screen_rect = invasion_game.screen.get_rect()
		self.image = pygame.image.load('images/ship1.bmp')
		self.image = pygame.transform.smoothscale(self.image, (70, 70))
		self.rect = self.image.get_rect()

		# Położenie każdego nowego statku
		self.rect.midbottom = self.screen_rect.midbottom

		# Położenie poziome statku jest przechowywane w postaci liczby zmiennoprzecinkowej.
		self.x = float(self.rect.x)

		# Opcje wskazujące na poruszanie statku
		self.moving_right = False
		self.moving_left = False

	def update(self):
		# Uaktualniamy położenie statku na podstawie opcji, wskazującej na jego ruch.
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
		if self.moving_left and self.rect.left > 0:
			self.x -= self.settings.ship_speed

		self.rect.x = self.x

	def blitme(self):
		# Wyświetlenie statku w aktualnym położeniu
		self.screen.blit(self.image, self.rect)

	def center_ship(self):
		# Umieszczenie statku na środku przy dolnel krawędzi ekranu
		self.rect.midbottom = self.screen_rect.midbottom
		self.x = float(self.rect.x)