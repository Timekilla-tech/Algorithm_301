import heapq

def assignBicycles(students, bicycles):
    heap = []
    
    for i, (sx, sy) in enumerate(students):
        for j, (bx, by) in enumerate(bicycles):
            distance = abs(sx - bx) + abs(sy - by)
            heapq.heappush(heap, (distance, i, j))
    
    assigned_students = set()
    assigned_bikes = set()
    result = [-1] * len(students)
    
    while len(assigned_students) < len(students):
        distance, student_index, bike_index = heapq.heappop(heap)
        if student_index not in assigned_students and bike_index not in assigned_bikes:
            result[student_index] = bike_index
            assigned_students.add(student_index)
            assigned_bikes.add(bike_index)
    
    return result

students = [(0, 0), (1, 1)]
bicycles = [(0, 1), (4, 3), (2, 1)]
result = assignBicycles(students, bicycles)
print(result)
