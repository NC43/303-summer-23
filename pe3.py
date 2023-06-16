def encode(input_text, shift):
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    encoded_text = ""

    for char in input_text:
        if char.isalpha():
            index = alphabet.index(char.lower())
            shifted_index = (index + shift) % 26
            encoded_char = alphabet[shifted_index]
            encoded_text += encoded_char if char.islower() else encoded_char.upper()
        else:
            encoded_text += char

    return alphabet, encoded_text

print(encode("a", 3))
# Output: (['a', 'b', ..., 'z'], 'd')

print(encode(" abc", 4))
# Output: (['a', 'b', ..., 'z'], 'efg')

print(encode(" xyz", 3))
# Output: (['a', 'b', ..., 'z'], 'abc')

print(encode("j!K,2?", 3))
# Output: (['a', 'b', ..., 'z'], 'm!n,2?')


def decode(input_text, shift):
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    decoded_text = ""

    for char in input_text:
        if char.isalpha():
            index = alphabet.index(char.lower())
            shifted_index = (index - shift) % 26
            decoded_char = alphabet[shifted_index]
            decoded_text += decoded_char if char.islower() else decoded_char.upper()
        else:
            decoded_text += char

    return decoded_text

print(decode("d", 3))
# Output: 'a'

print(decode(" efg", 4))
# Output: ' abc'

print(decode(" abc", 3))
# Output: 'xyz'

print(decode("m!n,2?", 3))
# Output: 'j!K,2?'


from datetime import date, timedelta


class BankAccount:
    def __init__(self, name="Clocks", ID="123", creation_date=date.today(), balance=0):
        if creation_date > date.today():
            raise Exception("Invalid creation date")

        self.name = name
        self.ID = ID
        self.creation_date = creation_date
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def view_balance(self):
        return self.balance


class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if (date.today() - self.creation_date) < timedelta(days=180):
            raise Exception("Withdrawals not allowed before 6 months")

        if amount > self.balance:
            raise Exception("Insufficient funds")

        self.balance -= amount


class CheckingAccount(BankAccount):
    def withdraw(self, amount):
        if amount > self.balance:
            self.balance -= (amount + 30)  # Deducting withdrawal amount and penalty fee
        else:
            self.balance -= amount

# Creating BankAccount instance
account = BankAccount("Alice", "456", date(2022, 1, 1), 1000)

# Depositing and withdrawing from the account
account.deposit(500)
account.withdraw(200)

# Viewing the balance
print(account.view_balance())  # Output: 1300

# Creating SavingsAccount instance
savings_account = SavingsAccount("Bob", "789", date(2023, 1, 1), 2000)

# Trying to withdraw before 6 months (raises exception)
savings_account.withdraw(500)  # Raises Exception: Withdrawals not allowed before 6 months

# Creating CheckingAccount instance
checking_account = CheckingAccount("Charlie", "999", date(2022, 1, 1), 500)


