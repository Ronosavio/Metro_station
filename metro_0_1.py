from abc import ABC, abstractmethod

visited_central = []
visited_airport = []

#keeping track of metrocard records
card_records = {}

#keeping track of the customer prizes based on their category
Adult_price = 200
Senior_price = 100
Kids_price = 50

#The value of the Discount percentage 
Discount_percent = 0.50 # 50% discount

class Passengers(ABC):
      @abstractmethod
      def passengers(self, card_number, balance):
          pass
      
 #Keeps track of the count of overall adults in the metro and balance requirements of the adult passengers to travel.
 #If the balance is less then the auto recharge function is initiated with the 2 % interest deduction for the auto recharge amount
class Adult(Passengers):
      adult_passenger_count = 0
      def passengers(self, card_number, balance):
          Type = 'ADULT'
          interest = 0
          Auto_recharge = True
          if balance >= Adult_price:
             Adult.adult_passenger_count += 1
          if balance < Adult_price:
             update_balance = input(f"LOW BALANCE:- {balance} \t CARD NUMBER:-'{card_number}'\nAUTO RECHARGE METRO CARD?\n(Y/N):\t")
             if update_balance.lower() == 'y':
                auto_recharge = (Adult_price - balance) 
                interest = (2/100) * auto_recharge
                #auto_recharge += interest
                balance = auto_recharge + balance 
                print(f"\nAUTO-RECHARGE OF {auto_recharge} RUPEESE (2% interest {interest}) INITIATED:\n")
                print("\t\t\t****HAPPY TRAVELLING****\t\n")
                Adult.adult_passenger_count += 1
             else:
                Auto_recharge = False
                print(f"I AM SORRY, YOU ARE NOT ELIGIBLE TO TRAVEL (LOW BALANCE : {balance})")
          else:
               print("\t\t\t****HAPPY TRAVELLING****\t\n")
          return card_number, balance , Type , interest, Auto_recharge
      @classmethod      
      def get_Adult_Count(cls):
          return cls.adult_passenger_count
      
 #Keeps track of the count of overall seniors in the metro and balance requirements of the senior passengers to travel.
 #If the balance is less then the auto recharge function is initiated with the 2 % interest deduction for the auto recharge amount                                    
class Senior(Passengers):
      senior_passenger_count = 0
      def passengers(self, card_number, balance):
          Type = 'SENIOR'
          interest = 0
          Auto_recharge = True
          if balance >= Senior_price:
             Senior.senior_passenger_count += 1
          if balance < Senior_price:
             update_balance = input(f"LOW BALANCE:- {balance} \t CARD NUMBER:-'{card_number}'\nAUTO RECHARGE METRO CARD?\n(Y/N):\t")
             if update_balance.lower() == 'y':
                auto_recharge = (Senior_price - balance) 
                interest = (2/100) * auto_recharge
                #auto_recharge += interest
                balance = auto_recharge + balance 
                print(f"AUTO-RECHARGE OF {auto_recharge} RUPEESE (2% interest {interest}) INITIATED:\n")
                print("\t\t\t****HAPPY TRAVELLING****\n")
                Senior.senior_passenger_count += 1
             else:
                Auto_recharge = False
                print(f"I AM SORRY, YOU ARE NOT ELIGIBLE TO TRAVEL (LOW BALANCE : {balance})")
          else:
               print("\n\t\t\t****HAPPY TRAVELLING****\n")   
          return card_number, balance , Type, interest , Auto_recharge
      @classmethod      
      def get_Senior_Count(cls):
          return cls.senior_passenger_count
      
#Keeps track of the count of overall kids in the metro and balance requirements of the kids passengers to travel.
 #If the balance is less then the auto recharge function is initiated with the 2 % interest deduction for the auto recharge amount   
