import xlrd
import numpy as np

class Read_Excel(object):
    def __init__(self, file, sheet):
        self.file = file
        self.sheet = sheet
        self.s = None

    #open the excel file
    def open_excel(self):
        try:
            book = xlrd.open_workbook(self.file)
        except Exception:
            print(u'useless file path')
        # 根据sheet值确定访问sheet方法
        if type(self.sheet) not in [int, str]:
            print(u'请输入<type int>or <type str>,not{0}'.format(type(self.sheet)))
        elif type(self.sheet) == int:
            self.s = book.sheet_by_index(self.sheet)
        else:
            self.s = book.sheet_by_name(self.sheet)

    # get the excel file data
    def excel_map(self):
        self.open_excel()
        rows = self.s.nrows  # 总行数
        cols = self.s.ncols  # total columns

        # Divide cells into two categories
        # path cell : value = 1
        # obstacle cell : value = 0
        # nearby apron : value = 2
        # far apron: value =3
        list_path = []
        list_near_p =[]
        list_far_p =[]
        list_bus_p =[]
        for i in range(0, rows):
            for j in range(0, cols):
                if self.s.cell_value(i, j) > 0:
                    list_path.append([i, j])
                    if self.s.cell_value(i, j) == 2:
                        list_near_p.append([i, j])
                    elif self.s.cell_value(i, j) == 3:
                        list_far_p.append([i, j])
                    elif self.s.cell_value(i, j) == 4:
                        list_bus_p.append([i, j])

        return list_path, list_near_p, list_far_p, list_bus_p

    def excel_array(self):
        self.open_excel()
        rows = self.s.nrows  # 总行数
        cols = self.s.ncols  # total columns
        array_map = np.empty((rows, cols))
        for i in range(0, rows):
            for j in range(0, cols):
                array_map[i][j] = self.s.cell_value(i, j)

        #print(array_map)
        return array_map


    def show_list(self):
        list_path, list_obstacle = self.excel_map()
        for point in list_path:
            print(point)
        print('-'*50)
        for point in list_obstacle:
            print(point)

