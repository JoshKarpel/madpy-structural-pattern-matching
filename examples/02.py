# Pattern matching is *not* faster than if/elif trees!
# It is *syntactic sugar* designed to make code more readable.

# To see how that works, we need a more complex example.

from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


def describe_list_of_points(points: list[Point]) -> str:
    match points:
        case []:
            return "No points in the list."

        case [Point(0, 0)]:
            return "The origin is the only point in the list."

        case [Point(x, y)]:
            return f"A single point {x}, {y} is in the list."

        case [Point(int(), 0) | Point(0, int())]:
            return "A single point on the X or Y axis is in the list."

        case [Point(0, y1), Point(0, y2)]:
            return f"Two points on the Y axis at {y1}, {y2} are in the list."

        case [Point(x, y), *_] if x == y:
            return "The first point in the list is on the diagonal."

        case _:
            return "Something else is found in the list."


print(f"{describe_list_of_points([])=}")
print(f"{describe_list_of_points([Point(0, 2)])=}")
print(f"{describe_list_of_points([Point(1, 2)])=}")
print(f"{describe_list_of_points([Point(0, 1), Point(0, 4)])=}")
print(f"{describe_list_of_points([Point(0, 1), Point(0, 4), Point(0, 5)])=}")
print(f"{describe_list_of_points([Point(0, 1), Point(0, 4), Point(2, 5)])=}")
print(f"{describe_list_of_points([Point(1, 1), Point(0, 4)])=}")
