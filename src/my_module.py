def get_cheapest_hotel(number):   #DO NOT change the function's name
    cheapest_hotel = "cheapest_hotel_name"

    ## base de dados dos hoteis ##
    lakewood = ["Lakewood", 110.00, 90.00, 80.00, 80.00]
    bridgewood = ["Bridgewood", 160.00, 60.00, 110.00, 50.00]
    ridgewood = ["Ridgewood", 220.00, 150.00, 100.00, 40.00]

    data = number.split(":")
    client_type = data[0]
    dates = data[1]

    weekend = 0
    weekday = 0
    # pegando os tipos de dias da semana
    date = dates.split(",")
    for day in date:
        day_type = (day[day.find('(')+1:day.find(')')])
        sat_n_sun = ["sat", "sun"]
        if day_type not in sat_n_sun:
            weekday += 1
        else:
            weekend += 1
    print(weekday)
    print(weekend)    

    return cheapest_hotel

get_cheapest_hotel("Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)")