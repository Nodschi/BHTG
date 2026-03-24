import config as con

def clamp_position(x, y):
    x = max(con.PLAYER_SIZE, min(x, con.WINDOW_SIZE_X - con.PLAYER_SIZE))
    y = max(con.PLAYER_SIZE, min(y, con.WINDOW_SIZE_Y - con.PLAYER_SIZE))

    return x, y