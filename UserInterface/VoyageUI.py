
class VoyageUI():

    def __init__(self, llAPI):
        self.llAPI = llAPI

    def header(self, form, string):
        """ creates a header with the form as decoration before the chosen string """
        print("\n\n"+form*(13 - int((len(string)/2))) + string + form*(13 - int((len(string)/2))))

    def display_voyages_menu(self):
        """ displays the main menu for voyages giving the user 
        the options to change, add, or see overview of voyages """

        print("*"*26 + "\n\t VOYAGES \n"+"*"*26)
        print("1. CHANGE\n2. OVERVIEW\n3. ADD")
        var = input("\nInput a command: ")
        if var == "1":
            self.change_voyage()
        elif var == "2":
            self.overview_options() # menu for overview choices
        elif var == "3":
            self.create_voyage()


    def overview_options(self):
        """ menu for overview choices """
        self.header("-", " GET OVERVIEW ")
        print("1. ALL VOYAGES \n2. VOYAGES BY DATE")
        option = input("\nInput a command: ")
        if option == "1":
            self.show_all_voyages()
        elif option == "2":
            self.choose_date()

    def choose_date(self):
        self.header("-"," CHOOSE DATE ")
        print("With the format dd/mm/yyyy")
        date = input("Please enter the desired date: ")
        if date == "01/01/1000":
            print("whoop whoop!!")

    def show_voyages_by_date(self):
        pass

    def show_voyages_by_week(self):
        pass

    def show_one_voyage(self):
        pass

    def show_all_voyages(self):
        counter = 0
        voyages_dict = {}
        self.header("-", " ALL VOYAGES ")
        voyage_list = self.llAPI.get_all_voyages()
        for voyage in voyage_list:
            voyage_name = voyage_list[0]
            counter += 1
            voyages_dict[str(counter)] = voyage
            print("{}. {}".format(counter,voyage_name))
        print(voyages_dict)

        ###### option to choose a specific destination
        input_choice = input("To choose a specific voyage enter it's number: ")
        if input_choice in voyages_dict:
            self.get_voyage(voyages_dict[input_choice])
            #self.display_voyage(voyages_dict[input_choice])

    def display_voyage(self, a_voyage_info_list):
        self.header("*", " {} ".format(a_voyage_info_list[0]))
        counter = 0
        for info in a_voyage_info_list:
            counter += 1
            print("{}. {}".format(counter, info))

    def add_voyage_menu(self):
        self.header("*"," VOYAGES ")
        print("1. ADD VOYAGE\n2. ADD FROM EXISTING VOYAGES")
        menu_choice = input("Input command here: ")
        if menu_choice == "1":
            self.create_voyage
        elif menu_choice == "2":
            self.copy_voyage
        else:
            print("Invalid choice\nPlease try again")

    def create_voyage(self):
        ''' Returns a list of information about a new voyage '''

        flight_number_1_str = ""
        flight_number_2_str = ""
        destination_str = ""
        flight_1_date_str = ""
        flight_1_time_str = ""
        flight_2_date_str = ""
        flight_2_time_str = ""
        airplane_ID_str = ""
        captain_str = ""
        copilot_str = ""
        fsm_str = ""
        fa1_str = ""
        fa2_str = ""

        voyage_info_list = [flight_number_1_str, flight_number_2_str, destination_str, flight_1_date_str, flight_1_time_str, \
                            flight_2_date_str, flight_2_time_str, airplane_ID_str, captain_str,copilot_str, fsm_str, fa1_str, fa2_str] 

        voyage_info_print_list = ["destination","flight 1 date (YYYY/MM/DD)", "flight 1 time (XX:XX:XX)", \
                                "flight 2 date (YYYY/MM/DD)","flight 1 time (XX:XX:XX)", "airplane"] 

        insert_list = ["\nplease enter new {}: ".format(voyage_info_print_list[i]) for i in range(len(voyage_info_print_list))]
        VALID_LIST = ["" for i in range(13)]
        VALID_LIST.append("confirm")
        choice = input("To choose what you want to add, enter a number: ")

        while choice in VALID_LIST:
                
            if choice == "1":
                country_str = input("\nEnter new country: ")
                destination_info_list[0] = country_str

            elif choice == "2":
                city_str = input("Enter new city: ")
                destination_info_list[1] = city_str
                    
            elif choice == "3":
                airport_str = input("Enter new airport: ")
                destination_info_list[2] = airport_str
                    
            elif choice == "4":
                flight_time_str = input("Enter new flight time: ")
                destination_info_list[3] = flight_time_str

            elif choice == "5":
                distance_str = input("Enter distance: ")
                destination_info_list[4] = distance_str
                    
            elif choice == "6":
                name_of_contact_str = input("Enter name of contact: ")
                destination_info_list[5] = name_of_contact_str

            elif choice == "7":
                emergency_number_str = input("Enter emergency phone number: ")
                destination_info_list[6] = emergency_number_str

            elif choice == "confirm":
                print("Changes have been confirmed")
                return self.llAPI.create_new_destination(destination_info_list)

            self.header("-", " ADD DESTINATION ")
            print("\n1. COUNTRY: {}\n2. CITY: {}\n3. AIRPORT: {}\n4. FLIGHT TIME: {}\n5. DISTANCE: {}\n6. NAME OF CONTACT: {}\n7. EMERGENCY PHONE: {}".format(country_str, city_str, airport_str, flight_time_str, distance_str, name_of_contact_str, emergency_number_str))
            print("To confirm changes enter confirm")
            choice = input("\nInput what you want to add: ")



        """
        new_voyage_dict = {str(i+1) : voyage_info_list[i] for i in range(0, len(voyage_info_list) ) }

        #### the header and main body
        self.header("-", " ADD VOYAGE ")
        for i in range(len(voyage_info_list)):
            print("{}. {}: {}".format((i+1), test_list[i],voyage_info_list[i]))
        input_number_str = input("\nInput what you want to add: ")
        #######

        ###### a while loop that asks for and replaces values for a new voyage
        while input_number_str in new_voyage_dict.keys():
            choice = input(insert_list[int(input_number_str) - 1]) # prints out the corresponding text to what the user wants to change and takes in the input
            new_voyage_dict[input_number_str] = choice # changes the value in the dict to the entered value

            self.header("-", " ADD VOYAGE ")
            for i in range(len(voyage_info_list)):
                print("{}. {}: {}".format((i+1), test_list[i], new_voyage_dict[str(i+1)]))
            print("To confirm changes enter confirm")

            input_number_str = input("\nInput what you want to add: ")
            
        if input_number_str == "confirm":
            new_voyage_info_list = [val for val in new_voyage_dict.values()]
            return new_voyage_info_list
        """

    def copy_voyage(self):
        pass

    def assign_voyage(self):
        pass

    def change_voyage(self):
        pass
