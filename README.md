# Welcome to the big bot poker tournament!

![alt text](https://github.com/kr0niker/poker/blob/main/robots.png)

In this tournament we will be using [the PyPokerEngine](https://ishikota.github.io/PyPokerEngine/). 

First, install the library.

```console
foo@bar:~$ pip install PyPokerEngine
```

(tournament.py)[https://github.com/kr0niker/poker/blob/main/tournament.py] contains a simple simulation function for a game with 10 players, where each starts with 1000 in chips. These are the starting conditions for your bot as well. 

The repository also contains three standard players:
1. (Fishes)[https://github.com/kr0niker/poker/blob/main/fishplayer.py]. This guys calls everything as long as they can.
2. (Random)[https://github.com/kr0niker/poker/blob/main/randomplayer.py]. You guessed it. You can play with how often they call, fold or raise. You can also think about the gistribution for the raises.
3. (Honest)[https://github.com/kr0niker/poker/blob/main/honestlayer.py]. This one is using the <code>estimate_hole_card_win_rate()</code> for MonteCarlo simulation of the outcomes. See, [source](https://github.com/ishikota/PyPokerEngine/blob/master/pypokerengine/utils/card_utils.py) for more details.

You need to develop a bot similar to the ones listed above. We will initiate the game with all the bots of the participants + three honest ones. We will have three runs to determine the winners. Good luck! Let the best player win!



