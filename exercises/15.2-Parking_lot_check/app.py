parking_state = [
    [1, 1, 1],
    [0, 0, 0],
    [1, 1, 2]
]

# Your code go here:


def get_parking_lot(matrix):
    state = {"total_slots":0,
             "available_slots": 0,
             "occupied_slots": 0}
    for i in range(len(matrix)):
        for y in range(len(matrix)):
            if matrix[i][y] == 0: pass
            elif matrix[i][y] == 1: state["occupied_slots"] += 1
            elif matrix[i][y] == 2: state["available_slots"] += 1
    
    state["total_slots"] = state["occupied_slots"] + state["available_slots"]
        

    return state

print(get_parking_lot(parking_state))
                   
