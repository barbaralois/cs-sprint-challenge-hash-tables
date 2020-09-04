#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

cache = {}

def reconstruct_trip(tickets, length):
    # for each ticket, add it to the cache with key as source, value as dest
    for ticket in tickets:
        cache[ticket.source] = ticket.destination
    # start at the ticket without a previous flight, get its dest
    starter = cache['NONE']
    log = [starter]
    # while the destination isn't none 
    while (cache[starter] != 'NONE'):
        # add the start location to the list, wire up the dest as the new start
        log.append(cache[starter])
        starter = cache[starter]
    log.append('NONE')
    return log
