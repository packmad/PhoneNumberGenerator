import argparse
import csv
import random


# https://it.wikipedia.org/wiki/Prefissi_telefonici_dei_cellulari_italiani
tim = [330, 331, 333, 334, 335, 336, 337, 338, 339, 360, 366, 368, 385]
vodafone = [340, 342, 344, 345, 346, 347, 348, 349]
wind = [320, 324, 327, 328, 329, 380, 388, 389]
tre = [391, 392, 393, 397]

prefixes = tim + vodafone + wind + tre
int_prefix = "+39"
googlecsv = ["Name", "Given Name", "Group Membership", "Phone 1 - Value"]
phone_set = set()


def get_rnd_phone():
    ret = int_prefix + str(random.choice(prefixes))
    for i in range(7):
        ret += str(random.randrange(0, 7))
    return ret


def create_list():
    while True:
        rnd_phone = get_rnd_phone()
        if rnd_phone not in phone_set:
            break
    name = "c" + str(len(phone_set))  # contact name
    phone_set.add(rnd_phone)
    return [name, name, "* My Contacts", rnd_phone]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generates Italian phone numbers randomly')
    parser.add_argument('-f', '--format', help='The output format (csv|txt)', required=True)
    parser.add_argument('-o', '--output', help='The output file', required=True)
    parser.add_argument('-s', '--size', help='How many numbers will be generated', required=True)
    args = vars(parser.parse_args())

    size = int(args['size'])
    with open(args['output'], 'w') as file:
        if args['format'] == 'csv':  # for google contacts import
            csv_writer = csv.writer(file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(googlecsv)
            for i in range(size):
                csv_writer.writerow(create_list())
        elif args['format'] == 'txt':
            for i in range(size):
                file.write(get_rnd_phone() + '\n')
    file.close()
    print('--end---')
