class GameStats:
	"""Monitorowanie statystyk gry."""

	def __init__(self, invasion_game):
		"""Inicjalizacja statystyk gry."""

		self.settings = invasion_game.settings
		self.reset_stats()

	def reset_stats(self):
		"""Inicjalizacja zmiennych danych:
		liczby pozostałych statków, wyniku, najlepszgo wyniku oraz poziomu."""

		self.ships_left = self.settings.ship_limit
		self.score = 0
		self.high_score = 0
		self.level = 1