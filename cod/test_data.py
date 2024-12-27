test_data = {
    "auth": {
        "username": "admin",
        "password": "password123"
    },
    "booking": {
        "valid": {
            "firstname": "Alexander",
            "lastname": "Grigor",
            "totalprice": 200,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2024-12-01",
                "checkout": "2024-12-10"
            },
            "additionalneeds": "Lunch"
        },
        "update":{
            "firstname": "Valera",
            "lastname": "Petrov",
            "totalprice": 200,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2024-11-16",
                "checkout": "2024-11-21"
            },
            "additionalneeds": "Dinner"
        },
        "get":{
            "firstname": "Alexander",
            "lastname": "Grigor",
            "totalprice": 180,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2024-10-10",
                "checkout": "2024-10-15"
            },
            "additionalneeds": "WiFi"
        },
        "delete":{
           "firstname": "Alexander",
            "lastname": "Grigor",
            "totalprice": 250,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2024-09-01",
                "checkout": "2024-09-10"
            },
            "additionalneeds": "Breakfast" 
        }
    }
}