import random
from terminaltables import AsciiTable
import curses

GAME_TITLE = "`•.,¸¸ [ JEU DU TAQUIN ] ¸¸,.•´"

# Nombre de cases par côté
TAQUIN_SIZE = 5

# Valeur de la case vide
EMPTY_CASE_VALUE = ""


# Taquin correct, dans l'ordre
CORRECT_SOLUTION = [list(a) for a in zip(*[iter(list(range(1, TAQUIN_SIZE ** 2)) + [EMPTY_CASE_VALUE])] * TAQUIN_SIZE)]


# Jeu en cours
CURRENT_STATE = []


def get_available_movements():
    # TODO : retourner une liste de mouvements possibles ["LEFT", "UP"]
    return []


def move(movement):
    # TODO : appliquer le mouvement de la case vide
    pass


def has_won(movement):
    # TODO : vérifier si le jeu est gagné
    pass


def handle_keypress(screen):
    try:
        key = screen.getkey().upper()
    except:
        return

    height, width = screen.getmaxyx()
    screen.erase()
    available_movements = get_available_movements()

    if key == "KEY_DOWN":
        screen.addstr(height - 1, 0, "↓ DOWN - A FAIRE", curses.A_REVERSE)
        if "DOWN" in available_movements:
            move("DOWN")

    elif key == "KEY_UP":
        screen.addstr(height - 1, 0, "↑ UP - A FAIRE", curses.A_REVERSE)
        if "UP" in available_movements:
            move("UP")

    elif key == "KEY_LEFT":
        screen.addstr(height - 1, 0, "← LEFT - A FAIRE", curses.A_REVERSE)
        if "LEFT" in available_movements:
            move("LEFT")

    elif key == "KEY_RIGHT":
        screen.addstr(height - 1, 0, "→ RIGHT - A FAIRE", curses.A_REVERSE)
        if "RIGHT" in available_movements:
            move("RIGHT")

    elif key in ("Q",):
        raise KeyboardInterrupt


def get_current_state_str():
    global CURRENT_STATE
    table = AsciiTable(CURRENT_STATE)
    table.inner_heading_row_border = False
    table.inner_row_border = True
    table.justify_columns[0] = "center"
    table.justify_columns[1] = "center"
    return table.table


def display_output(screen):
    # Title
    screen.addstr(0, 0, GAME_TITLE, curses.color_pair(1))

    # Table game
    screen.addstr(2, 0, get_current_state_str(), curses.color_pair(1))

    # Controls
    screen.addstr(4 + TAQUIN_SIZE * 2, 0, "Utiliser les flêches pour déplacer la case vide.")
    screen.addstr(5 + TAQUIN_SIZE * 2, 0, "(r)eset | (s)olution | (q)uitter")


def init_state():
    global CURRENT_STATE
    cases = list(range(1, TAQUIN_SIZE ** 2)) + [EMPTY_CASE_VALUE]
    random.shuffle(cases)
    CURRENT_STATE = [list(a) for a in zip(*[iter(cases)] * TAQUIN_SIZE)]


def main():
    """Fonction principale de l'application"""
    try:
        # Initalisation de l'UI
        stdscr = curses.initscr()
        curses.start_color()
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)
        curses.noecho()
        stdscr.keypad(True)
        stdscr.nodelay(True)

        # Récupération d'un taquin tiré aléatoirement
        init_state()

        while True:
            # Attend une action et affiche le résultat
            handle_keypress(stdscr)
            display_output(stdscr)

            # Frequence de rafraichissement
            curses.napms(50)  # ms
    except KeyboardInterrupt:
        pass
    finally:
        # Lorsqu'on quite, on restaure l'environnement du terminal
        curses.nocbreak()
        stdscr.keypad(False)
        curses.echo()
        curses.endwin()


if __name__ == "__main__":
    main()
