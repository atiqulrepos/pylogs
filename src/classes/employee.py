from src.utils import log


class Employee:
    def __init__(self, fname=None, lname=None):
        self.fname = fname
        self.lname = lname

    def email(self):
        return f"{self.fname}.{self.lname}@email.com"

    def print_email(self):
        email = self.email()
        log().critical(email)
        log().error(email)
        log().warning(email)
        log().info(email)
        log().debug(email)
