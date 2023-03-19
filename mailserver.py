import smtpd
import asyncore

class TestMailServer(smtpd.SMTPServer):
    def process_message(self, peer, mailfrom, rcpttos, data):
        print(f"Received message from {mailfrom}")
        print(f"To: {rcpttos}")
        print(f"Message: {data}")

mail_server = TestMailServer(('localhost', 1025), None)
asyncore.loop()