class Kids(Passengers):
      kid_passenger_count = 0
      def passengers(self, card_number, balance):
          Type = 'KIDS'
          interest = 0
          Auto_recharge = True
          if balance >= Kids_price:
             Kids.kid_passenger_count += 1
          if balance < Kids_price:
             update_balance = input(f"LOW BALANCE:- {balance} \t CARD NUMBER:-'{card_number}'\nAUTO RECHARGE METRO CARD?\n(Y/N):\t")
             if update_balance.lower() == 'y':
                auto_recharge = (Kids_price - balance) 
                interest = (2/100) * auto_recharge
                #auto_recharge += interest
                balance = auto_recharge + balance 
                print(f"AUTO-RECHARGE OF {auto_recharge} RUPEESE (2% interest {interest} deducted) INITIATED:\n")
                print("\t\t\t****HAPPY TRAVELLING****\t\n")
                Kids.kid_passenger_count += 1
             else:
                Auto_recharge = False
                print(f"\nI AM SORRY, YOU ARE NOT ELIGIBLE TO TRAVEL (LOW BALANCE : {balance})")
          else:
               print("\n\t\t\t****HAPPY TRAVELLING****\t\n")
          return card_number, balance , Type, interest, Auto_recharge
      @classmethod      
      def get_Kid_Count(cls):
          return cls.kid_passenger_count
           
     

class Stations(ABC):
      @abstractmethod
      def platform(self, passenger: Passengers, card_number, balance):
          pass
      
#Keeps track of the type of passengers entering the central station
#Also the transaction of the prices from the central station for passsengers  is taken and updated balance is given back
#Keeps track of the passengers eligible for discount for their return journey
class Central_Station(Stations):
      Central_Station_Collection = 0
      Discount_collection = 0.0
      adult_count = 0 
      senior_count = 0
      kid_count =0
      def platform(self, passenger: Passengers, card_number, balance):
          
          platform_name = 'CENTRAL STATION'
          count = 0
          updated_card_number, updated_balance, passenger_type, passenger_interest, rechargre_verify  = passenger.passengers(card_number, balance)
          count_adult = Adult.get_Adult_Count()
          count_senior = Senior.get_Senior_Count()
          count_kid = Kids.get_Kid_Count()
          if  passenger_type.lower() == 'adult' and rechargre_verify == True:
              count = count_adult 
              Central_Station.adult_count += 1
              visited_central.append(card_number)  
              
          if  passenger_type.lower() == 'senior'and rechargre_verify == True:
              count = count_senior   
              Central_Station.senior_count += 1
              visited_central.append(card_number)

          if  passenger_type.lower() == 'kids'and rechargre_verify == True:
              count = count_kid
              Central_Station.kid_count += 1
              visited_central.append(card_number)

          if card_number in visited_airport:
             if  passenger_type.lower() == 'adult' and count != 0 and rechargre_verify == True:
                    Discount_price = Adult_price * Discount_percent
                    Central_Station.Discount_collection += float(Discount_price)
                    updated_balance = updated_balance - Discount_price
                    Central_Station.Central_Station_Collection += Discount_price

             if  passenger_type.lower() == 'senior' and count != 0 and rechargre_verify == True:
                    Discount_price = Senior_price * Discount_percent 
                    Central_Station.Discount_collection += float(Discount_price)
                    updated_balance = updated_balance - Discount_price
                    Central_Station.Central_Station_Collection += Discount_price

             if  passenger_type.lower() == 'kids' and count != 0 and rechargre_verify == True:
                    Discount_price = Kids_price * Discount_percent
                    Central_Station.Discount_collection += float(Discount_price)
                    updated_balance = updated_balance - Discount_price
                    Central_Station.Central_Station_Collection += Discount_price
          else:
               Discount_price = None

          if passenger_type.lower() == 'adult' and Discount_price == None and rechargre_verify == True:
             if count != 0:
                updated_balance =  updated_balance - Adult_price
                Central_Station.Central_Station_Collection += Adult_price
    
          if passenger_type.lower() == 'senior' and Discount_price == None and rechargre_verify == True:
             if count != 0:
                updated_balance =  updated_balance - Senior_price
                Central_Station.Central_Station_Collection += Senior_price

          if passenger_type.lower() == 'kids' and Discount_price == None and rechargre_verify == True:
             if count != 0:
                updated_balance = updated_balance - Kids_price
                Central_Station.Central_Station_Collection += Kids_price
              
          #print(f"\n\tPROCESSING  PASSENGERS AT CENTRAL STATION:\t\n")
          print(f" CARD NUMBER: {updated_card_number} \tPASSENGER TYPE: {passenger_type} \t FROM: {platform_name} \tDISCOUNT_PRICE : {Discount_price}")
          #print(f"PASSENGER INTEREST DEDUCTED: {passenger_interest}\n") 
          print("\n")
          
          Central_Station.Central_Station_Collection += passenger_interest

          if card_number in card_records:
             _, passenger_type = card_records[card_number]
             card_records[card_number] = (updated_balance, passenger_type)

          return ('\t\t*******STATION RECORDS UPDATED*******\t\n')
      
      @classmethod
      def central_station_collection(cls):
          return cls.Central_Station_Collection, cls.Discount_collection
      @classmethod
      def central_station_passenger_collection(cls):
          return cls.senior_count,cls.adult_count,cls.kid_count
    
