# Q-Learning on Maze Game

A bot is placed in a maze with walls, negative blocks and positive blocks. The goal is to find the shortest path to one of the positive blocks which maximizes the reward. 

Some large maps (100x100),

![](/samples/large1.png?raw=true "Large Map 1")
![](/samples/large2.png?raw=true "Large Map 2")
![](/samples/large3.png?raw=true "Large Map 3")

Smaller maps (50x50),

![](/samples/small1.png?raw=true "Small Map 1")
![](/samples/small2.png?raw=true "Small Map 2")


## Q Learning Challenge

Q Learning challenge by @Sirajology on [Youtube](https://youtu.be/A5eihauRQvo)

## Dependencies

- Python 2.7
- tkinter
- numpy

If on Ubuntu you can install tkinter for python2.7 with
$sudo apt-get install python-tk

## Usage

Run `python Learner.py` in terminal to see the the bot in action. It'll keep trying various paths until it finds the optimal strategy and then follows that from then onwards.

## Features added

* Player randomly initialized at a position where there is no wall
* Walls are generated using cellular automata. More details about this [here](http://natureofcode.com/book/chapter-7-cellular-automata/)
* World size is 50x50 (Can be changed as required)
* Red (Negative blocks) and Green (Positive blocks) are generated at random positions where no walls are present. The number of each of these blocks is configurable, currently 3 Red and 2 Green blocks are generated.
* Exploration/exploitation tradeoff so that the bot initially choses actions at random (since initially the Q table has random values) and then slowly over time chooses actions based on the Q Table.
* Limit total moves to 5000 after which the bot restarts (helpful when the bot gets stuck at some area of the map) and reduce sleep time so the iterations happen faster and we get results quicker.

## Improvements for the future

* Walls generated need to be filtered out to ensure that small regions are removed and small holes are covered. This can be done by performing a DFS in each region to count the number of walls/holes in each region and then remove them if needed.

### Credits

The credits for the base maze game code go to [PhillipeMorere](https://github.com/PhilippeMorere).
