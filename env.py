from excel_to_map import *
import pygame          # 导入模块
from pygame.locals import *    # 导入pygame一些常用的函数和常量
import sys
from agents import agent
import numpy as np
from map_to_graph import *


class Env_Make:
    def __init__(self, width, height, bg_name):
        # initial the screen & background image
        self.screen = pygame.display.set_mode((width, height))
        self.bg = pygame.image.load(bg_name)
        # put bg on the assigned point in the memory,the bg is not showed in this step
        self.screen.blit(self.bg, (0, 0))# (x, y) is the left up location
        pygame.init()

    # do things about displaying in this function

    def set_landmark(self, mark_group):
        for mark in mark_group.sprites():
            self.screen.blit(mark.image, mark.rect)

    def env_render(self, agent_group, mark_group: pygame.sprite.Group):
        self.screen.blit(self.bg, (0, 0))  # update the background image
        self.set_landmark(mark_group)  # update the display of logos

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("end simulation...")
                pygame.quit()
                exit(0)
        # update the display of cars
        for CarAgent in agent_group:
            CarAgent.update_p()
            self.screen.blit(CarAgent.image, CarAgent.rect)
        # update the screen
        pygame.display.update()
        # pygame.time.delay(100)

    # get all the and sort of the agents
    def get_all_state_sort(self, agent_group):
        state_sort_list = []
        for CarAgent in agent_group.sprites():
            state_sort_list.append([CarAgent.state, CarAgent.sort])

        return state_sort_list



