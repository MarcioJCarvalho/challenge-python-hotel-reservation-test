def get_cheapest_hotel(number):   #DO NOT change the function's name
    cheapest_hotel = "cheapest_hotel_name"

    ## base de dados dos hoteis ##
    lakewood = ["Lakewood", 110.00, 90.00, 80.00, 80.00]
    bridgewood = ["Bridgewood", 160.00, 60.00, 110.00, 50.00]
    ridgewood = ["Ridgewood", 220.00, 150.00, 100.00, 40.00]

    data = number.split(":")
    client_type = data[0]
    dates = data[1]

    print(client_type)
    return cheapest_hotel

get_cheapest_hotel("Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)")