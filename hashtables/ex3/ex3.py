def intersection(arrays):
    """
    YOUR CODE HERE
    """
    intersected = {}
    # loop through the list of arrays
    for array in arrays:
        # loop through each individual array
        for number in array:
            # if that number is already in intersected, add one
            if number in intersected:
                intersected[number] += 1
            # if it's the first time we've seen it, it starts at 1
            else:
                intersected[number] = 1
    
    # only return the ones that were in every array, or the length of "arrays"
    return [key for key, value in intersected.items() if value == len(arrays)]


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
