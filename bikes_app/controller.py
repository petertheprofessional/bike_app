import db


class BikeController:
    def list_bikes(self):
        return db.load_bikes()

    def list_bikes_by_manufacturer(self, manufacturer):
        result = []
        for bike in db.bikes:
            if bike.manufacturer == manufacturer:
                result.append(bike)
        return result

    def add_bike(self, bike):
        current_list = db.load_bikes()
        current_list.append(bike)
        db.store_bikes(current_list)

    def remove_bike(self, id_: str):
        for bike in db.bikes:
            if bike.id == id_:
                db.bikes.remove(bike)

class ClientController:
    def list_all_clients(self):
        return db.clients

    def list_client_by_id(self, id):
        for client in db.clients:
            if client.id == id:
                return client.id, client.name, client.email, client.address

    def add_client(self, client):
        db.clients.append(client)

    def remove_client(self, id_: str):
        for client in db.clients:
            if client.id == id_:
                db.clients.remove(client)

class PartnerController:
    def list_all_partners(self):
        return db.partners

    def list_partners_by_email(self, email):
        results = []
        for partner in db.partners:
            if partner.email == email:
                results.append(partner)
        return results

    def add_partner(self, partner):
        db.partners.append(partner)

    def remove_partner(self, name: str):
        for partner in db.partners:
            if partner.name == name:
                db.partners.remove(partner)

class BillController:
    pass