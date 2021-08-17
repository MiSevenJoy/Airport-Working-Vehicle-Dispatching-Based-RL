import pygame
import numpy as np

pixel_x = 31
pixel_y = 31

class Agent(pygame.sprite.Sprite):
    def __init__(self, image_name, p_list, sort, name):
        super().__init__()

        # 加载图像

        self.image = pygame.image.load(image_name)

        # 设置尺寸

        self.rect = self.image.get_rect()
        self.place = p_list

        # the way of display :topleft
        # also the initial position
        self.rect.topleft = [p_list[1]*pixel_y, p_list[0]*pixel_x]

        # # the place of agent
        # self.place = place
        # state = 0 ==> free
        # state =1 ==> busy
        self.state = 0

        # sort = 0 ==> Shuttle car
        # sort = 1 ==> Package car
        # sort = 2 ==> landmark
        self.sort = sort

        self.schedule = None
        self.schedule_length = None
        # the point in the schedule that agent in
        self.order = 0
        # the pixel of each grid
        self.Name = name

    # get the position of agent
    def get_place(self):
        return self.place

    def get_schedule(self, list_schedule):
        self.schedule = np.array(list_schedule)
        #print(self.schedule)
        self.schedule_length = len(list_schedule)
        #print(self.schedule_length)

    def change_rect(self, p_new):
        # self.place = p_new
        # in pygame the axis is the transposition of the axis of cols & rows
        self.rect.x = p_new[1] * pixel_y
        self.rect.y = p_new[0] * pixel_x

    # only when the agent is busy,it moves,when it finished one task, the state will be changed back to 0
    # when the car is free ,it has no schedule path
    def update_p(self):
        if self.state == 1:
            d_move = self.schedule[self.order+1] - self.schedule[self.order]
            self.place = self.schedule[self.order+1].tolist()
            self.rect.x += d_move[1]*pixel_y
            self.rect.y += d_move[0]*pixel_x
            self.order += 1







