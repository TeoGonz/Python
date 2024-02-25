class GetAverage:
    def __init__(self):
        self.__list = []
        self.__len = 0    
        self.__average = 0

    #   Función para tetornar el promedio
    def return_average(self, array):
        self.list = array
        current = self.list
        sum = 0
        for index, value in enumerate(current):
            sum = sum + value
            self.__len += 1
        self.__average = sum / self.__len
        return self.__average