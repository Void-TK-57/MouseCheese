
import numpy as np
import pandas as pd
import random

class Player:

    def __init__(self, x, y, Q = None, rewards = None):
        self.x = x
        self.y = y
        self.Q = Q
        self.rewards = rewards
        self.exploration_time = 20

    def move(self, map_matrix, action):
        x, y = self.x, self.y
        if action == "right":
            x += 1
        elif action == "left":
            x -= 1
        elif action =="up":
            y += 1
        elif action == "down":
            y -= 1
        if x < 0 or y < 0 or x >= map_matrix.shape[0] or y >= map_matrix.shape[1] or map_matrix[y, x] == -1:
            return False
        elif map_matrix[x, y] == 1:
            self.x = x
            self.y = y
            return True
        else:
            self.x = x
            self.y = y
            return None

    def get_reward(self):
        # get goal position
        distance = self.rewards[self.y, self.x]
        # reward function is proportional to the inverse of the reward
        return 300 - 10*distance

    def Q_learn(self, map_matrix, learning_rate = 0.7, gamma = 0.8):
        # get current state
        state = self.get_state()
        
        chance_of_exploration = 70
        if self.exploration_time > 0:
            self.exploration_time -= 1
            chance_of_exploration = 100
        # get action
        action = self.get_action(chance_of_exploration)
        # move the player
        move_valid = self.move(map_matrix, action)
        # get new state
        new_state = self.get_state()
        # get reward
        if move_valid == False:
            reward = -100
        else:
            reward = self.get_reward()

        # update function
        self.Q[action][state] = self.Q[action][state] + learning_rate * (reward + gamma * np.max(self.Q.loc[new_state]) - self.Q[action][state])
        
        return move_valid

    def init_Q(self, path=None, width = 0, height = 0):
        index = []
        columns = ["up", "right", "down", "left"]
        if path is not None:
            with open(path) as json_file:
                Q = np.array(json.load(json_file)["Q"])
        else:
            Q = np.zeros(width*height)
        # create matrix based on distance
        for i in range(Q.shape[0]):
            for j in range(Q.shape[1]):
                if path is None:
                    Q[i][j] = end[0]+end[1] - (i + j)
                index.append(str(i)+"-"+str(j))
        # set Q dataframe
        self.Q = pd.DataFrame(Q, index = index, columns = columns)
    


    def get_state(self, x = None, y = None):
        return str(self.x)+"-"+str(self.y)

    def get_action(self, chance = 70):
        random_number = random.randint(0, 100)
        if random_number < 70:
            # action based on q
            actions = self.Q.loc[self.get_state()]
            # return index of max value
            return actions.idxmax()
            
        else:
            actions_list = ["up", "right", "down", "left"]
            # action is random
            return actions_list[ random.randint(0, 3) ]
            

    def log(self):
        print("X:")
        print(self.x)
        print("Y:")
        print(self.y)
        print("Q:")
        print(self.Q.to_string())
        print("="*20)