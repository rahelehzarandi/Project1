import mysql.connector
import math





connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_1',
         user='root',
         password='rahelehz',
         autocommit=True
         )
budget1 = 200
gift = 6
large_airport_counter=0
airportChosen_list = []
airportCorrect_list = ['?lesund Airport, Vigra','Andya Airport, Andenes','Trondheim Airport, V?rnes',
                       'roms? Airport, Langnes ','Turku Airport','Sodankyla Airport','Helsinki Vantaa Airport',
                       'Kuusamo Airport','Bleck?sen Airstirp','V?ster Private Airstrip','Gothenburg-Landvetter Airport'
                       ,'Stockholm Skavsta Airport','Batuna Aerodrome','Viru Harbour Airstrip','Egilssta?ir Airport',
                       'Reykjavik Airport','Vesthimmerlands Flyveplads','Stauning Airport','Aalborg airport',
                       'Copenhagen Kastrup airport']
countryCorrect_list =['Finland','Norway','Sweden','Iceland','Denmark']
player_name=input("** WELLCOM  SANTA CLAUSE ** enter your name :")
print(f"HI ' {player_name} ', YOU WILL WIN IF PATH 4 LARGE AIRPORT FROM DIFFRENT COUNTRY . YOUR BUDGET IS 200 ")
print('Your Current Location is in unknown airport in Finland')
distance1="SELECT  latitude_deg,longitude_deg FROM scandinavia where " \
      "airport_name='Sodankyla Airport'"
#print(distance1)
cursor = connection.cursor()
cursor.execute(distance1)
result = cursor.fetchall()
if cursor.rowcount > 0:
    for row in result:
        x=row[0]
        y=row[1]

i=0
while budget1 > 0 and gift > 0 :
        i=i+1
        print('Choose one of the these destination COUNTRY: Finland,Norway,Sweden,Iceland,Denmark')
        country_input = input("COUNTRY NAME : ")
        if country_input not in countryCorrect_list:
            print("YOU INPUT INCORRECT COUNTRY .... PLEASE ENTER CORRECT COUNTRY ")
            if i == 10 :
                print("!!!!!!!!!!! ACCESS DENIED!!!!!!!!!!!!")
                exit()

        else:


            print("YOUR CHOSEN COUNTRY IS :", country_input)

            sql = "SELECT airport_name FROM scandinavia where " \
                  "country='" + country_input + "'"
            #print(sql)
            cursor = connection.cursor()
            cursor.execute(sql)
            result = cursor.fetchall()
            if cursor.rowcount > 0:
                for row in result:
                    print(row)

            print("PLEASE CHOOSE FROM THOSE AIRPORT")
            input_airport = input("write your chosen airport name : ")

            if input_airport not in airportCorrect_list:
                print("YOU INPUT INCORRECT AIRPORT .... PLEASE ENTER CORRECT AIRPORT ")
                input_airport = input("write your chosen airport name : ")
            else:

                if input_airport in airportChosen_list:
                    print("!!You have already selected this airport!!")

                else:
                    airportChosen_list.append(input_airport)
                    print(airportChosen_list)

                    distance2 = "SELECT latitude_deg,longitude_deg,type  FROM scandinavia where " \
                                "airport_name ='" + input_airport + "'"
                    #print(distance2)
                    cursor = connection.cursor()
                    cursor.execute(distance2)
                    result = cursor.fetchall()
                    if cursor.rowcount > 0:
                        for row in result:
                            x1 = row[0]
                            y1 = row[1]
                            air_type = row[2]
                            air_type = str(air_type)
                            if air_type == "large_airport"  :
                                budget1=budget1 + 5
                                large_airport_counter = large_airport_counter + 1
                                #print(f"//// YOU HAVE AIMED {large_airport_counter}  TARGET FROM 4 GOAL UNTIL NOW ////")
                            # else:
                            #     print("YOU CAN NOT ACHIVE TARGET")


                            if air_type == "medium_airport":
                                budget1 = budget1 + 2

                    dis = math.sqrt((x - x1) ** 2 + (y - y1) ** 2)
                    #print("YOUR DISTANCE IS:",dis)
                    use_budget = dis*2
                    budget1 = budget1 - use_budget
                    gift = gift - 1

                    print(f"YOUR LEFT GIFT IS :{gift}")
                    print(f"//// YOU HAVE AIMED {large_airport_counter}  TARGET FROM 4 GOAL UNTIL NOW ////")
                    print("YOUR CONSUNED BUDGET IS :", use_budget)

                    print("YOUR LEFT BUDGET IS :",budget1)
                    if large_airport_counter == 4:
                         print('****************YOU WIN ****************')
                         exit()


                x=x1
                y=y1


print("!!!!!!!!!   Game Over  !!!!!!!!! (Your Budget Is Finish or Your Gift Is Finish ) !!!!!!!!!")
exit()



