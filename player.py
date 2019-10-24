
import numpy as np
import random

class Player:

    def __init__(self, x, y, matrix = None):
        self.x = x
        self.y = y
        self.Q = Q

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

    def get_reward(self, map, end):
        pass

    def Q_learn(self, map_matrix, iterations, learning_rate = 0.5, gamma = 0.5, state = 0):
        state = self.move(map_matrix, self.get_action())
        
        # update function
        self.Q[state, action] = self.Q[state, action] + lr * (reward + gamma * np.max(self.Q[new_state, :]) - self.Q[state, action])

    def init_Q(self, path=None, end = None):
        if path is not None:
            with open(path) as json_file:
                self.Q = np.array(json.load(json_file)["Q"])
        else:
            # create matrix based on distance
            for i in range(self.Q.shape[0]):
                for j in range(self.Q.shape[1]):
                    self.Q[i][j] = end[0]+end[1] - (i + j)

    def get_state(self, x = None, y = None):
        if x is None:
            x = 
        return self.x + self.y*self.Q.shape[0]

    def get_action(self, chance = 70):
        i = random.randint(0, 100)
        if i < 70:
            # action based on q
            actions = sefl.Q[self.get_state()]
            print(actions)
            # get action
            action = np.where(actions == np.min(actions))[0][0]
            # return action
            return action
            
        else:
            # action is random
            return random.randint(0, 3)
            

    def log(self):
        print("X:")
        print(self.x)
        print("Y:")
        print(self.y)
        print("="*20)