import random
import csv

# https://it.wikipedia.org/wiki/Prefissi_telefonici_dei_cellulari_italiani
tim = [330, 331, 333, 334, 335, 336, 337, 338, 339, 360, 366, 368, 385]
vodafone = [340, 342, 344, 345, 346, 347, 348, 349]
wind = [320, 324, 327, 328, 329, 380, 388, 389]
tre = [391, 392, 393, 397]

prefixes = tim + vodafone + wind + tre
googlecsv = ["Name", "Given Name", "Group Membership", "Phone 1 - Value"]
phone_set = set()


def get_rnd_phone():
    ret = "+39" + str(random.choice(prefixes))
    for i in range(7):
        ret += str(random.randrange(0, 7))
    return ret


def create_list():
    while True:
        rnd_phone = get_rnd_phone()
        if rnd_phone not in phone_set:
            break
    name = "c" + str(len(phone_set))
    phone_set.add(rnd_phone)
    return [name, name, "* My Contacts", rnd_phone]


if __name__ == "__main__":
    with open('phones.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(googlecsv)
        for i in range(24998):
            spamwriter.writerow(create_list())