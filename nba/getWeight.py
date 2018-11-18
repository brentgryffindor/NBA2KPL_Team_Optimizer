def get_training_set(data):
    for column in data:
        if column != "Team" and column != "Gamertag" and column != "Event":
            print(data[column].mean())
