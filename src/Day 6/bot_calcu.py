bot_name = input("Enter the bot name: ")

direction = "forward"
steps = 0
max_step = 100
STEP_DISTANCE_KM = 0.1   # 1 step = 0.1 km

print(f"\n{bot_name} started moving...\n")

while steps < max_step:
    event = input("Enter event (clear / human / obstacle / wall): ").lower()

    # HUMAN → STOP & WAIT
    if event == "human":
        print("Human detected. Bot stopped and waiting...")
        wait = input("Has the human passed? (yes/no): ").lower()
        if wait == "yes":
            print("Human passed. Bot resumed movement.")
        else:
            print("Bot still waiting...")
            continue

    # OBSTACLE / WALL → CHANGE DIRECTION
    elif event in ["wall", "obstacle"]:
        turn = input("Obstacle detected! Choose new direction (left/right): ").lower()
        if turn in ["left", "right"]:
            direction = turn
            print(f"Direction changed to {direction}")
        else:
            print("Invalid direction")
        continue

    # CLEAR PATH → MOVE
    elif event == "clear":
        steps += 1
        distance_km = steps * STEP_DISTANCE_KM
        print(f"{bot_name} moving {direction} | Distance: {distance_km} km")

    else:
        print("Invalid event")
        break                                           
    print("\n--- Travel Summary ---")
    print(f"Bot Name: {bot_name}")
    print(f"Final Direction: {direction}")
    print(f"Total Distance Travelled: {steps * STEP_DISTANCE_KM} km")
