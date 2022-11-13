from datetime import datetime
import random
import time
import csv
from track import *
from car import *



def lap_time(start):
    race_time = time.time() - start
    race_time = round(race_time, 2)
    return race_time


def timestring():
    pass


def race():
    car_1 = Car.car_symbol(car1)
    car_2 = Car.car_symbol(car2)
    speed_1 = random.randint(1, 4)
    speed_2 = random.randint(1, 4)
    track_1 = Track.track_compiler(race_track)
    track_2 = Track.track_compiler(race_track)
    print(*track_1, sep="")
    print(*track_2, sep="")
    track_1.insert(0, car_1)
    track_2.insert(0, car_2)
    print(*track_1, sep="")
    print(*track_2, sep="")
    track_length = len(track_1)
    time.sleep(1)
    at_the_moment = time.time()
    for race in range(len(track_1)):
        current_pos_1 = track_1.index(car_1)
        current_pos_2 = track_2.index(car_2)
        next_pos_1 = current_pos_1 + speed_1
        next_pos_2 = current_pos_2 + speed_2
        track_1.pop(current_pos_1)
        track_2.pop(current_pos_2)
        track_1.insert(next_pos_1, car_1)
        track_2.insert(next_pos_2, car_2)
        print(*track_1, sep="")
        print(*track_2, sep="")
        time.sleep(1)
        if track_1[-1] == car_1 and track_2[-1] == "|":
            fin_time = lap_time(at_the_moment)
            print("Car 'X' Won! \nRace Finished!\n ", fin_time, "seconds")
            with open("results.csv", "a") as result:
                result.write(f"Car X Won race at {fin_time} seconds\n")
            break
        if track_2[-1] == car_2 and track_1[-1] == "|":
            fin_time = lap_time(at_the_moment)
            print("Car 'O' Won! \nRace Finished!", fin_time, "seconds")
            with open("results.csv", "a") as result:
                result.write(f"Car O Won race at {fin_time} seconds\n")
            break
        if track_1[-1] == car_1 and track_2[-1] == car_2:
            fin_time = lap_time(at_the_moment)
            print("TIE!\nRace Finished!", fin_time, "seconds")
            with open("results.csv", "a") as result:
                result.write(f"There is a TIE at {fin_time} seconds\n")
                break


class ScoreBoard:
    pass


def menu():
    raw_input = None
    while True:
        raw_input = input("1 Start race\n2 See score-board\n3 Quit the game")
        if raw_input.isnumeric():
            raw_input = int(raw_input)
            if raw_input == 1:
                race()
                continue
            if raw_input == 2:
                with open("results.csv", 'r') as file:
                    csvreader = csv.reader(file)
                    for row in csvreader:
                        print(row)
                continue
            if raw_input == 3:
                with open("results.csv", 'w'):
                    pass
                print("Thank you for the game!")
                break
            else:
                print("Not accepted numeric value")
                continue
        else:
            print("Please enter a number")
            continue

menu()
