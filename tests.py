import arcade 
import os 
import json 
settings = {
    "graphics": {
        "fullscreen": False,
        "windowed": True,
        "borderless": False,
        "vsync": False,
        "max_fps": 60,
    },
    "keybinding": {
        "forward": arcade.key.W,
        "left": arcade.key.A,
        "backward": arcade.key.S,
        "right": arcade.key.D,
        "attack": arcade.MOUSE_BUTTON_LEFT,

        "inventory": arcade.key.TAB,
        "run": arcade.key.LSHIFT,
        "crouch": arcade.key.LCTRL,
        "menu": arcade.key.ESCAPE,
    },
    "sounds": {
        "master_volume": 100 ,
        "music_volume": 100,
        "sfx_volume": 100,
        "mute_all": False,
    }
}

# --- SAVE --- # 
def save():
    with open ("settings.json", "w") as f: 
        json.dump(settings, f, indent=4, ensure_ascii=False)

class Game(arcade.Window):
    def __init__(self):
        super().__init__(640, 360, "Game", vsync=settings["graphics"]["vsync"])
        self.player = arcade.SpriteCircle(radius=10, color=arcade.color.WHITE)
        self.player.center_x = 320
        self.player.center_y = 180
        self.player.change_x = 0
        self.player.change_y = 0
        self.player_list = None
        self.hud_sprites = None
    def setup(self):
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player)
        self.hud_sprites = arcade.SpriteList()
        hp_sprite = arcade.Sprite("здоровье.png", scale=1.5)
        hp_sprite.center_x = 150 
        hp_sprite.center_y = 320
        self.hud_sprites.append(hp_sprite)
 
    def on_key_press(self, key, modifiers):
        if key == settings['keybinding']['forward']: 
            self.player.change_y = 5 
        elif key == settings['keybinding']['left']:
            self.player.change_x = -5
        elif key == settings['keybinding']['backward']:
            self.player.change_y = -5
        elif key == settings['keybinding']['right']:
            self.player.change_x = 5
    def on_key_release(self, key, modifiers):
        if key == settings['keybinding']['forward'] or key == settings['keybinding']["backward"]: 
            self.player.change_y = 0
        elif key == settings['keybinding']['left'] or key == settings['keybinding']["right"]:
            self.player.change_x = 0
    def on_update(self, delta_time):
        self.player_list.update()
    def on_draw(self):
        self.clear()
        self.hud_sprites.draw()
        self.player_list.draw()
if __name__ == "__main__":
    window = Game()
    window.setup()
    arcade.run()
