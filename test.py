from initial import *
import random
from tasks import task
import numpy as np
from numpy import random as nr
from get_task_car import *

if __name__ == '__main__':
    j = 0
    while j < 1000:
        seed = random.random()
        if seed < 0.01:
            ran_n = 1
        else:
            ran_n = 0
        # random create task
        # while True:
        #     ran_n = int(nr.poisson(1, 1))
        #     if ran_n < 2:
        #         break
        if ran_n > 0:
            for item in range(j, j+1):
                # create one task
                globals()['task'+str(item)] = task.ran_create_task(list_path, list_path)
                task_group.append(globals()['task'+str(item)])
                # choose a car for the task
                decide_car(car_group, globals()['task'+str(item)])
                ###############################################
                globals()['task'+str(item)].car.state = 1

                # make the car's point as the task's start point
                globals()['task'+str(item)].get_start_point(globals()['task'+str(item)].car.get_place())

                # the logo is dynamic,coming up with one task
                mark_group.add(globals()['task'+str(item)].mark_pass, globals()['task'+str(item)].mark_end)

                path1, dist1 = cal.calculation_3point(str(globals()['task'+str(item)].p_start), str(globals()['task'+str
                (item)].p_pass),str(globals()['task'+str(item)].p_end), map_name)

                globals()['task'+str(item)].car.get_schedule(path1)
                for element in task_group:
                    if element.state == 0:
                        # for every task it is needed to check complete or not
                        element.check_state(element.car.get_place())
                    else:
                        task_group.remove(element)

                my_env.env_render(car_group, mark_group)

        j += 1
        # print(len(task_group))





