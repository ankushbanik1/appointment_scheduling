import smtplib
import time
import pandas as pd
df = pd.read_csv("data.csv")
df1 = pd.read_csv("customardata.csv")


def appointment():
    k = 0
    df = pd.read_csv("data.csv")
    df1 = pd.read_csv("customardata.csv")
    name = input("Name?")
    yourid = input("your ID ?")
    your_prof = input("which  profession service provider you want ?")
    servicename = input("service provider name ?")
    email = input("your email ?")
    starttime = input("enter starting date-time")
    endtime = input("enter end date-time")
    location = input("enter your location")
    b = pd.DataFrame(
        [[yourid, name, starttime, endtime, location, your_prof, servicename, email]])

   
    b.columns = df1.columns
    df1 = df1.append(b)
    df1.to_csv("customardata.csv", index=False)
    print("Successfully Added New Entry.")
    for j in range(len(df["name"])):

        if df["name"][j]==servicename and your_prof==df["profession"][j] and ((df["bookingStartTimeperiod"][j]< starttime and df["bookingEndTimeperiod"][j]>=starttime)or(df["bookingStartTimeperiod"][j]<endtime and df["bookingEndTimeperiod"][j]>=endtime)):

            k=1
            break        
    if(k==0):
        print("Available..your solt  booking is in progresss....")
        b=pd.DataFrame([[(df["ID"][len(df)-1])+1,servicename,your_prof,location,starttime,endtime,yourid]])
        b.columns=df.columns
        df=df.append(b)
        df.to_csv("data.csv",index=False)
        time.sleep(2)
        gmailaddress ="ankushbanik1234@gmail.com"
        gmailpassword = "9091203984"
        mailto1 = email

        msg = "Congrats,"+name+"\n your slot is booked."
        try:
            mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
            # ...send emails
            mailServer.starttls()
            mailServer.login(gmailaddress , gmailpassword)
            mailServer.sendmail(gmailaddress, mailto1 , msg)
            print(msg)
            print("\n check your mail")
            mailServer.quit()
        except:
           print(msg)
           time.sleep(1)
           print("Thank You so much, See you again")
       
    else:
        msg1="Sorry!! "+name+" service provider is not avaiable "

        print(msg1)

if __name__ == "__main__":
    appointment()
