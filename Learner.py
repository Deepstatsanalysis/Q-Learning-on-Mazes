__author__ = 'philippe'
import World
import threading
import time
import numpy as np

discount = 0.3
gamma = 0.8 # Initial probability
gamma_decay = 0.95 # Exploration/exploitation tradeoff
actions = World.actions
states = []
Q = {}
for i in range(World.x):
    for j in range(World.y):
        states.append((i, j))

for state in states:
    temp = {}
    for action in actions:
        temp[action] = 0.1
        World.set_cell_score(state, action, temp[action])
    Q[state] = temp

for (i, j, c, w) in World.specials:
    for action in actions:
        Q[(i, j)][action] = w
        World.set_cell_score((i, j), action, w)


def do_action(action):
    s = World.player
    r = -World.score
    if action == actions[0]:
        World.try_move(0, -1)
    elif action == actions[1]:
        World.try_move(0, 1)
    elif action == actions[2]:
        World.try_move(-1, 0)
    elif action == actions[3]:
        World.try_move(1, 0)
    else:
        return
    s2 = World.player
    r += World.score
    return s, action, r, s2


def max_Q(s):
    val = None
    act = None
    for a, q in Q[s].items():
        if val is None or (q > val):
            val = q
            act = a
    return act, val


def inc_Q(s, a, alpha, inc):
    Q[s][a] *= 1 - alpha
    Q[s][a] += alpha * inc
    World.set_cell_score(s, a, Q[s][a])


def run():
    global discount
    global gamma
    time.sleep(1)
    alpha = 1
    t = 1
    # If its taking too long, then restart and try again
    max_run_iter = 5000
    cur_iter = 0
    while True:
        cur_iter += 1
        if cur_iter > max_run_iter:
            cur_iter = 0
            World.restart_game()

        # Pick the right action
        s = World.player
        max_act, max_val = max_Q(s)

        # Exploration/Exploitation tradeoff
        if np.random.rand(1) <= gamma:
            max_act = np.random.choice(["up", "down", "left", "right"])
            # print max_act

        (s, a, r, s2) = do_action(max_act)

        # Update Q
        max_act, max_val = max_Q(s2)
        inc_Q(s, a, alpha, r + discount * max_val)

        # Check if the game has restarted
        t += 1.0
        if World.has_restarted():
            World.restart_game()
            gamma *= gamma_decay
            time.sleep(0.01)
            t = 1.0

        # Update the learning rate
        alpha = pow(t, -0.1)

        # Reduce sleep time to get results faster
        time.sleep(0.01)


t = threading.Thread(target=run)
t.daemon = True
t.start()
World.start_game()
