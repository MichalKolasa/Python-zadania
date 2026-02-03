class Settings:
	"""Klasa przechowująca ustawienia gry."""

	def __init__(self):
		"""Inicjalizacja ustawień wstępnych.

		Ustawienia wstępne: ekranu, statku, pocisku, obcego, szybkości
		rozgrywki oraz dźwięku."""

		# Ustawienia ekranu
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (25, 20, 50)

		# Ustawienia statku
		self.ship_limit = 3
		self.ship_speed = 7.5

		# Ustawienia pocisku
		self.bullet_width = 10
		self.bullet_height = 30
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 3
		self.bullet_speed = 6.5

		# Ustawienia obcego
		self.fleet_drop_speed = 10

		# Zmiana szybkości rozgrywki
		self.speedup_scale = 1.1

		self.initialize_dynamic_settings()

		# Ustawienia dźwięków
		self.shoot_volume = 0.5
		self.explosion_volume = 1

	def initialize_dynamic_settings(self):
		"""Inicjalizacja ustawień, ulegających zmianom w trakcie gry."""

		self.alien_speed = 1.0

		self.fleet_direction = 1

		self.alien_points = 1

	def increase_speed(self):
		"""Zmiana ustawień dotyczących szybkości."""

		self.alien_speed *= self.speedup_scale