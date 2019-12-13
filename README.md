#Appointment_scheduling

About :
Python job scheduling for humans.
Online bookings/appointments/calendars in Python
An in-process scheduler for periodic jobs that uses the builder pattern for configuration. 
Features:
 Easy appointment creation for various Service Provider
Easy date picker, time picker and auto time suggestion while creating new appointment
Success notification
Booking Record saving in the csv File.
Different Slot suggestion while  date is already booked.
Its Checking the entered Date is Weekend or not.
Its give us the distance between two city that user have entered and the estimated time that will take to reach.
 
Requirements :
geopy==1.20.0
python
openrouteservice==2.2.3
pandas

Procedure:
At first we import our all library of python that we are going to  use through out our program
 Read our csv file.
After that we will write a function that will handle all the main work of the project
And we are taking the details from user (category, dates)
Now we are asking for choosing the slot , we will take the input and show them our slotting option, we already defined our slot 
 
Taking the date and time : After choosing the slotting option,we are taking the slot and marge the date and time together according to the user input and save as date and time.

Checking weekday or weekend: Here we are checking the date where it is weekend or not by simply using date.weekday()<5 if it returns true that it is week day if not that its basically a weekend. We use this logic to our program to find the weekdays .

Booking status checking: The main work is checking the slot is already booked or not for this problem we apply the logic that is we are fetching the data from our dataset that is basically the record of booking. At First we checking the category with the user input then it will check all the category and their respective date and time section. If it found that for this category, the date and time what user has given is already exists in our record than it will simply return that service provider is not available at that time and if can not find any date and time in our csv as same as user entered it will save his record and give the customer a notification that his/her appointment is booked .

Calculating the distance and time: After that now we will take Two location to basically calculate the Distance and estimated time with a third party api that is openrouteservice api. To calculate the distance and the estimated time, at first we have to find the latitude and longitude of the specific address
We find the address with a popular python library Geopy (geopy makes it easy for Python developers to locate the coordinates of addresses, cities, countries,   ) now with a tool of geopy named Nominatim  we find the latitude and longitude  and call our third party API Openrouteservice api we call our api with a personal api token and pass the calculated coordinates to our API and after that it gives us a dictionary,from that We are fetching our required data like distance and time.  we used this logic to our program in order to find the estimated time and the Distance between two places.
Suggesting slot: In the case of Not available service provider ,we are returning the other slot option to the customer what he has not enter in the time of booking.
We are able to do this with if else condition.we check what option user entered while booking and match with our left options and return the suggestion of another slots.
 
And the very important thing it does, to save our all records of bookings . its working like a database, from where we can get all the records.
 
Full source Code : 
 
 
 
                                                                              A document is created by :
                                                                                                              Ankush Banik
 
 
 
 
 
 
 
 
