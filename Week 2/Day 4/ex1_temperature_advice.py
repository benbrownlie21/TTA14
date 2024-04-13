from random import uniform


def get_random_temp(season):
    if season == "Winter":
        return round(uniform(-10, 5), 2)
    elif season == "Spring":
        return round(uniform(6, 16), 2)
    elif season == "Summer":
        return round(uniform(25, 40), 2)
    elif season == "Autumn":
        return round(uniform(17, 24), 2)
    else:
        return None


def main():
    while True:
        user_input = input("Type in a season: ")
        receive_random_temp = get_random_temp(user_input)
        if receive_random_temp is not None:
            if receive_random_temp < 0:
                print(
                    f"Brrr at {receive_random_temp}°C, it's freezing today! Better wear some extra layers"
                )
            elif 0 < receive_random_temp <= 16:
                print(
                    f"It's quite chilly at {receive_random_temp}°C, don't forget your coat!"
                )
            elif 16 < receive_random_temp <= 23:
                print(
                    f"It's starting to warm up at {receive_random_temp}°C, no need for a coat today!"
                )
            elif 24 <= receive_random_temp <= 32:
                print(
                    f"It looks like summer at {receive_random_temp}°C, t-shirt and shorts day!"
                )
            else:
                print(
                    f"Wow it's a scorcher at {receive_random_temp}°C, you MUST use sun block!!!"
                )
            break
        else:
            print("Please enter a valid season!")


main()
