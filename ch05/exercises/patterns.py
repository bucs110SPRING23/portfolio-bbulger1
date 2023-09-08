def star_pyramid(rows):
    for x in range(rows):
        stars = x*"*"
        print(stars)

def rstar_pyramid(rows):
    stars = ""
    for x in range(rows):
        x2 = rows - x
        stars = x2*"*"
        print(stars)


def main():
    rows = input("How many rows? ")
    rows = int(rows)
    star_pyramid(rows)
    rstar_pyramid(rows)

main()