from collections import namedtuple
from itertools import chain

SimResult = namedtuple("SimResult", ["vel_x", "vel_y", "max_y", "landing"])
Target = namedtuple("Target", ["x1", "y1", "x2", "y2"])


def scan_vel_x(vel_x: int, target: Target) -> list[SimResult]:
    success_results: list[SimResult] = []
    vel_y = target.y2
    failures = 0
    max_failures = (
        abs(target.y2) - abs(target.y1) + abs(target.y2)
    )  # positive vel max failures + negative vel max failures
    while failures < max_failures:
        sim_result = simulate(vel_x, vel_y, target)
        if sim_result.landing == "target":
            success_results.append(sim_result)
        else:
            failures += 1
        vel_y += 1
    return success_results


def simulate(vel_x: int, vel_y: int, target: Target) -> SimResult:
    x, y = 0, 0
    max_y = 0
    step_vel_x, step_vel_y = vel_x, vel_y
    while y >= target.y2 and x <= target.x2:
        if y <= target.y1 and x >= target.x1:
            return SimResult(vel_x, vel_y, max_y, "target")
        x += step_vel_x
        y += step_vel_y
        if step_vel_x > 0:
            step_vel_x -= 1
        elif step_vel_x < 0:
            step_vel_x += 1
        step_vel_y -= 1
        max_y = max(y, max_y)
    return SimResult(
        vel_x, vel_y, -1, "missed_y" if target.x1 <= x <= target.x2 else "missed_x"
    )


t = Target(x1=20, y1=-5, x2=30, y2=-10)
results = list(chain(*(scan_vel_x(i, t) for i in range(1, t.x2 + 1))))

# 17
print(max(result.max_y for result in results))

# 17b
print(len(results))
