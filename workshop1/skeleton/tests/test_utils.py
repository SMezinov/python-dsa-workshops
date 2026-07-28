def add_to_stack(*lst, stack):
    for element in lst:
        stack.push(element)

def add_to_queue(*lst, queue):
    for element in lst:
        queue.enqueue(element)