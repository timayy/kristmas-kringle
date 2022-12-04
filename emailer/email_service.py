
class EmailService:
    def __init__(self, username: str, password: str) -> None:
        """"""

    def send_email(self, recipient: str, subject: str, body: str):
        """"""

    def close_email_server(self):
        """"""

class MockEmailService(EmailService):
    def __init__(self, username: str, password: str) -> None:
        pass

    def send_email(self, recipient: str, subject: str, body: str):
        
        print(f"Would have sent email to: {recipient}.")
        print(f"-- with subject: {subject}.")
        print(f"-- with body: \n{body}.")

    def close_email_server(self):
        pass