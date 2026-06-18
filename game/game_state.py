class GameState:

    def __init__(self):

        # flow
        self.game_state = "menu"   # menu / playing / win / lose / level_complete
        self.current_level = 1

        # player
        self.player_x = 0
        self.player_y = 0
        self.player_state = "alive"   # alive / respawning / dead
        self.respawn_timer = 0

        # stats
        self.score = 0
        self.lives = 3

        # world
        self.map_data = None
        self.rows = 0
        self.cols = 0

        self.walls = []
        self.dots = []
        self.ghosts = []

        # UI timers
        self.level_complete_timer = 0

        # audio flags
        self.menu_started = False
        self.menu_music_played = False