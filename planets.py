test_cases = int(input())

for _ in range(test_cases):
    n, c = list(map(int, input().split(' ')))
    planets = input().split(' ')

    orbit_count = {}
    for planet in planets:
        orbit_count[planet] = orbit_count.get(planet, 0) + 1

    min_cost = 0
    for val in orbit_count.values():
        min_cost += min(val, c)
    print(min_cost)

