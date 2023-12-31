
![](./robots.png)

Welcome to the big bot poker tournament!
In this tournament we will be using [the PyPokerEngine](https://ishikota.github.io/PyPokerEngine/). 

Do not forget to install the library.

```console
foo@bar:~$ pip install PyPokerEngine
```

[tournament.py](https://github.com/kr0niker/poker/blob/main/tournament.py) contains a simple simulation function for a game with 10 players, where each starts with 1000 in chips. These are the starting conditions for your bot as well. 

The repository also contains three standard players:
1. [Fishes](https://github.com/kr0niker/poker/blob/main/fishplayer.py). This guys calls everything as long as they can.
2. [Random](https://github.com/kr0niker/poker/blob/main/randomplayer.py). You guessed it. You can play with how often they call, fold or raise. You can also think about the gistribution for the raises.
3. [Honest](https://github.com/kr0niker/poker/blob/main/honestplayer.py). This one is using the <code>estimate_hole_card_win_rate()</code> for MonteCarlo simulation of the outcomes. See, [source](https://github.com/ishikota/PyPokerEngine/blob/master/pypokerengine/utils/card_utils.py) for more details.

You need to develop a bot similar to the ones listed above. Here is how we run the final tournament.

1. You submit the bots by Wednesday next week.
2. The bots are randomly assigned to two starting tables with 2 additional random and 3 fish players.
3. The tables start with 1000 credits and run for max of 1000 games.
4. The 2 best bots (in terms of the final amount of chips) on each of the two semi-final tables are chosen to play in the final.
5. The final is between 4 best of your bots 2 random players and 4 fishes.





