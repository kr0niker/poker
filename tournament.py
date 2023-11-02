from pypokerengine.api.game import setup_config, start_poker
from fishplayer import FishPlayer
from randomplayer import RandomPlayer
from honestplayer import HonestPlayer

#we initialize 10 players. 4 fishes, 4 randoms and 2 honest ones.

config = setup_config(max_round=100, initial_stack=1000, small_blind_amount=20)
config.register_player(name="f1", algorithm=FishPlayer())
config.register_player(name="f2", algorithm=FishPlayer())
config.register_player(name="f3", algorithm=FishPlayer())
config.register_player(name="f4", algorithm=FishPlayer())
config.register_player(name="r1", algorithm=RandomPlayer())
config.register_player(name="r2", algorithm=RandomPlayer())
config.register_player(name="r3", algorithm=RandomPlayer())
config.register_player(name="r4", algorithm=RandomPlayer())
config.register_player(name="h1", algorithm=HonestPlayer())
config.register_player(name="h2", algorithm=HonestPlayer())
game_result = start_poker(config, verbose=1)
