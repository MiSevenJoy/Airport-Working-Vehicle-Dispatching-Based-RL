import pygame
import random
from tasks import task


def decide_car(agent_group, my_task: task.Task):
    free_agent_list = []
    for element in agent_group:
        if element.state == 0:
            free_agent_list.append(agent_group.index(element))
    n = random.randint(0, len(free_agent_list)-1)
    my_task.car = agent_group[free_agent_list[n]]
    return free_agent_list[n]
