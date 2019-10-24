class Player:

    def __init__(self, x, y, matrix = None):
        self.x = x
        self.y = y
        self.matrix = matrix

    def move(self, map_matrix, action):
        x, y = self.x, self.y
        if action == 0:
            x += 1
        elif action == 2:
            x -= 1
        elif action ==1:
            y += 1
        elif action == 3:
            y -= 1
        if x < 0 or y < 0 or x >= map_matrix.shape[0] or y >= map_matrix.shape[1] or map_matrix[x, y] == -1:
            return False
        elif map_matrix[x, y] == 1:
            self.x = x
            self.y = y
            return True
        else:
            self.x = x
            self.y = y
            return self

    def log(self):
        print("X:")
        print(self.x)
        print("Y:")
        print(self.y)
        print("="*20)