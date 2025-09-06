# Function 1: Calculate the height of the ball after time t
# This function should take the initial height h0 and time t as inputs, and return the height at time t.
# Round up to one decimal point
def calculate_height(h0, t):
    # TODO: Implement this function
    i_height=float(input("Enter initial height: "))
    time=float(input("Enter time: "))
    g=-9.8
    f_height=i_height+0.5*g*time**2
    rounded_height=round(f_height, 1)
    print(f"Height of ball at time {time} seconds = {rounded_height} meters")

# Function 2: Calculate the distance traveled by the car
# This function should take the time t as input and return the distance traveled by the car.
def calculate_car_distance(t):
    # TODO: Implement this function
    speed=20
    time=float(input("Enter time for car (in seconds): "))
    distance=speed*time
    rounded_distance=round(distance, 1)
    print(f"The car will travel {rounded_distance} meters in {time} seconds")
