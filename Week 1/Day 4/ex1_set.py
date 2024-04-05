my_fav_numbers = set([21, 5, 18, 31, 30, 28])
my_fav_numbers.add(14)
my_fav_numbers.add(48)

my_fav_numbers.remove(28)
print(f"My Favourite numbers are: {my_fav_numbers}")

friend_fav_numbers = [1, 4, 9, 27]
print(f"My friend's favourite numbers are: {friend_fav_numbers}")

our_fav_numbers = list(my_fav_numbers) + friend_fav_numbers
print(f"A combination of my friend's and I's favourite numbers are: {our_fav_numbers}")
