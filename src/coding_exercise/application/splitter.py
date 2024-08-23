import numpy as np

from src.coding_exercise.domain.model.cable import Cable

class Splitter:

    def __validate(self):
        valid = True
        if not valid:
            raise ValueError

    # Split method implementation which takes two arguments and generate the results accordingly.
    # If the arguments are out of range it raises ValueError

    def split(self, cable: Cable, times: int) -> list[Cable]:
        self.__validate()

        if (1 > times) or (times >= 64):
            raise ValueError

        if (2 > cable.length) or (cable.length >= 1024):
            raise ValueError

        calculated_length = cable.length
        array_of_cables = []

        print("Initial cable length: ", cable.length, "No of iterations: ", times)

        # Start the splitting operation
        if cable.length % 2 == 0:
            for i in range(times):
                if calculated_length > 1:
                    calculated_length = int(np.floor(calculated_length / 2))

                array_of_cables.append(calculated_length)
                array_of_cables.append(calculated_length)
                print("Iteration: ", i, "Calculated: ", calculated_length)
        else:
            for i in range(cable.length):
                array_of_cables.append(1)

        np.sort(array_of_cables)

        no_iterations = int(cable.length / array_of_cables[len(array_of_cables) - 1])

        # Calculate the final array with the exact lengths
        final_array_of_cables = []
        for i in range(no_iterations):
            cable_length = int(cable.length / no_iterations)
            cable_name = cable.name + "-" + str(i).zfill(cable_length)
            final_array_of_cables.append(Cable(cable_length, cable_name))
            print("Element:", final_array_of_cables[i].name, "Length:", final_array_of_cables[i].length)

        print("---------------------------------------------------\n")
        return final_array_of_cables

