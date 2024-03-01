import math

def solve_projectile_motion(range_, initial_velocity, launch_angle):
    # Convert launch angle from degrees to radians
    launch_angle_rad = math.radians(launch_angle)
    
    # Acceleration due to gravity (m/s^2)
    g = 9.81
    
    # Calculate time of flight
    time_of_flight = (2 * initial_velocity * math.sin(launch_angle_rad)) / g
    
    # Calculate maximum height reached
    max_height = (initial_velocity**2 * (math.sin(launch_angle_rad))**2) / (2 * g)
    
    return time_of_flight, max_height

def main():
    range_ = float(input("Enter the horizontal distance traveled by the projectile (meters): "))
    initial_velocity = float(input("Enter the initial velocity of the projectile (m/s): "))
    launch_angle = float(input("Enter the launch angle of the projectile (degrees): "))

    time_of_flight, max_height = solve_projectile_motion(range_, initial_velocity, launch_angle)

    print("Time of flight:", round(time_of_flight, 2), "seconds")
    print("Maximum height reached:", round(max_height, 2), "meters")

if __name__ == "__main__":
    main()

confirmation = input("Press ENTER to exit")