#same working process as central station followed in  Airport station
class Airport_station(Stations):
      Airport_station_Collection = 0
      Discount_collection = 0.0
      adult_count = 0 
      senior_count = 0
      kid_count =0
      def platform(self, passenger: Passengers, card_number, balance):
          Discount_price = None
          count = 0
          platform_name = 'AIRPORT STATION'
          updated_card_number, updated_balance, passenger_type, passenger_interest, recharge_verify = passenger.passengers(card_number, balance)
          count_adult = Adult.get_Adult_Count()
          count_senior = Senior.get_Senior_Count()
          count_kid = Kids.get_Kid_Count()

          if  passenger_type.lower() == 'adult'and recharge_verify == True:
              count = count_adult
              Airport_station.adult_count += 1
              visited_airport.append(card_number)

          if  passenger_type.lower() == 'senior'and recharge_verify == True:
              count = count_senior  
              Airport_station.senior_count += 1 
              visited_airport.append(card_number)  

          if  passenger_type.lower() == 'kids'and recharge_verify == True:
              count = count_kid
              Airport_station.kid_count += 1
              visited_airport.append(card_number)

          if card_number in visited_central:
             if  passenger_type.lower() == 'adult' and count != 0 and recharge_verify == True:
                    Discount_price = Adult_price * Discount_percent
                    Airport_station.Discount_collection += float(Discount_price)
                    updated_balance = updated_balance - Discount_price
                    Airport_station.Airport_station_Collection += Discount_price

             if  passenger_type.lower() == 'senior' and count != 0 and recharge_verify == True:
                    Discount_price = Senior_price * Discount_percent
                    Airport_station.Discount_collection += float(Discount_price)
                    updated_balance = updated_balance - Discount_price
                    Airport_station.Airport_station_Collection += Discount_price
                 
             if  passenger_type.lower() == 'kids' and count != 0 and recharge_verify == True:
                    Discount_price  = Kids_price * Discount_percent
                    Airport_station.Discount_collection += float(Discount_price)
                    updated_balance = updated_balance - Discount_price
                    Airport_station.Airport_station_Collection += Discount_price
          else:
               Discount_price = None

          if passenger_type.lower() == 'adult' and Discount_price == None and recharge_verify == True:
             if count != 0:
                updated_balance =  updated_balance - Adult_price
                Airport_station.Airport_station_Collection += Adult_price
    
          if passenger_type.lower() == 'senior' and Discount_price == None and recharge_verify == True:
            if count != 0:
                updated_balance =  updated_balance - Senior_price
                Airport_station.Airport_station_Collection += Senior_price

          if passenger_type.lower() == 'kids' and Discount_price == None and recharge_verify == True:
             if count != 0:
                updated_balance = updated_balance - Kids_price
                Airport_station.Airport_station_Collection += Kids_price
              
          #print(f"\n\tPROCESSING  PASSENGERS AT AIRPORT STATION:\t\n")
          print(f" CARD NUMBER: {updated_card_number} \tPASSENGER TYPE: {passenger_type} \t FROM: {platform_name}\t DISCOUNT_PRICE : {Discount_price}")
          #print(f"\n{passenger_type} PASSENGERS:{count}\n")
          print("\n")
          #print(f"PASSENGER INTEREST DEDUCTED: {passenger_interest}")

          
          Airport_station.Airport_station_Collection += passenger_interest

          if card_number in card_records:
             _, passenger_type = card_records[card_number]
             card_records[card_number] = (updated_balance, passenger_type)
          return ('\t\t******STATION RECORDS UPDATED********\t\n')
      
      @classmethod
      def airport_station_collection(cls):
          return cls.Airport_station_Collection,cls.Discount_collection
      
      @classmethod
      def airport_station_passenger_collection(cls):
          return cls.senior_count,cls.adult_count,cls.kid_count


