from models import Bike, Client, Partner
import pickle


clients = []

partners = []

def load_bikes():
    try:
        with open('bikes.pickle', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        store_bikes([])
        return []


def store_bikes(current_list):
    with open('bikes.pickle', 'wb') as file:
        pickle.dump(current_list, file)

bikes = load_bikes()