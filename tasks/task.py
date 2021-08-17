import operator
import random

d_distance = 100
# define the distance(m) of one grid
d_time = 10
# define the time(s) of one grid
# the landmark uesd to display should be created when the task is given so we can write a function here to achieve it
from agents import agent

passenger_img = '/home/joy/PycharmProjects/simulation/logo/passenger.png'
plane_point_img = '/home/joy/PycharmProjects/simulation/logo/plane_point.png'


class Task:
    def __init__(self, p_pass, p_end):
        self.p_pass = p_pass
        self.p_end = p_end
        self.state = 0
        # state=0 ==>not complete
        # state =1 ==>complete
        self.p_start = None
        self.t = None
        self.s = None
        self.car = None
        self.mark_pass = agent.Agent(passenger_img, self.p_pass, 2, '0')
        self.mark_end = agent.Agent(plane_point_img, self.p_end, 2, '0')

    # (x,y) "agent" ==>"task"
    def get_start_point(self, p_start):
        self.p_start = p_start

    def kill_mark(self):
        self.mark_pass.kill()
        self.mark_end.kill()

    # when the car assigned to th task arrived the end, the task is completed state ==> 1
    def check_state(self, p_agent):
        if operator.eq(p_agent, self.p_end):
            self.state = 1
            self.kill_mark()
            self.car.state = 0
            self.car.order = 0
            print(self.car.state)

    def get_reward(self, n):
        # total distance and time
        self.t = n*d_time
        self.s = n*d_distance
        return self.t, self.s


def ran_create_task(list_pass, list_end):
    p_pass_index = random.randint(0, len(list_pass)-1)
    while True:
        p_end_index = random.randint(0, len(list_end)-1)
        if p_end_index != p_pass_index:
            break
    new_task = Task(list_pass[p_pass_index], list_end[p_end_index])
    return new_task