import random


def generate(width, height, smoothness, values):
    """Generates and returns a new procedurally-generated terrain

    Generates and returns a two-dimensional list with the
    passed values spread throughout in a terrain-like fashion.

    Args:
        width: The width of the terrain to generate.
        height: The height of the terrain to generate.
        smoothness: The number of times to run the smoothing
            algorithm on the terrain.
        values: A dictionary containing the values to spread
            throughout the terrain paired to their relative
            probabilities of appearing. For example:
            {"X": 0.2442, "#": 0.2558, ".": 0.2442, " ": 0.2558}

            In this example, "X" and "." are slightly less likely
            to appear than "#" and " ".

    Returns:
        A two-dimensional list with the values spread in a
        terrain-like fashion. For example, running this code:

        > terrain = platypus.generate(10, 10, 1, {"X": 0.2442,
        >                                         "#": 0.2558,
        >                                         ".": 0.2442,
        >                                         " ": 0.2558})

        ...can create a terrain that, when displayed, looks like:

        .  .  .  .  .  .  .  .  X  X
        #  .  .  .  .  .  .  .  X  X
        #  .  .  .  .  .  .  .  X  X
        #  #  #  #  #  .           X
        #  #  #
        #  #
        #              X  X  X  X  X
                    X  X  X  X  X  X
                    X  X  X  X
                    X  X  X

    Raises:
        ValueError: Platypus terrains must be at least 3x3
            (Attempted: (dimensions attempted)).
    """
    # Check to see that the width and height are each at least three
    # If the width or height is less than three...
    if width < 3 or height < 3:
        # Raise a ValueError
        raise ValueError("Platypus terrains must be at least 3x3 (Attempted: " + str(width) + "x" + str(height) + ").")

    # Create a blank slate to fill with terrain values
    terrain = _create_blank(width, height)

    # Fill the terrain with noise
    _create_noise(terrain, values)

    # Iterate over the noise repeatedly to smooth it ('smoothness' times)
    for i in range(smoothness):
        _smooth(terrain, values)

    # Return the terrain
    return terrain


def _create_blank(width, height):
    """Returns a 2D list filled with None elements.

    Creates and returns a list of lists of the given dimensions
    filled with None elements.

    Args:
        width: The width of the blank terrain to generate.
        height: The height of the blank terrain to generate.
    """
    # Use a list comprehension to generate a blank of the given dimensions
    empty_terrain = [[None for i in range(width)] for j in range(height)]

    # Return the list
    return empty_terrain


def _create_noise(terrain, values):
    """Fills the given terrain with noise made with the given values.

    Args:
        terrain: The terrain to fill with noise.
        values: The values to create noise with.
    """
    # For every row...
    for i in range(len(terrain)):
        # For every column...
        for j in range(len(terrain[i])):
            # Fill this tile with a chosen value
            terrain[i][j] = _choose_value(values)


def _choose_value(values):
    """Chooses a value from the given values.

    This takes into account the respective probabilities
    of each value.

    Args:
        values: The dictionary from which to choose a value.
            For example: {"X": 1, "#": 2}

    Returns:
        A weighted, but randomly chosen value from the given
        dictionary.
    """
    # Find out maximum threshold (sum of all value probabilities)
    maximum = 0
    for value in values:
        maximum += values[value]

    # Create a random number
    choice = random.random() * maximum

    # Declare threshold -- the value that will grow until the random number is less than it
    threshold = 0

    # For every value...
    for value in values:
        # Increase the threshold by the value's probability
        threshold += values[value]

        # If the random number is less than the threshold...
        if choice < threshold:
            return value


def _smooth(terrain, values):
    """Smooths the terrain.

    Iterates over the terrain by choosing random indices
    and setting said indices to the majority neighbor value.

    Args:
        terrain: The terrain to smooth.
        values: The values of the terrain. These are used to
            simplify computation in determine_value.

    Returns:
        A more smoothly-bordered terrain (less noisy).
    """
    # Create list of unchecked indices
    indices = _generate_indices_list(terrain)

    # For every index in the list...
    for i in indices:
        # Set row and column values
        row, column = i

        # Collect neighbor values
        neighbors = _get_neighbors(terrain, i)

        # Set this terrain value based on the neighbors
        terrain[row][column] = _determine_value(neighbors, values)

    # Return the smoothed terrain
    return terrain


def _generate_indices_list(terrain):
    """Returns a unordered list of valid coordinates for given terrain.

    Args:
        terrain: The terrain to find coordinates for.
    """
    # Create list of ordered indices
    indices = []

    # For each row...
    for i in range(len(terrain)):
        # For each column...
        for j in range(len(terrain[i])):
            indices.append((i, j))

    # Scramble indices
    random.shuffle(indices)

    # Return scrambled list of indices
    return indices


def _get_neighbors(terrain, pos):
    """Returns a list of a given element's neighbor values.

    Args:
        terrain: The terrain to look for neighbors in.
        pos: The position of the element to find neighbors for.
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


def _determine_value(neighbors, values):
    """Returns the value to set an element to based on its neighbors.

    Args:
        neighbors: The neighbors of the element in question.
        values: The values of the terrain. This is passed in so that
            a new dictionary doesn't have to be created and added to.
    """
    # Create a dictionary to keep track of the amounts of each value
    counts = {value: 0 for value in values}

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


def display_terrain(terrain):
    """Prints an ASCII representation of a given terrain to the console.

    Args:
        terrain: The terrain to display to the console.
    """
    # Iterate through every element in the terrain...
    for i in terrain:
        for j in i:
            # Print each element with some space afterwards
            print(j, end="  ")
        # After each row is done printing, separate with a newline
        print()
