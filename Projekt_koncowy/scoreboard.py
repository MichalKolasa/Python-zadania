import pygame.font
from pygame.sprite import Group
from space_ship import Ship

class Scoreboard:
	"""Klasa przeznaczona do przedstawiania informacji o punktacji."""

	def __init__(self, invasion_game):
		self.invasion_game = invasion_game
		self.screen = invasion_game.screen
		self.screen_rect = invasion_game.screen.get_rect()
		self.settings = invasion_game.settings
		self.stats = invasion_game.stats

		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont('None', 48)

		self.prep_score()
		self.prep_high_score()
		self.prep_level()
		self.prep_ships()

	def prep_score(self):
		# Przekształcenie punktacji na wygenerowany obraz
		score_str = str(self.stats.score)
		self.score_image = self.font.render(score_str, True,
											self.text_color, None)

		# Wyświetlenie punktacji w prawym górnym rogu
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20

	def prep_high_score(self):
		# Przekształcenie najlepszego wyniku na wygenerowany obraz
		high_score_str = str(self.stats.high_score)
		self.high_score_image = self.font.render(high_score_str, True,
												 self.text_color, None)

		# Wyświetlenie najlepszego wyniku w grze
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = self.score_rect.top

	def prep_level(self):
		# Przekształcenie numeru poziomu na wygenerowany obraz
		level_str = str(self.stats.level)
		self.level_image = self.font.render(level_str, True,
		self.text_color, None)

		# Numer poziomu jest wyświetlany pod aktualną punktacją.
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.score_rect.right
		self.level_rect.top = self.score_rect.bottom + 10

	def check_high_score(self):
		# Sprawdzenie, czy mamy nowy najlepszy wynik osiągnięty dotąd w grze
		if self.stats.score > self.stats.high_score:
			self.stats.high_score = self.stats.score
			self.prep_high_score()

	def prep_ships(self):
		# Wyświetla liczbę staków, jakie pozostały graczowi
		self.ships = Group()
		for ship_number in range(self.stats.ships_left):
			ship = Ship(self.invasion_game)
			ship.rect.x = 10 + ship_number * ship.rect.width
			ship.rect.y = 10
			self.ships.add(ship)

	def show_score(self):
		# Wyświetlenie punktacji na ekranie
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.high_score_image, self.high_score_rect)
		self.screen.blit(self.level_image, self.level_rect)
		self.ships.draw(self.screen)

