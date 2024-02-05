import random

game = "Abruptly Goblins"

gamers = []
def add_gamer(gamer, gamers_list):
    if "name" in gamer and "availability" in gamer:
        gamers_list.append(gamer)
    else: print("not enough information for " + gamer)

add_gamer({"name": "Kimberley Warner", "availability": ["Monday", "Tuesday", "Friday"]}, gamers)
add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)

print("\n")
print(gamers, "\n")

def build_daily_frequency_table():
    table = {"Monday": 0, "Tuesday": 0, "Wednesday": 0, "Thursday": 0, "Friday": 0, "Saturday": 0, "Sunday": 0}
    return table

count_availability = build_daily_frequency_table()

def calculate_availability(gamers_list, available_frequency):
    for player in gamers_list:
        for day in player["availability"]:
            available_frequency[day] += 1
            
calculate_availability(gamers, count_availability)

print(count_availability, "\n")

def find_best_night(availability_table):
    temp = max(availability_table.values())
    res = []
    for key in availability_table: 
        if availability_table[key] == temp:
            res.append(key)            
    return res

best_nights = find_best_night(count_availability)
if len(best_nights) > 1:
    print("There has been a tie: ", best_nights, "\n")

best_night = random.choice(best_nights)
if len(best_nights) > 1:
    print("The randomly selected winning night is: " + str(best_night), "\n")
else:
    print("The winning night is: " + str(best_night), "\n")

attending_game_night = []

def available_on_night(gamers_list, day):
    for gamer in gamers_list:
        if day in gamer["availability"]:
            attending_game_night.append(gamer["name"])
        else:
            continue

available_on_night(gamers, best_night)
print("Attendees for " + str(best_night) + ": " + str(attending_game_night))
print("\n")

form_email = """Hi {0}, \n\nThis week, the "{1}" game night will be played on {2} evening, commencing at 6pm.\n---\n\n"""

for name in attending_game_night:
    print(form_email.format(str(name), str(game), str(best_night)))