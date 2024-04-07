import threading
import time
from scipy.optimize import minimize

class UserPosition:
    def __init__(self, beacons):
        self.beacons = beacons
        self.user_position = [0, 0]
        self.update_position()

    def distance(self, point1, point2):
        return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5

    def loss(self, user_position):
        return sum((self.distance(user_position, beacon['position']) - beacon['distance'])**2 for beacon in self.beacons)

    def calculate_position(self):
        initial_guess = [0, 0]
        result = minimize(self.loss, initial_guess, method='Nelder-Mead')
        return result.x

    def update_position(self):
        self.user_position = self.calculate_position()
        print(f"Позиция пользователя: {self.user_position}")

    def start(self):
        while True:
            self.update_position()
            time.sleep(1)

if __name__ == "__main__":
    beacons = [
        {'position': [0, 0], 'distance': 5},
        {'position': [10, 0], 'distance': 5},
        {'position': [0, 10], 'distance': 7.07}
    ]

    user_position_calculator = UserPosition(beacons)
    thread = threading.Thread(target=user_position_calculator.start)
    thread.start()
