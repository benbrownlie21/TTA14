magician_names = ["Harry Houdini", "David Blaine", "Criss Angel"]


def show_magicians():
    print(magician_names)


show_magicians()


def make_great(magicians):
    for magician in magicians:
        print(magician.title() + " the Great")


make_great(magician_names)
