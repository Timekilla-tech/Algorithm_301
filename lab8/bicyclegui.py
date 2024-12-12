import tkinter as tk
from tkinter import messagebox
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
        _, student_index, bike_index = heapq.heappop(heap)
        if student_index not in assigned_students and bike_index not in assigned_bikes:
            result[student_index] = bike_index
            assigned_students.add(student_index)
            assigned_bikes.add(bike_index)

    return result


def draw_grid(canvas, grid_size):
    for i in range(0, grid_size * 50, 50):
        canvas.create_line(i, 0, i, grid_size * 50, fill="gray")
        canvas.create_line(0, i, grid_size * 50, i, fill="gray")


def draw_entities(canvas, students, bicycles, assignments):
    # Draw students
    for i, (x, y) in enumerate(students):
        canvas.create_oval(
            x * 50 + 10, y * 50 + 10, x * 50 + 40, y * 50 + 40, fill="blue", tags=f"student_{i}"
        )
        canvas.create_text(x * 50 + 25, y * 50 + 25, text=f"S{i}", fill="white")

    # Draw bicycles
    for i, (x, y) in enumerate(bicycles):
        canvas.create_rectangle(
            x * 50 + 10, y * 50 + 10, x * 50 + 40, y * 50 + 40, fill="red", tags=f"bike_{i}"
        )
        canvas.create_text(x * 50 + 25, y * 50 + 25, text=f"B{i}", fill="white")

    # Draw assignments
    for student_index, bike_index in enumerate(assignments):
        sx, sy = students[student_index]
        bx, by = bicycles[bike_index]
        canvas.create_line(
            sx * 50 + 25, sy * 50 + 25, bx * 50 + 25, by * 50 + 25, fill="green", width=2
        )


def run_assignment():
    # Grid, Students, and Bicycles
    grid_size = 10
    students = [(1, 0), (1, 1), (3, 3)]
    bicycles = [(0, 1), (4, 3), (2, 1)]

    # Perform assignment
    assignments = assignBicycles(students, bicycles)

    # Clear canvas and draw new grid
    canvas.delete("all")
    draw_grid(canvas, grid_size)
    draw_entities(canvas, students, bicycles, assignments)

    # Show result in a messagebox
    result_text = "\n".join([f"Student {i} -> Bicycle {assignments[i]}" for i in range(len(students))])
    messagebox.showinfo("Assignments", f"Assignments:\n{result_text}")


# Tkinter GUI
root = tk.Tk()
root.title("Student-Bicycle Assignment")

# Canvas for the grid
canvas = tk.Canvas(root, width=500, height=500, bg="white")
canvas.pack()

# Button to start assignment
assign_button = tk.Button(root, text="Run Assignment", command=run_assignment)
assign_button.pack()

# Initial grid
draw_grid(canvas, 10)

root.mainloop()
