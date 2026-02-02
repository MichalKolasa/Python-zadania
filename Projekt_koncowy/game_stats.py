class GameStats:
	"""Monitorowanie statystyk gry."""

	def __init__(self, invasion_game):
		self.settings = invasion_game.settings
		self.reset_stats()

	def reset_stats(self):
		# Inicjalizacja zmiennych danych
		self.ships_left = self.settings.ship_limit
		self.score = 0
		self.high_score = 0
		self.level = 1