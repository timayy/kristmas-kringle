

import os
import random
import sys
from dataclasses import dataclass
from timeit import default_timer as timer
from typing import List, Tuple

from emailer.email_service import EmailService, MockEmailService
from emailer.gmail_service import GmailService

@dataclass
class Person:
    name: str
    excludes: str
    email_address: str
    buying_for: 'Person'


artem = Person(name="Artem", excludes="Tylah", email_address="fakeemail.com", buying_for=None)
tylah = Person(name="Tylah", excludes="Artem", email_address="fakeemail.com", buying_for=None)
ryan = Person(name="Ryan", excludes="Ellissa", email_address="fakeemail.com", buying_for=None)
ellissa = Person(name="Ellissa", excludes="Ryan", email_address="fakeemail.com", buying_for=None)
patrick = Person(name="Patrick", excludes="Gemma", email_address="fakeemail.com", buying_for=None)
gemma = Person(name="Gemma", excludes="Patrick", email_address="fakeemail.com", buying_for=None)


people = [
    artem, tylah,
    ryan, ellissa,
    patrick, gemma
]


def select_kks(people: List[Person]) -> Tuple[List[Person], int]:
    
    total_attempts = 0
    current_attempts = 0
    recipients = []

    while len(recipients) != len(people):
        current_attempts +=1
        total_attempts += 1

        person_one = random.choice(people)
        person_two = random.choice(people)

        # Reset if choice can't be resolved.
        if (current_attempts > 100):
            reset_people(people)
            recipients = []
            current_attempts = 0

        # Can't buy for yourself.
        if person_one.name == person_two.name:
            continue

        # Can't buy for your partner.
        if person_one.excludes == person_two.name:
            continue

        # Can't buy for more than one person.
        if person_one.buying_for is not None:
            continue

        # Can't get more than one gift!
        if person_two in recipients:
            continue

        person_one.buying_for = person_two
        recipients.append(person_two)
                
    return people, total_attempts


def reset_people(people: List[Person]):
    for person in people:
        person.buying_for = None


def get_people_results(people: List[Person]) -> str:
    return "\n".join([f"{person.name} is buying for: {person.buying_for.name}" for person in people])


def send_emails_to_people(email_service: EmailService, people: List[Person], execution_time, total_attempts):
    for person in people:
        email_service.send_email(
            person.email_address, 
            "Friendmas - Your KK is... 👀", 
            (
            f"Hey {person.name}!"
            f"\n"
            f"\nFriendmas is upon us, which means its time for Kris Kringle 🎉🎄"
            f"\nLet's get together, and share some gifts that Twinkle!"
            f"\n"
            f"\nThe budget sits at $30 bucks - but a tiny bit of leeway is fine."
            f"\nNow get ready, and read below, for your special assign -"
            f"\n"
            f"\nBecause this year, you're buying for the wonderful..."
            f"\n"
            f"\n🎅🎅 {person.buying_for.name} 🎅🎅"
            f"\n"
            f"\nGood luck! I know you'll sleigh it ;)"
            f"\n"
            f"\n---"
            f"\n"
            f"\nFun bot facts:"
            f"\nRunning this code took: {execution_time} seconds."
            f"\nMade {total_attempts} attempts to find your perfect match."
            f"\nThis was coded on a kitchen counter, and partly on a family couch."
            )
        )


def main():

    # Get env vars.
    email_username = os.getenv("EMAIL_USERNAME")
    email_password = os.getenv("EMAIL_PASSWORD")

    # Run mode - test or normal.
    run_mode = "Test"
    email_service = MockEmailService(email_username, email_password)
    if len(sys.argv) < 2 or sys.argv[1].lower() != "-t":
        run_mode = "Normal"
        email_service = GmailService(email_username, email_password)
        pass

    print(f"Running in: {run_mode} mode.")

    # Run kk selection.
    start = timer()
    final_people, total_attempts = select_kks(people)
    end = timer()

    execution_time = end - start

    # Confirm results with opperator before sending.
    print(get_people_results(final_people))
    print(f"\nMade {total_attempts} attempts to find your perfect match.\n")

    continue_input = input("Type 'y' to continue, or 'n' to stop: ")

    if continue_input != "y":
        raise ValueError("Exited because of input; cheers champion.")

    # Send emails.
    send_emails_to_people(email_service, final_people, execution_time, total_attempts)

    email_service.close_email_server()
    

if __name__ == "__main__":
    main()
