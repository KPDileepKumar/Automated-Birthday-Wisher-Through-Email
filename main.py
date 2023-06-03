##################### Extra Hard Starting Project ######################
import pandas as pd
import datetime as dt
import random
import smtplib


# 4. Send the letter generated in step 3 to that person's email address.
def mail(address, letter):
    my_email = "dilipecnad@gmail.com"
    password = "mwxaslhsxpodcntz"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=address,
                            msg=f"Subject:Letter From Dilip\n\n {letter}")


# 2. Check if today matches a birthday in the birthdays.csv
birthday_file = pd.read_csv("birthdays.csv")
birthday_dict = birthday_file.to_dict(orient="records")
today = dt.datetime.now()
today_month = today.month
today_day = today.day

for person in birthday_dict:
    if today_month == person["month"] and today_day == person["day"]:
        random_nu = random.randint(1, 3)
        with open(f"letter_templates/letter_{random_nu}.txt") as random_template:
            random_letter = random_template.read()
            replaced_letter = random_letter.replace("[NAME]", person["name"])
            mail(person["email"], replaced_letter)

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv


