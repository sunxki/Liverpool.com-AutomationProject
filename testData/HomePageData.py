class HomePageData:

    """Data provided to the HomePage class """

    items = [{
        "brand":"Nintendo",
        "Model":"Switch",
        "color":"Azul",
        "price_down":5000,
        "price_up":10000
    },
        {
            "brand": "Aeropostale",
            "Model": "Camisa",
            "color": "Azul",
            "price_down": 5000,
            "price_up": 10000
        },
        {
            "brand": "Apple",
            "Model": "Macbook",
            "color": "Gris",
            "price_down": 5000,
            "price_up": 10000
        },
        {
            "brand": "Apple",
            "Model": "Iphone",
            "color": "Dorado",
            "price_down": 5000,
            "price_up": 10000
        },
        {
            "brand": "asdsd",
            "Model": "ggffgdfdd",
            "color": "sdsd",
            "price_down": 5000,
            "price_up": 10000
        },

    ]

    expected_data = []
    for element in items:
        search = ""
        for i in range(0, 3):
            search = search + list(element.values())[i] + " "
        expected_data.append(dict([('Search', search[0:len(search)-1])]))


    expected_smart = [{
        "Search": "SmartTV",
        "Brand": "LG",
        "Size": "50",
        "Price": 11000
    },
        {
            "Search": "SmartTV",
            "Brand": "Samsung",
            "Size": "43",
            "Price": 11000
        }
    ]