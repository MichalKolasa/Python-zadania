import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
	"""Klasa do zarządzania pociskami wystrzeliwanymi przez statek."""

	def __init__(self, invasion_game):
		"""Utworzenie pocisku w aktualnym położeniu statku."""

		super().__init__()
		self.screen = invasion_game.screen
		self.settings = invasion_game.settings
		self.color = self.settings.bullet_color

		# Utworzenie prostokąta pocisku w punkcie (0, 0), a następnie
		# zdefiniowanie dla niego odpowiedniego położenia.
		self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
			self.settings.bullet_height)
		self.rect.midtop = invasion_game.ship.rect.midtop

		self.y = float(self.rect.y)

	def update(self):
		"""Porusza pociskiem po ekranie."""

		self.y -= self.settings.bullet_speed
		self.rect.y = self.y

	def draw_bullet(self):
		"""Wyświetla pocisk na ekranie."""

		pygame.draw.rect(self.screen, self.color, self.rect)