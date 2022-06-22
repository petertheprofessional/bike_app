from typing import List

from fastapi import APIRouter
from controller import BikeController, ClientController, PartnerController
from models import Bike, Client, Partner


bike_routes = APIRouter()
bike_controller = BikeController()
client_routes = APIRouter()
client_controller = ClientController()
partner_routes = APIRouter()
partner_controller = PartnerController()

@bike_routes.get('/bikes')
def get_bikes():
    return bike_controller.list_bikes()


@bike_routes.get('/bikes/by_manufacturer')
def get_bikes_by_manufacturer(manufacturer: str):
    return bike_controller.list_bikes_by_manufacturer(manufacturer)


@bike_routes.post('/bikes')
def post_bike(bike: Bike):
    bike_controller.add_bike(bike)


@bike_routes.delete('/bikes/{id_}')
def delete_bike(id_: str):
    bike_controller.remove_bike(id_)


@client_routes.get('/clients')
def get_clients():
    return client_controller.list_all_clients()

@client_routes.get('/clients/by_id')
def get_clients_by_id(id: int):
    return client_controller.list_client_by_id(id)

@client_routes.post('/clients')
def post_clients(client: Client):
    client_controller.add_client(client)


@client_routes.delete('/clients/{id_}')
def delete_client(id_: str):
    client_controller.remove_client(id_)


@partner_routes.get('/partners')
def get_partners():
    return partner_controller.list_all_partners()


@partner_routes.get('/partners/by_email')
def get_partners_by_email(email: str):
    return partner_controller.list_partners_by_email(email)


@partner_routes.post('/partners')
def post_partners(partner: Partner):
    partner_controller.add_partner(partner)


@partner_routes.delete('/partners/{id_}')
def delete_partner(name: str):
    partner_controller.remove_partner(name)
