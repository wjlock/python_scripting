hello_file = open("hello.txt", "w")
ga_intro = "Hell to all of my GA family"
hello_file.write(ga_intro)
# print(hello_file.read())

# hello_file.close()

car_file = open("car.txt", "w")
new_car_list = "Pickles \nPickles Two, The Revenge"
car_file.write(new_car_list)
# print(car_file.read())
car_file.close()


# my_new_file = open('person.txt', "w")
# my_new_file.write('Bobby')
# my_new_file.close()


# Write to a file
# with open('person.txt', "w") as person_file:
#     person_file.write('Ronald')


# Append to a file
# with open("person.txt", 'a') as person_file:
#     person_file.write('\nVictor')

# with open('person.txt', 'r+') as person_file:
#     print(person_file.read())
#     person_file.write('\nHello')
#     print(person_file.read())


# my_new_file = open('person.txt', 'r+')
# my_new_file.write('Rome Bell\nMike\nJoe')
# my_new_file.close()

# with open('person.txt') as people:
#     people_list = people.readlines()

#     for each_person in people_list:
#         print(each_person)

with open('prime_numbers.txt') as numbers:
    numbers_list = numbers.readlines()

    def double(num):
        print(num*2)

    for each_number in numbers_list:
        double(int(each_number))


with open('one_to_hundred.txt') as numbers:
    numbers_list = numbers.readlines()
    result = []

    for each_number in numbers_list:
        if each_number == "Five" or "Fifteen":
            result.append(each_number)
    print(result)