class Metro_Records:
    def process_passengers(self, station, passenger, card_number, balance):
        # Process the passenger with the given card number and balance
        return station.platform(passenger, card_number, balance)

    def process_multiple_passengers(self):
        num_passengers = int(input("How many passengers do you want to process? "))
        for _ in range(num_passengers):
            station_name = input("Enter the station (central/airport): ").lower()
            card_number = input("Enter the card number: ")
            if card_number in card_records:
               balance, passenger_type = card_records[card_number]
            else:
                 passenger_type = input("Enter the passenger type (adult/senior/kid): ").lower()
                 balance = float(input("Enter the balance: "))
                 card_records[card_number] = balance, passenger_type
                 print("\n\n")
            

            # Choose the correct station
            if station_name == "central":
                station = central_station
            elif station_name == "airport":
                station = airport_station
            else:
                print("Invalid station name!\n")
                continue

            # Choose the correct passenger type
            if passenger_type == "adult":
                passenger = adult_passenger
            elif passenger_type == "senior":
                passenger = senior_passenger
            elif passenger_type == "kid":
                passenger = kid_passenger
            else:
                print("Invalid passenger type!\n")
                continue

            # Process the passengers
            print(self.process_passengers(station, passenger, card_number, balance))

    def records(self):

        print(f"\nCOLLECTION FROM:\tCENTRAL STATION: {Central_Station.central_station_collection()}")
        senior_count,adult_count, kid_count = Central_Station.central_station_passenger_collection()
        passenger_counts = [
            ('Adults', adult_count),
            ('Seniors', senior_count),
            ('Kids', kid_count)
        ]
        passenger_counts.sort(key=lambda x: x[1], reverse=True)
        print("\nPASSENGER TYPE COLLECTION:")
        for passenger_type, count in passenger_counts:
            print(f"\t\t\t{passenger_type}: {count}")



        print(f"\nCOLLECTION FROM:\tAIRPORT STATION: {Airport_station.airport_station_collection()}")
        senior_count,adult_count, kid_count = Airport_station.airport_station_passenger_collection()
        passenger_counts = [
            ('Adults', adult_count),
            ('Seniors', senior_count),
            ('Kids', kid_count)
        ]
        # Sort the list by the count in descending order
        passenger_counts.sort(key=lambda x: x[1], reverse=True)
        print("\nPASSENGER TYPE COLLECTION:")
        for passenger_type, count in passenger_counts:
            print(f"\t\t\t{passenger_type}: {count}")


# Create instances of stations and passengers (assuming these classes are defined elsewhere)
central_station = Central_Station()  
airport_station = Airport_station()  
adult_passenger = Adult()            
senior_passenger = Senior()          
kid_passenger = Kids()               
metro_records = Metro_Records()


#calling
if __name__ == '__main__':
   metro_records.process_multiple_passengers()
   print("\n\n\t\t**********METRO_FINAL_REPORT*************\n")
   metro_records.records()
   input()

