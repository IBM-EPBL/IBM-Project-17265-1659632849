from flask import Flask
from flask_mail import Mail, Message

message = Mail(
                from_email='dhanushgoku997@gmail.com',
                to_emails=email,
                subject='extrack',
                html_content='<h1>Thank you for registering with ExTrack,you can now login and use the application</h1>'
                )
            try:
                    sg = SendGridAPIClient("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")
                    response = sg.send(message=message)
                    print(response.status_code)
                    print(response.body)
                    print(response.headers)
            except Exception as e:
                    print(e)
        