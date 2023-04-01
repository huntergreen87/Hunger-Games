import random
import names
import time
import sys

year = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", "12th", "13th", "14th", "15th",
        "16th", "17th", "18th", "19th", "20th", "21st", "22nd", "23rd", "24th", "25th", "26th", "27th", "28th", "29th", "30th", "31st", "32nd", "33rd", "34th", "35th", "36th"]
current_year = ""
tributes = {}
dead_tributes = {}
victors = {}
death_count = 0

random_events = ["Volcano Erupts in the Arena", "Rapid Dogs swarm the arena",
                 "Poisonous Gas fills into the arena", "Tracker Jackers swarm", "Flesh eating bugs begin to swarm"]


def std_print_slowly(text):
    for letter in text:
        print(letter, end='')
        sys.stdout.flush()
        time.sleep(0.07)


class Tributes():
    def __init__(self, tribute_name, district, gender):
        self.name = tribute_name
        self.district = district
        self.score = random.randint(1, 12)
        self.hp = random.randint(100, 150)
        self.dmg = random.randint(10, 30)
        self.gender = gender

    def generate_key(self):
        return f"District {self.district} {self.gender}"


for number in range(24):
    if number % 2 == 0:
        tributes[f"District {(number // 2) + 1} Female"] = Tributes(
            names.get_full_name(gender="female"), (number // 2) + 1, "Female")
    else:
        tributes[f"District {(number // 2) + 1} Male"] = Tributes(
            names.get_full_name(gender="male"), (number // 2) + 1, "Male")


def reset():
    global current_year, tributes, dead_tributes, death_count
    current_year = ""
    tributes = {}
    dead_tributes = {}
    death_count = 0

# Initiate Game Play#


def main_menu():
    global current_year
    while True:
        current_year = random.choice(year)
        print("\033[1;36m" + "\033[1m" +
              '\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' + "\033[1m"+"\033[1;36m\n")
        print(f"Welcome to the {current_year} annual Hunger Games!\n")
        print("\033[1;36m" + "\033[1m" +
              'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' + "\033[1m"+"\033[1;36m\n")
        time.sleep(0.5)
        std_print_slowly(
            'Would you like to volunteer as Tribute (Y) or (N)? Press (Q) to quit Press (V) to view the Victors. ')
        volunteer = input()
        if volunteer.upper() == 'Q':
            print("How Dare you rebel against the capitol...")
            exit()
        if volunteer.upper() == 'Y':
            break
        if volunteer.upper() == 'N':
            winner = names.get_full_name()
            win_dist = str(random.randint(1, 13))
            win_cat = winner + ", District " + win_dist
            print(f"The Winner is {winner} from District {win_dist}!")
            victors.update({win_cat: current_year})
            if current_year in year:
                year.remove(current_year)
            current_year = ""
        if volunteer.upper() == "V":
            if len(victors) == 0:
                print("There are currently no Victors")
            else:
                print(victors)


main_menu()

user_district = int(input("\nWhat district are you from? (1-12) "))
user_name = input("\nWhat's your name? ")
while True:
    option_1 = input("\nAre you a (M)ale tribute or a (F)emale tribute? ")
    if option_1.upper() == "M":
        gender_modifier = 1
        gender = "Male"
        break
    if option_1.upper() == "F":
        gender_modifier = 2
        gender = "Female"
        break
    print("Hmm, try again")
# Display the tributes: Tribute Parade: This replaces the Tribute with User Data
user_key = f"District {user_district} {gender}"
user = tributes[user_key]
user.name = user_name

std_print_slowly("\nThis years' Tributes are:\n")
time.sleep(1.0)
for tribute in tributes.values():
    std_print_slowly(
        f"District {tribute.district} {tribute.gender} : {tribute.name}")
    time.sleep(0.5)

tribute_list = list(tributes.items())
random.shuffle(tribute_list)
tributes = dict(tribute_list)

# Your Mentor
mentor = names.get_full_name()
std_print_slowly(
    f"\n\nYou return from the Tribute Parade and meet with your mentor: {mentor}\n")
time.sleep(0.75)
std_print_slowly(f"{mentor}: well let's have a look at what we got...")
time.sleep(0.75)

talent_matrix = [["Hunting", 150, 25], ["Combat", 125, 20],
                 ["Camoflague", 125, 15], ["Strength", 125, 20]]

while True:
    print("\n[1] Hunting")
    print("[2] Combat")
    print("[3] Camoflague")
    print("[4] Strength")
    talent = int(input(f"\n{mentor}: Do you have any skills? "))
    if 1 <= talent <= 4:
        talents = talent_matrix[talent - 1]
        user.talent = talents[0]
        user.hp = talents[1]
        user.dmg = talents[2]
        break
    print(f"{mentor}: Hmmm...Not sure I know that one.")
time.sleep(1.5)
print(f"{mentor}: All in all.....I like your odds.\n")
time.sleep(1.5)
print("Tribute Stats:\n")
print(f"Tribute Name: {user.name}\nGender: {user.gender}\nDistrict:{user.district}\nTalent: {user.talent}\nHP: {user.hp}\nDamage: {user.dmg}")
time.sleep(1.5)
# Assess overall score from Game Makers on a scale from 1-12
print(f"\n\n{user.name} steps in front of the Game Makers and demonstrated your {user.talent} skills. But...how generous were they?\n\n")
time.sleep(1.0)
print(f"{user.name} from District {user.district} with a score of:")
time.sleep(1.0)
print(f"\n{user.score}!\n")
if 1 <= user.score <= 3:
    user.hp += 4
    user.dmg += 4
    print(f"{mentor}: Well that's not good...")
if 4 <= user.score <= 5:
    user.hp += 6
    user.dmg += 6
    print(f"{mentor}: Well that dog don't hunt...")
if 6 <= user.score <= 7:
    user.hp += 8
    user.dmg += 8
    print(f"{mentor}: If you're lucky you'll make top 12...")
if 8 <= user.score <= 10:
    user.hp += 10
    user.dmg += 10
    print(f"{mentor}: We can certainly work with that...")
if user.score == 11:
    user.hp += 15
    user.dmg += 15
    print(f"{mentor}: ... Wow....very impressed!")
if user.score == 12:
    user.hp += 20
    user.dmg += 20
    print(f"{mentor}: Clearly the Capital wants you dead...")
time.sleep(1.0)
print("\nYour new stats: ")
print(f"\nTribute: {user.name}\nDistrict: {user.district}\nGender: {user.gender}\nHP: {user.hp}\nDMG: {user.dmg}\n")

time.sleep(2.5)
print("You are flown from the tribute center to an undisclosed location were you enter the Launch Room.\n")
time.sleep(2.5)
print("You say goodbye to your stylist and hear the countdown to enter the tubes. Inside the tube is a metal plate, which the tube closed around.\n")
time.sleep(2.5)
print("Slowly, you are raised up until you find yourself standing on a platform surrounded by other tributes. Slowly the 1 minute counter starts to tick closer and closer to one...\n")
time.sleep(2.5)
print(
    f"Your heart begins to race as you look around at the other tributes.\n")
time.sleep(2.0)
print("And the clock continues to count down...10...9..8...\n")

# Cornucopia Action#
print("Now is the time to decide...what will you do when the timer runs out?\n")
number_killed = random.randint(1, 12)
while True:
    option_1 = input("\n(R)un and hide, (F)ight at the Cornucopia? ")
    if option_1.upper() == "R":
        print("You turn away from the Cornucopia and fly into the woods, evading all enemies and escaping the blood bath.")
        print(number_killed)
        while number_killed > 0:
            choice = random.choice(list(tributes.keys()))
            if choice != user_key:
                dead_trib = tributes[choice]
                dead_tributes[dead_trib.name] = dead_trib.district
                tributes.pop(choice)
                number_killed -= 1
                death_count += 1
        break
    elif option_1.upper() == "F":
        # Random probability of success you either live, die, or lose HP
        probability = random.random()
        if probability >= 0.8:
            tributes.pop(user_key)
            print("You died\n")
            dead_tributes.update({user_key: user.name})
            winner = str(random.choice(list(tributes.values())))
            win_trib = tributes[winner]
            win_cat = f"District {win_trib.district}, {win_trib.name}"
            victors.update({win_cat: current_year})
            print(
                f"The Winner is {win_trib.name} from District {win_trib.district}!")
            if current_year in year:
                year.remove(current_year)
            reset()
            main_menu()
        else:
            while number_killed > 0:
                choice = random.choice(list(tributes.keys()))
                if choice != user_key:
                    dead_trib = tributes[choice]
                    dead_tributes[dead_trib.name] = dead_trib.district
                    tributes.pop(choice)
                    number_killed -= 1
                    death_count += 1
            print("\nYou somehow survived and made it to the woods\n")
        break
    else:
        print("Hmm, try again")

print(f"\nNumber of dead tributes: {death_count}")
print(f"\nDead Tributes: {dead_tributes}\n")


def main_play():
    global dead_tributes, death_count, tributes, current_year
    while len(tributes) > 2:
        print("\n[1] Gamemaker Event")
        print("\n[2] Hunt down a Tribute")
        choice = input("\nWhat's your next move? ")
        number_killed = random.randint(1, (len(tributes)-2))
        if choice == "1":
            event = random.choice(random_events)
            print(f"All of the sudden {event}!")
            probability = random.random()
            if probability >= 0.8:
                tributes.pop(user_key)
                print("You died\n")
                dead_tributes.update({user_key: user.name})
                winner = random.choice(list(tributes.keys()))
                win_trib = tributes[winner]
                win_cat = f"District {win_trib.district}, {win_trib.name}"
                victors.update({win_cat: current_year})
                print(
                    f"The Winner is {win_trib.name} from District {win_trib.district}!")
                if current_year in year:
                    year.remove(current_year)
                reset()
                main_menu()
                break
            else:
                while number_killed > 0:
                    choice = random.choice(list(tributes.keys()))
                    if choice != user_key:
                        dead_trib = tributes[choice]
                        dead_tributes[dead_trib.name] = dead_trib.district
                        tributes.pop(choice)
                        number_killed -= 1
                        death_count += 1
                print(f"\nNumber of dead tributes: {death_count}")
                print(f"\nDead Tributes: {dead_tributes}\n")
                main_play()
                break
        if choice == "2":
            opponent = user
            while opponent == user:
                opponent = random.choice(list(tributes.values()))
            print(
                f"\nYou make your way through the arena and encounter {opponent.name}. Only one of you will walk away.\n")
            # if random_tribute in tributes:#
            while True:
                if opponent.hp > 0:
                    opponent.hp = opponent.hp-user.dmg
                    print(f"{user.name} wounded {opponent.name}")
                    print(f"{opponent.name}'s current HP is {opponent.hp}")
                    print("\n")
                if opponent.hp <= 0:
                    target_key = opponent.generate_key()
                    tributes.pop(target_key)
                    print(f"You killed {opponent.name}")
                    dead_tributes.update({target_key: opponent.name})
                    death_count += 1
                    main_play()
                    # Remove the opponent value from tributes
                if user.hp > 0:
                    user.hp = user.hp-opponent.dmg
                    print(f"{opponent.name} has wounded {user.name}!!")
                    print(f"Your current HP is {user.hp}\n")
                if user.hp <= 0:  # Remove you from Tributes and end the game with a random remaining winner
                    target_key = user_key
                    tributes.pop(target_key)
                    print("You died\n")
                    dead_tributes.update({target_key: user_name})
                    death_count += 1
                    winner = str(random.choice(list(tributes.values())))
                    if winner in tributes.values():
                        win_dist = tributes.district
                        win_cat = winner + ", District " + win_dist
                        victors.update({win_cat: current_year})
                    print(f"The Winner is {winner} from District {win_dist}!")
                    if current_year in year:
                        year.remove(current_year)
                    reset()
                    main_menu()
                    break
        print("Invalid Option. Pick again.")

    print(
        f"\nThis is it. The final battle. You and {opponent.name}. Only one of you will become a Victor.\n")
    # if random_tribute in tributes:#
    while True:
        if opponent.hp > 0:
            opponent.hp = opponent.hp-user.dmg
            print(f"{user.name} wounded {opponent.name}")
            print(f"{opponent.name}'s current HP is {opponent.hp}")
            print("\n")
        if opponent.hp <= 0:
            target_key = opponent.generate_key()
            tributes.pop(target_key)
            print(f"You killed {opponent.name}")
            dead_tributes.update({target_key: opponent.name})
            death_count += 1
            print(f"A voice comes out of no where:\n")
            print(
                f"Claudius Templesmith: Ladies and Gentlemen, may I present the winner of the {current_year} annual Hunger Games. {user.name}")
            winner = user.name
            win_cat = f"District {user.district}, {user.name}"
            victors.update({win_cat: current_year})
            print(victors)
            if current_year in year:
                year.remove(current_year)
            reset()
            main_menu()
        if user.hp > 0:
            user.hp = user.hp-opponent.dmg
            print(f"{opponent.name} has wounded {user.name}!!")
            print(f"Your current HP is {user.hp}\n")
        if user.hp <= 0:  # Remove you from Tributes and end the game with a random remaining winner
            target_key = user_key
            tributes.pop(target_key)
            print("You died\n")
            dead_tributes.update({target_key: user_name})
            death_count += 1
            winner = opponent.name
            win_cat = f"District {opponent.district}, {opponent.name}"
            victors.update({win_cat: current_year})
            print(
                f"The Winner is {opponent.name} from District {opponent.district}!")
            if current_year in year:
                year.remove(current_year)
            reset()
            main_menu()


main_play()
