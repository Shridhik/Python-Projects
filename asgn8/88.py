import random


def day0mat(pop_density, disease_chance, grid_size):    # For day 0 of disease, we will need the population density, and the chances of getting a disease
    """
    Generates a matrix of grid_size x grid_size and each cell is populated based on pop_density propabilty check
    and is either healthy(0) or diseased based on disease_chance propability. This is day0 (initial grid)
    Args:
        pop_density (): propability of the cell in the matrix of grid_size x grid_size is populated
        disease_chance (): propability of the cell that is populated is healthy or diseased
        grid_size (): dimension or size of matrix or grid.

    Returns:
        matrix - returns a dictionary matrix with key(x,y) and
                 value '.' means empty(not populated)
                        0  means healthy(populated)
                        1  means diseased(populated)
    """

    emptyordead = 0         # initializing the count of population
    healthy = 0
    diseased = 0
    total = 0
    print("Initial Day0 Grid with cells empty - '.' or healthy - '0' or diseased - '1'")
    print("___________________________________________________________________________")
    matrix = {}                     # created a new dictionary for each coordinate pair and value
    for x in range(grid_size):      # goes through every x coordinate up to the input dimension of grid
        for y in range(grid_size):  # goes through every y coordinate paird for every x coordinate to create a square grid
            rand_healthy = random.random()      # the chance of a cell being occupied by a person is randomly chosen
            rand_diseased = random.random()     # the change of a cell being diseased by a person is randomly generated
            if rand_healthy < pop_density:      # if the probability of an occupied cell is less than the given density
                matrix[(x, y)] = 0              # then the cell will be a healthy person
                if rand_diseased < disease_chance:      # if the probability of being diseased is less than the chance of getting the disease
                    matrix[(x, y)] = 1          # then the cell will be an unhealthy person
            else:
                matrix[(x, y)] = '.'            # else the cell will be a "."
            print(matrix[(x, y)], ' ', end="")  # print statement that avoids returning line after every print statement, found this soution on https://docs.python.org/3/whatsnew/3.0.html
        print("")

    for cell in matrix:                         # for every cell in the grid
        total += 1                              # will count the total cells in the grid cumulatively
        if matrix[cell] is '.':                 # if the x,y pair is a "."
            emptyordead += 1                    # the empty or dead cell count will go up 1
        elif matrix[cell] is 0:                 # if the x,y pair is a 0
            healthy += 1                        # the amount of healthy cell count will go up 1
        elif matrix[cell] is 1:                 # if the x,y pair is a 1
            diseased += 1
    print("")                                   # neat print statements
    print("TotalCell: ", total,      "Healthy: ", healthy, "    Diseased: ", diseased, "      empty: ", emptyordead)
    print("")
    return matrix


def x3matrix(target, birth_chance, spread_chance, disease_duration, mortality_rate, grid_size, matrix, new_matrix):
    """
    x3matrix function will determine how the target cell in the matrix 3x3 grid (Cell in the middle surrounded by 8 cells on all sides) affects
    surrounding cell or how surrounding 8 cells affects the target cell and update it into new_matrix 3x3 grid.
    Args:
        target (): center cell that affects or affected by surrounding cells passed from the zombie sim(moves through every cell in matrix)
        birth_chance (): The chance of an empty cell becoming an healthy cell (Number between 0 and 1)
        spread_chance (): The likelihhod that the disease will spread from one diseased square to its neighbours.
        disease_duration (): Nummber of days that a cell remains diseased. End of the duration the cell either dies or becomes healthy
        mortality_rate (): The chance that a diseased cell will die at the end of the disease duration.
        grid_size (): dimension or size of matrix or grid.
        matrix (): This is the input to this function matrix (dictionary) with key(x,y) and value(state of cell-0,1,'.').
        new_matrix(): Also an input that is the updated version of the matrix and transfered back to matrix at the end of each day

    Returns:
        new_matrix - returns an updated dictionary new_matrix with key(x,y) and
                 value '.' means empty(not populated)
                        0  means healthy(populated)
                        1  means diseased for 1 day(populated)
                        2-9 means diseased for 2-9 days
    """

    deadoralive = random.random()
    newlife = random.random()
    infect = random.random()

    if matrix[target] != '.':                                   # if the target cell in the grid is not an empty cell
        if matrix[target] in range(1, disease_duration + 1):    # if the target cell is in range of disease duration days
            new_matrix[target] = matrix[target] + 1             # increment that by 1 and put it back in new_matrix target location

            if matrix[target] == disease_duration + 1:          # if target cell at this point has already reached maximum disease duration
                if deadoralive < mortality_rate:                # we check the deadoralive(random number between 0 and 1) is less than moratility chance
                    new_matrix[target] = '.'                    # then we consider that cell occupant as dead , so it is a '.'
                    return new_matrix[target]
                else:
                    new_matrix[target] = 0                      # else it is a healthy cell (0)
                    return new_matrix[target]

    for x in range(target[0] - 1, target[0] + 2):               # this is to go to the left and the right of the target cell on the x axis by 1 cell
        for y in range(target[1] - 1, target[1] + 2):           # this is to go to the left and the right of the target cell on the y axis by 1 cell
            if (x, y) != target:                                # if the pair is not equal to the target cell
                if x < 0 or y < 0 or x >= grid_size or y >= grid_size:      # if the pair (x,y) comes outside the grid, skip this
                    pass
                else:
                    if matrix[(x, y)] != '.':                   # if any of the surrounding cells are not a .
                        if matrix[target] == 0 and 0 < matrix[(x, y)] <= disease_duration:  # and if the target cell is equal to 0 (healthy) and the surrounding cells is between 0 and disease duration
                            if infect < spread_chance:                                          # depending on the spread chance, the target cell may become diseased
                                new_matrix[target] = 1
                                # return new_matrix[target]

                    if matrix[target] == '.' and matrix[(x, y)] == 0:   # if the center cell is an empty cell, and the surrounding cells are healthy
                        if newlife < birth_chance:                      # depending on the birth chance, an new cell may be made healthy (newborn)
                            new_matrix[target] = 0
                            # return new_matrix[target]
    return new_matrix[target]


