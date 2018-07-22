import random


class TerrainGenerator:
    def __init__(self, dimensions, values):
        # Split up dimensions
        self.width, self.height = dimensions

        # Create dictionary of values with respective probabilities to choose from
        self.values = values

    def generate(self, smoothness):
        """
        Generates and returns a list filled with the values in a terrain-like distribution
        :param smoothness: how many times to run the smoothing process
        :return: a procedurally-generated list with the values in a terrain-like distribution
        """
        # Create a blank slate to fill with terrain values
        empty_terrain = self.create_blank()

        # Fill the terrain with noise
        terrain = self.create_noise(empty_terrain)

        # Iterate over the noise
        for i in range(smoothness):
            terrain = self.smooth_random(terrain)

        # Return the terrain
        return terrain

    def create_blank(self):
        """
        Creates and returns a empty (None-filled) list with the requested dimensions
        :return: a None-filled list of lists with the requested dimensions
        """
        # Multiply that row to create a two-dimensional list
        empty_terrain = [[None for i in range(self.width)] for j in range(self.height)]

        # Return the list
        return empty_terrain

    def create_noise(self, terrain):
        """
        Fills a passed-in list with (weighted, but) randomly chosen values
        :param terrain: the list to fill with value noise
        :return: the terrain filled with value noise
        """
        # For every row...
        for i in range(len(terrain)):
            # For every column...
            for j in range(len(terrain[i])):
                # Fill this tile with a chosen value
                terrain[i][j] = self.choose_value()

        # Return the filled-in terrain
        return terrain

    def choose_value(self):
        """
        Chooses a value from the dictionary of values, given their respective probabilities
        :return: a (weightedly) random value from the values dictionary
        """
        # Find out maximum threshold (sum of all value probabilities)
        maximum = 0
        for value in self.values:
            maximum += self.values[value]

        # Create a random number
        choice = random.random() * maximum

        # Declare threshold -- the value that will grow until the random number is less than it
        threshold = 0

        # For every value...
        for value in self.values:
            # Increase the threshold by the value's probability
            threshold += self.values[value]

            # If the random number is less than the threshold...
            if choice < threshold:
                return value

    def smooth_index(self, terrain):
        """
        Iterates over the terrain row by row, column by column to smooth borders between value-groups
        :param terrain: the terrain to smooth
        :return: a more smoothly-bordered terrain
        """
        # For every row...
        for i in range(len(terrain)):
            # For every column:
            for j in range(len(terrain[i])):
                # Collect neighbor values
                neighbors = self.get_neighbors(terrain, (i, j))

                # Set this terrain value based on the neighbors
                terrain[i][j] = self.determine_value(neighbors)

        # Return the smoothed terrain
        return terrain

    def smooth_random(self, terrain):
        """
        Iterates over the terrain randomly to smooth borders between value-groups
        :param terrain: the terrain to smooth
        :return: a more smoothly-bordered terrain
        """
        # Create list of unchecked indices
        indices = self.generate_indices_list()

        # For every index in the list...
        for i in indices:
            # Set row and column values
            row, column = i

            # Collect neighbor values
            neighbors = self.get_neighbors(terrain, i)

            # Set this terrain value based on the neighbors
            terrain[row][column] = self.determine_value(neighbors)

        # Return the smoothed terrain
        return terrain

    def generate_indices_list(self):
        """
        Returns a list of tuples in a random order such that every element is a valid coordinate
        :return: a list of tuples in a random order
        """
        # Create list of ordered indices
        indices = []

        # For each row...
        for i in range(self.height):
            # For each column...
            for j in range(self.width):
                indices.append((i, j))

        # Scramble indices
        random.shuffle(indices)

        # Return scrambled list of indices
        return indices

    def get_neighbors(self, terrain, pos):
        """
        Returns a list of an element's neighbors
        :param terrain: the terrain to examine
        :param pos: the position of the element on the terrain
        :return: a list of an element's neighbors
        """
        # Split coordinates
        i, j = pos

        # If the element is in the first row...
        if i == 0:
            # If it's in the top-left corner...
            if j == 0:
                neighbors = [terrain[i][j + 1],         # Right
                             terrain[i + 1][j + 1],     # Bottom-right
                             terrain[i + 1][j]]         # Bottom

            # If it's in the top-right corner...
            elif j == len(terrain[i]) - 1:
                neighbors = [terrain[i][j - 1],         # Left
                             terrain[i + 1][j - 1],     # Bottom-left
                             terrain[i + 1][j]]         # Bottom

            # Otherwise...
            else:
                neighbors = [terrain[i][j - 1],         # Left
                             terrain[i + 1][j - 1],     # Bottom-left
                             terrain[i + 1][j],         # Bottom
                             terrain[i + 1][j + 1],     # Bottom-right
                             terrain[i][j + 1]]         # Right

        # If it's in the last row...
        elif i == len(terrain) - 1:
            # If it's in the bottom-left corner...
            if j == 0:
                neighbors = [terrain[i][j + 1],         # Right
                             terrain[i - 1][j + 1],     # Top-right
                             terrain[i - 1][j]]         # Top

            # If it's in the bottom-right corner...
            elif j == len(terrain[i]) - 1:
                neighbors = [terrain[i][j - 1],         # Left
                             terrain[i - 1][j - 1],     # Top-left
                             terrain[i - 1][j]]         # Top

            # Otherwise...
            else:
                neighbors = [terrain[i][j - 1],         # Left
                             terrain[i - 1][j - 1],     # Top-left
                             terrain[i - 1][j],         # Top
                             terrain[i - 1][j + 1],     # Top-right
                             terrain[i][j + 1]]         # Right

        # If it's in the first column, but not the first or last row...
        elif j == 0:
            neighbors = [terrain[i - 1][j],             # Top
                         terrain[i - 1][j + 1],         # Top-right
                         terrain[i][j + 1],             # Right
                         terrain[i + 1][j + 1],         # Bottom-right
                         terrain[i + 1][j]]             # Bottom

        # If it's in the last column, but not the first or last row...
        elif j == len(terrain[i]) - 1:
            neighbors = [terrain[i - 1][j],             # Top
                         terrain[i - 1][j - 1],         # Top-left
                         terrain[i][j - 1],             # Left
                         terrain[i + 1][j - 1],         # Bottom-Left
                         terrain[i + 1][j]]             # Bottom

        # Otherwise...
        else:
            neighbors = [terrain[i][j - 1],             # Left
                         terrain[i + 1][j - 1],         # Bottom-left
                         terrain[i + 1][j],             # Bottom
                         terrain[i + 1][j + 1],         # Bottom-right
                         terrain[i][j + 1],             # Right
                         terrain[i - 1][j + 1],         # Top-right
                         terrain[i - 1][j],             # Top
                         terrain[i - 1][j - 1]]         # Top-left

        # Return the neighbors
        return neighbors

    def determine_value(self, neighbors):
        """
        Returns the new value to set an element to based on its neighbors
        :param neighbors: the nearby values to use to determine an element's value
        :return: the element's new value
        """
        # Create a dictionary to keep track of the amounts of each value
        counts = {value: 0 for value in self.values}

        # For each neighbor...
        for neighbor in neighbors:
            # Count it
            counts[neighbor] += 1

        # Create majority value (by default the first value type in counts)
        majority = list(counts.keys())[0]

        # Find the biggest value...
        for value in counts:
            # If this value's count is bigger...
            if counts[value] > counts[majority]:
                # Set majority to it
                majority = value
            # If it ties with the current majority...
            elif counts[value] == counts[majority]:
                # Randomly choose the majority between them
                majority = value if random.random() > 0.5 else majority

        # Return the majority value
        return majority


def main():
    t = TerrainGenerator((80, 80), {"X": 2.1,
                                    "#": 2.2,
                                    ".": 2.1,
                                    " ": 2.2})

    terrain = t.generate(100)

    for i in terrain:
        for j in i:
            print(j, end="  ")
        print()


main()
