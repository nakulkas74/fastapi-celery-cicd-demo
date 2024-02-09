from send_mail import SendMail

sender_email = 'nakulchamariya373@gmail.com'
sender_password = 'gnhcjjvsjznxvodv'

def email_link(receiver_email_list, email_title, email_descp):
    new_mail = SendMail(receiver_email_list, email_title, email_descp, sender_email)
    new_mail.send(sender_password)