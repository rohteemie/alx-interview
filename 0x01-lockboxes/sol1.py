def canUnlockAll(boxes):
    # create a set of visited boxes, initially containing only the first box
    visited = set([0])
    
    # create a stack to keep track of boxes to visit
    stack = [0]
    
    # loop through the stack
    while stack:
        # pop a box from the stack
        box = stack.pop()
        
        # loop through all the keys in the current box
        for key in boxes[box]:
            # check if the key is a valid box and has not been visited
            if key not in visited and 0 <= key < len(boxes):
                # add the box to the visited set and the stack
                visited.add(key)
                stack.append(key)
    
    # check if all boxes have been visited
    return len(visited) == len(boxes)

"""
The algorithm used in this code is Depth First Search (DFS). The goal of the algorithm is to visit all boxes in a depth-first manner, starting from the first box, and checking all keys in each box along the way. The algorithm terminates when all boxes have been visited or the stack is empty, meaning that no more boxes can be visited.

The time complexity of this algorithm is O(n + m), where n is the number of boxes and m is the total number of keys in all boxes. In the worst case, the algorithm may need to visit all boxes and keys, leading to a time complexity of O(n + m). However, in the best case, the algorithm may only need to visit a few boxes and keys, leading to a much better time complexity.

The visited set is used to keep track of visited boxes and its average time complexity for adding and checking elements is O(1). The stack is used to keep track of boxes to visit and its average time complexity for popping and appending elements is O(1). Overall, the algorithm has a linear time complexity."""
