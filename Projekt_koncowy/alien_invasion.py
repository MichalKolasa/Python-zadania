import sys
from time import sleep
import pygame
from game_settings import Settings
from space_ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


class AlienInvasion:
    """Klasa do zarządzania zasobami i sposobem działania gry."""

    def __init__(self):
        """Inicjalizacja gry.

        Inicjalizuje:
        - tło,
        - statek gracza,
        - flotę obcych,
        - wskaźniki statystyk,
        - dźwięki gry.
        """

        pygame.init()
        pygame.mixer.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
			(self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.bg_image = pygame.image.load('images/image4.png').convert()
        self.bg_image = pygame.transform.scale(
            self.bg_image,
            (self.settings.screen_width, self.settings.screen_height)
        )

        # Utworzenie egzemplarza przechowującego statystyki gry
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        self.play_button = Button(self, "Graj")

        self.shoot_sound = pygame.mixer.Sound('sounds/shoot.wav')
        self.explosion_sound = pygame.mixer.Sound('sounds/explosion.wav')
        self.shoot_sound.set_volume(self.settings.shoot_volume)
        self.explosion_sound.set_volume(self.settings.explosion_volume)

        self.game_active = False


    def run_game(self):
        """Główna pętla gry."""

        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Reakcja na zdarzenia generowane przez klawiaturę i mysz."""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Obsługa przycisku "Graj"."""

        button_clicked = self.play_button.rect.collidepoint(mouse_pos)

        if button_clicked and not self.game_active:
            self.settings.initialize_dynamic_settings()

            # Wyzerowanie statystyk
            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            self.game_active = True

            # Sprzątanie
            self.bullets.empty()
            self.aliens.empty()

            # Nowa flota i wyśrodkowanie statku
            self._create_fleet()
            self.ship.center_ship()

            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        """Obsługa wcisniętych klawiszy K_RIGHT, K_LEFT i SPACE."""

        if event.key == pygame.K_RIGHT:
            # przesuwamy statek w prawo
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # przesuwamy statek w lewo
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Obsługa zwolnionych klawiszy K_RIGHT, K_LEFT"""

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Tworzy nowy pocisk i dodaje go do grupy pocisków."""

        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            self.shoot_sound.play()

    def _update_bullets(self):
        """Uaktualnia położenia pocisków i usuwa niewidoczne."""

        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Reakcja na kolizję między pociskiem i obcym"""

        # Sprawdzenie, czy jakiś pocisk trafił obcego. Jeśli tak usuwamy go wraz
        # z pociskiem.
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

        if collisions:
            self.explosion_sound.play()
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            # pozbycie się istniejących pocisków i utworzenie nowej floty
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # Inkrementacja poziomu gry
            self.stats.level += 1
            self.sb.prep_level()

    def _create_fleet(self):
        """Tworzy pełną flotę obcych"""

        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height * 2
        while current_y < (self.settings.screen_height - 8 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            # ukończenie rzędu, wyzerowanie wartości x oraz inkrementacja y
            current_x = alien_width
            current_y += 2 * alien_height

    def _update_aliens(self):
        """Aktualizuje położenie wszystkich obcych we flocie.

        Wykrywa kolizję między obcym i statkiem.
        Sprawdza, czy jakiś obcy dotarł do dolnej krawędzi ekranu."""

        # Położenie wszytkich obcych we flocie
        self._check_fleet_edges()
        self.aliens.update()

        # Wykrywanie kolizji między obcym i statkiem
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Sprawdzanie, czy jakiś obcy dotarł do dolnej krawędzi ekranu
        self._check_aliens_bottom()


    def _create_alien(self, x_position, y_position):
        """Tworzy obcego i umieszcza go w rzędzie"""

        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        """Zmienia kierunek floty, gdy ta dojdzie do końca ekranu."""

        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Przesuwa flotę w dół i zmienia jej kierunek na przeciwny"""

        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        """Reakcja na uderzenie obcego w statek.

        Zmniejsza ilość pozostałych statków i resetuje poziom."""

        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            # Sprzątanie
            self.bullets.empty()
            self.aliens.empty()

            # Nowa flota
            self._create_fleet()
            self.ship.center_ship()

            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        """Sprawdzan, czy jakikolwiek obcy dotarł do dolnej krawędzi ekranu"""

        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit()
                break

    def _update_screen(self):
        """Uaktualnia elementy na ekranie i przechodzi do nowego ekranu"""

        self.screen.blit(self.bg_image, (0, 0))

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)

        self.sb.show_score()

        if not self.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

if __name__ == '__main__':
    invasion = AlienInvasion()
    invasion.run_game()