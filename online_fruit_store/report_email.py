!/usr/bin/env python3

import os
import datetime
import reports
import emails

feedbackDir = "supplier-data/descriptions/"

def generate_pdf():
    total_string = ""
    feedbackFiles = os.listdir(feedbackDir)
    for txtfile in feedbackFiles:
        fb = open(feedbackDir+txtfile)
        data = fb.read().split("\n")
        dict = {"name":data[0], "weight":int(data[1].split(" ")[0]), "description":data[2], "image_name":txtfile.split(".")[0]+".jpeg"}
        name = 'name: ' + dict['name'] + '<br/>' # i have to make empty here, so i am using <br> as \n works in python only.
        #print(name)
        total_string += name
        weight = 'weight: ' + str(dict['weight'])+ ' lbs' + '<br/>' + '<br/>' #here i have 2 newlines because of task says so
        total_string += weight
    return total_string

if __name__ == "__main__":
    #making pdf report:
    attachment = 'supplier-data/processed.pdf'
    today = datetime.datetime.now().date()
    title = "Processed Update on {}.".format(today.strftime("%B %d, %Y"))
    paragraph = generate_pdf()
    reports.generate_report(attachment, title, paragraph)

    #constructing an email:
    sender = 'automation@example.com'
    recipient = 'student-04-db78ef0449e5@example.com'
    subject = 'Upload Completed - Online Fruit Store'
    body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'
    attachment_path = 'supplier-data/processed.pdf'
    complete_email = emails.generate(sender, recipient, subject, body, attachment_path)

    #sending an email with .pdf
    emails.send(complete_email)
