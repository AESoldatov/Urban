class Figure:
    sides_count = 0
    def __init__(self):
        self.__sides = []
        self.__color = []
        #self.filled = True
    def get_color(self):
        pass
    def __is_valid_color(self, rgb):
        if  all(0 <= color <= 255 for color in rgb):
            return True
        else:
            return False