def zombie_sim(grid_size, pop_density, disease_chance, birth_chance, spread_chance, disease_duration, mortality_rate, noofdays):
    """
    zombie_sim function runs through the no of days that we want to run the simulation to show how the parameters affect
    the spread of the disease.
    Args:
        grid_size (): dimension or size of matrix or grid.
        pop_density (): input for day0 grid generation - propability of the cell in the matrix of grid_size x grid_size is populated
        disease_chance (): input for day0 grid generation - propability of the cell that is populated is healthy or diseased
        birth_chance (): The chance of an empty cell becoming an healthy cell (Number between 0 and 1)
        spread_chance (): The likelihhod that the disease will spread from one diseased square to its neighbours.
        disease_duration (): Number of days that a cell remains diseased. End of the duration the cell either dies or becomes healthy
        mortality_rate (): The chance that a diseased cell will die at the end of the disease duration.
        noofdays(): No of days we run the simulation

    Returns:
        None
    """

    if disease_duration > 9:                                                # ensures a parameter of making sure the disease duration is between 1 - 10
        print(" Disease duration parameter needs to be between 1-10")
        return
    print("")

    matrix = day0mat(pop_density, disease_chance, grid_size)        # store the grid for  day0, the original output, into "matrix"

    for days in range(0, noofdays):                                 # a for loop that runs for every day we inpput
        print("Day " + str(days + 1) + " Grid with cells empty - '.' or healthy - '0' or diseased - '1'")           # print statement
        print("___________________________________________________________________________________________")
        new_matrix = matrix
        for x in range(0, grid_size):                               # we repeat the process of looking to each x,y pair (cell)
            for y in range(0, grid_size):
                target = (x, y)                                     # main cell we are looking at
                new_matrix[target] = x3matrix(target, birth_chance, spread_chance, disease_duration, mortality_rate, grid_size, matrix,
                                              new_matrix)           # runs the x3matric function and returns the state of all surrounding cells including the target cell, for the new grid
        matrix = new_matrix                                         # swaps the new matrix with the matrix for the next day

        for x in range(0, grid_size):                               # prints the grid
            for y in range(0, grid_size):
                print(matrix.get((x, y)), ' ', end="")
            print("")

        cnt = count(matrix, disease_duration)                       # runs the count function and stores the result (cumulative count) in "cnt"
        # print(cnt[0], cnt[1], cnt[2], cnt[3])
        if cnt[1] > 0 and cnt[2] == 0:                              # if the count of healthy people is greater than 0 and the count of diseased is equal to 0
            print(" After " + str(days+1) + " days , seems like your neighbourhood is not contaminated. All is well ")
            break
        print("")

        if cnt[0] == cnt[3]:                                        # if the count of total people is equal to the count of empty or dead cells
            print(" After " + str(days+1) + " days,  everyone is dead")
            break

        elif days+1 == noofdays:                                    # if you have reached the maximum number of days,
            print(" At the end of " + str(days+1) + " still some survivors or diseased people still alive")
    return


def count(matrix, disease_duration):
    """
    count function to count the number of healthy,diseased and empty or dead cells that is used to decide whether to terminate or not.
    Args:
        matrix (): grid output at end of each day to count the state of each cell.
        disease_duration (): Number of days that a cell remains diseased. End of the duration the cell either dies or becomes healthy

    Returns:
        total : Total cell count in the grid/matrix
        healthy : Total count of healthy cells in the matrix
        diseased : Total count of diseased cells (1-10) in the matrix
        emptyordead : Total count of empty cell or dead cell in the matrix
    """

    emptyordead = 0      # initialization
    healthy = 0
    diseased = 0
    total = 0
    for cell in matrix:     # count of population as seen before
        total += 1
        if matrix[cell] is '.':
            emptyordead += 1
        elif matrix[cell] is 0:
            healthy += 1
        elif matrix[cell] in range(1, disease_duration + 1):
            diseased += 1
    print("TotalCell: ", total,      "Healthy: ", healthy, "    Diseased: ", diseased, "      EmptyorDead: ", emptyordead)
    print("")
    return total, healthy, diseased, emptyordead


def main():
    """
    Main function
    """
    # zombie_sim(grid_size, pop_density, disease_chance, birth_chance, spread_chance, disease_duration, mortality_rate, noofdays)

    zombie_sim(20, 0.15, 0.1, 0.1, 0.1, 3, 0.5, 500)            # requested simulation


if __name__ == '__main__':
    main()
