# Alien Invasion
**Alien Invasion** to prosta gra typu *space shooter* napisana w języku **Python**
z wykorzystaniem biblioteki **pygame**.  
Projekt ma charakter edukacyjny i demonstruje m.in.:

- programowanie obiektowe,
- obsługę zdarzeń (klawiatura, mysz),
- kolizje sprite’ów,
- dźwięk i grafikę 2D,
- strukturę większego projektu w Pythonie.  

Celem gracza jest zestrzelenie całej floty obcych nim ta dojdzie na dół ekranu,
bądź uderzy statek gracza. 
  
## Wymagania:

- Python 3.10+
- pygame

Instalacja pygame:  
bash: pip install pygame
  
## Interfejs:  
Po uruchomieniu gry na środku ekranu będzie widoczny przycisk **Graj**, którego 
naciśnięcie rozpocznie rozgrywkę.   
Liczba pozostałych statków widoczna jest w lewym górnym rogu ekranu.
Na środku ekranu widoczny jest najwyższy uzyskany w rozgrywce wynik, po prawej obecny wynik,
pod nim nr poziomu.
## Sterowanie z klawiatury:
- **strzałka w prawo** - ruch statkiem w prawo
- **strzałka w lewo** - ruch statkiem w lewo
- **spacja** - wystrzel pocisk
  
## Liczba żyć, poziomy rozgrywki:  
Gracz ma do dyspozycji trzy życia (statki), jeśli któryś z obcych uderzy statek gracza
to gracz traci jedno życie i zaczyna poziom od nowa. Po utracie wszystkich żyć gracz
zaczyna całą rozgrywkę od nowa, tracąc cały dotychczasowy postęp. Poziom trudności gry wzrasta
po ukończeniu każdego poziomu (zestrzeleniu całej floty) - wzrasta prędkość poruszania się obcych.


# Struktura projektu
Projekt składa się z następujących klas i metod w nich zawartych:  
  
## class AlienInvasion  
***Klasa do zarządzania zasobami i sposobem działania gry.*** 
### def run_game(self)  
Główna pętla gry - nasłuchiwanie zdarzeń pochodzących z klawiatury i myszy, odświeżanie 
ekranu i elementów dynamicznych gry.  

**Metody pomocnicze w tej klasie:** 
- **def _check_events(self)** - Reakcja na zdarzenia generowane przez klawiaturę i mysz.  


- **def _check_play_button(self, mouse_pos)** - Obsługa przycisku "Graj".  


- **def _check_keydown_events(self, event)** - Obsługa wcisniętych klawiszy K_RIGHT, K_LEFT i SPACE.  


- **def _check_keyup_events(self, event)** - Obsługa zwolnionych klawiszy K_RIGHT, K_LEFT.  


- **def _fire_bullet(self)** - Tworzy nowy pocisk i dodaje go do grupy pocisków.  


- **def _update_bullets(self)** - Uaktualnia położenia pocisków i usuwa niewidoczne.  


- **def _check_bullet_alien_collisions(self)** - Reakcja na kolizję między pociskiem i obcym.  


- **def _create_fleet(self)** - Tworzy pełną flotę obcych.  


- **def _update_aliens(self)** - Aktualizuje położenie wszystkich obcych we flocie. Wykrywa kolizję między obcym i statkiem.
        Sprawdza, czy jakiś obcy dotarł do dolnej krawędzi ekranu.  


- **def _create_alien(self, x_position, y_position)** - Tworzy obcego i umieszcza go w rzędzie.  


- **def _check_fleet_edges(self)** - Zmienia kierunek floty, gdy ta dojdzie do końca ekranu.  


- **def _change_fleet_direction(self)** - Przesuwa flotę w dół i zmienia jej kierunek na przeciwny.  


- **def _ship_hit(self)** - Reakcja na uderzenie obcego w statek. Zmniejsza ilość pozostałych statków i resetuje poziom.  


- **def _check_aliens_bottom(self)** - Sprawdza, czy jakikolwiek obcy dotarł do dolnej krawędzi ekranu.  


- **def _update_screen(self)** - Uaktualnia elementy na ekranie i przechodzi do nowego ekranu.

## class Settings  
***Klasa przechowująca ustawienia gry.***  
### def initialize_dynamic_settings(self)
Inicjalizacja ustawień, ulegających zmianom w trakcie gry.
### def increase_speed(self)
Zmiana ustawień dotyczących szybkości.
## class GameStats  
***Klasa do monitorowania statystyk gry.***  
### def reset_stats(self)
Inicjalizacja zmiennych danych: liczby pozostałych statków, wyniku, najlepszgo wyniku oraz poziomu.
## class Scoreboard  
***Klasa przeznaczona do przedstawiania informacji o punktacji.***
### def prep_score(self)
Przekształca punktację na wygenerowany obraz.
### def prep_high_score(self)
Przekształca najlepszy wynik na wygenerowany obraz.
### def prep_level(self)
Przekształca numer poziomu na wygenerowany obraz.
###	def check_high_score(self)
Sprawdza, czy mamy nowy najlepszy wynik osiągnięty dotąd w grze.
###	def prep_ships(self)
Wyświetla liczbę statków, jakie pozostały graczowi.
###	def show_score(self)
Wyświetla punktacje na ekranie.
## class Ship(Sprite)  
***Klasa do obsługi statku kosmicznego gracza.***
###	def update(self)
Uaktualnia położenie statku na podstawie opcji, wskazującej na jego ruch.
###	def blitme(self)
Wyświetla statek w aktualnym położeniu.
###	def center_ship(self)
Umieszcza statek na środku przy dolnej krawędzi ekranu.
## class Alien(Sprite)  
***Klasa reprezentująca pojedynczego obcego we flocie.***  
###	def check_edges(self)
Sprawdza, czy obcy nie wychodzi poza ekran.
###	def update(self)
Przesuwa obcego w prawo.
## class Bullet(Sprite)  
***Klasa do zarządzania pociskami wystrzeliwanymi przez statek.***
###	def update(self)
Porusza pociskiem po ekranie.
###	def draw_bullet(self)
Wyświetla pocisk na ekranie.
## class Button  
***Klasa do tworzenia przycisków dla gry.***
###	def _prep_msg(self, msg)
Tworzy z napisu obraz do wyświetlenia.  
###	def draw_button(self)
Wyświetla przycisk.
### Źródła materiałów audio i grafik wykorzystanych w grze:
    - audio: https://freesound.org/
    - grafiki: https://opengameart.org/
Oryginalna wersja projektu pochodzi z książki ***Python Crash Course*** autorstwa
Erica Matthes.