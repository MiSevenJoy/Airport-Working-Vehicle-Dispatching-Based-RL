from agents import agent
import pygame
from env import *
from map_to_graph import *

bg_img = '/home/joy/PycharmProjects/simulation/map.png'
bus_img = '/home/joy/PycharmProjects/simulation/logo/bus.png'
package_car_img = '/home/joy/PycharmProjects/simulation/logo/package_car.png'
parking_point_img = '/home/joy/PycharmProjects/simulation/logo/parking_point.png'
map_name = '/home/joy/PycharmProjects/simulation/airport_map.xls'
# creating one environment
my_env = Env_Make(674, 983, bg_img)
# loading the xls file to get different kinds of grid_list
my_map = Read_Excel(map_name, 'map')
list_position = my_map.excel_map()
list_path = list_position[0]
list_near_p = list_position[1]
list_far_parking = list_position[2]
list_bus_parking = list_position[3]
cal = Calculation()
# #########################################
# change: random from the list above

for i in range(40):
    if i < 5:
        locals()['bus'+str(i)] = agent.Agent(bus_img, list_bus_parking[0], 0, 'bus'+str(i))
    elif i < 10:
        locals()['bus' + str(i)] = agent.Agent(bus_img, list_bus_parking[1], 0, 'bus'+str(i))
    elif i < 15:
        locals()['bus' + str(i)] = agent.Agent(bus_img, list_bus_parking[2], 0, 'bus'+str(i))
    else:
        locals()['bus' + str(i)] = agent.Agent(bus_img, list_bus_parking[3], 0, 'bus'+str(i))

car_group = []
for i in range(20):
    car_group.append(locals()['bus'+str(i)])
mark_group = pygame.sprite.Group()
task_group = []
