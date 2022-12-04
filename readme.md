# kristmas-kringle

A silly Kris Kringle program that selects KK pairs, with restrictions (i.e. for partners), and sends an email to all participants.

This is the least optimal way to ever make this selection, but it was made on a kitchen countertop at 11pm so, eh 🤷‍♂️.

## How to?

1. Set the environement variables - `EMAIL_USERNAME` and `EMAIL_PASSWORD`.
2. In `main.py` configure the `people` list with `Person` objects as needed.
3. In `main.py` configure the `send_emails_to_people` message as needed.
4. Run `python .\kristmas-kringle\main.py -t` - the test flag (`-t`) will help you ensure everything is working correctly.
5. Run `python .\kristmas-kringle\main.py` when you're ready! If you're a participant, get someone else to do this part ;).
6. Once the `Type 'y' to continue, or 'n' to stop:` prompt appears; review the selection, and press `y` if you're happy.
7. Enjoy KK'ing!
