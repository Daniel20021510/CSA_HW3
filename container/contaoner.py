from objects.plant_classes import Plant


class Container:
    def __init__(self):
        self.container = list()

    def out(self, output_file):
        with open(output_file, 'a') as f:
            f.write("Number of plants: " + str(len(self.container)) + '\n\n')
            for i in range(len(self.container)):
                f.write(f"{i}: " + str(self.container[i]) + '\n')

    def add(self, item):
        if len(self.container) < 10000:
            self.container.append(item)
            return True
        else:
            return False

    @staticmethod
    def read_input(input_file) -> 'Container':
        container = Container()
        with open(input_file, 'r') as input_file:
            plants_number = input_file.readline()
            if not plants_number:
                return container
            plants_number = int(plants_number)
            for i in range(plants_number):
                container.add(Plant.read_input(input_file))
        return container

    def straight_insertion(self):
        for i in range(len(self.container)):
            plant = self.container[i]
            j = i
            while(j > 0 and self.container[j-1].vowels_per_size() > plant.vowels_per_size()):
                self.container[j] = self.container[j-1]
                j -= 1
            self.container[j] = plant

    @staticmethod
    def random(size):
        container = Container()
        print(size)
        if size > 10000:
            print("Error: Size more then 10000")
            exit(0)
        if size < 1:
            print("Error: Size less then 1")
            exit(0)
        for i in range(size):
            container.add(Plant.random_plant())
        return container