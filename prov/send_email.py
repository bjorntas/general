import smtplib as email
import ssl

def notify(area):

    Message = """
    Subject: Ledig tid

    Ledig tid: https://fp.trafikverket.se/boka/#/
    Ort: {0}
    """
    from_adress = 'cavumseptum@gmail.com'
    password = 'CAVUMSEPTUM1'

    context = ssl.create_default_context()

    server = email.SMTP_SSL('smtp.gmail.com', 465, context=context)
    server.login(from_adress, password)
    server.sendmail(
        from_adress,
        'bjsa@kth.se',
        Message.format(area)
    )

    server.quit()

notify('Ort2')
