cache = {}

def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # add every item in weights to the cache with its index as a value
    for i in range(len(weights)):
        cache[weights[i]] = i
    # then, get the other weight we'd be looking for
    for j in range(len(weights)):
        a = limit - weights[j]
        # and check if it's a key in the cache
        if a in cache:
            # if it is, return the value (aka the index)
            return (max(j, cache[a]), min(j, cache[a]))

    return None
