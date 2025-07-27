body_temp = float(input("please enter your temp body:"))
suger = 200
if body_temp > 39.5:
    print("go to doctor argent!!")
    print("take Analgetic until hospital!")
    print("call 101 if you feel more bad!")
elif 38 < body_temp < 39.6:
    print("follow on your body temp!")
elif suger > 150:
    print("take insulin!")
else:
    print("every thing is good")

print("make happen any way!")
