def Band_name_Generator():
    print("Hello Human,\nWelcome To The Band Name Generator.")
    city = input("Enter a city you lived in - ")
    animal = input("Enter your favorte animal - ")
    return "1st Band Name Generated - The {} {}s\n2nd Band name Generated - The {}s of {}".format(city, animal, animal, city)

print(Band_name_Generator())