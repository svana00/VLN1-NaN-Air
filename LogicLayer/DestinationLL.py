from MODELS.destination import Destination

class DestinationLL():

    def __init__(self, ioAPI):
        self.ioAPI = ioAPI
   
    def get_destinations(self):
        ''' Returns a list of destination tuples containing id, country and city '''
        dest_list = self.ioAPI.load_all_destinations()
        return dest_list

    def get_destination_info(self, dest_id):
        dest_list = self.ioAPI.load_all_destinations()
        
        for dest in dest_list:
            if dest.get_id() == dest_id:
                return dest

    def lets_see_if_this_works(self):
        dest_instance_list = self.ioAPI.load_all_destinations()
        return dest_instance_list
    
    def create_new_destination(self, new_destination):

        # ---- Create Destination ID ----
        new_dest_id = new_destination.get_city()[:3].upper()

        dest_list = self.ioAPI.load_all_destinations()
        for dest in dest_list:
            temp_dest_id = dest.get_id()
            if new_dest_id == temp_dest_id:
                new_dest_id = new_destination.get_country()[:3].upper()
        
        new_destination.set_id(new_dest_id)
        dest_csv_string = new_destination.instance_to_csv_string()
        
        return self.ioAPI.create_new_destination(dest_csv_string)
    
    def store_new_changes(self, dest_instance_list):
        return self.ioAPI.store_destination_info(dest_instance_list)

    #def change_destination(self, old_str, new_str):
    #    old_file = self.ioAPI.get_all_file()
    #    new_file = open("Destinations_temp.csv", "w")
    #    for line in old_file:
    #        new_file.write(line.replace(old_str, new_str)
    #    return self.ioAPI.change_destination()