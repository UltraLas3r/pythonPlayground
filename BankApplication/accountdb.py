import sqlite3

# define connection and cursor
connection = sqlite3.connect('my_bank_accounts.db')
cursor = connection.cursor()

# create tables
CREATE_ACCOUNTS_TABLE = """CREATE TABLE IF NOT EXISTS
                            Accounts(user_id INTEGER PRIMARY KEY, 
                            user_fname TEXT, 
                            user_lname TEXT)"""

CREATE_USER_ACCOUNT_BALANCE_TABLE = """CREATE TABLE IF NOT EXISTS
                            UserAccountBalance(user_id INTEGER, 
                            user_fullname TEXT, 
                            account_balance FLOAT,
                            FOREIGN KEY (user_id) REFERENCES accounts(user_id))"""

# user 1id, 2first name, 3last name, 4opening deposit
CREATE_NEW_ACCOUNT = """INSERT INTO accounts (?, ?, ?, ?)"""

INSERT_DEPOSIT_INTO_USER_ACCOUNT = "INSERT INTO UserAccountBalance (user_id, account_balance) VALUES (?, ?)"

WITHDRAW_FROM_USER_ACCOUNT = """SELECT * FROM UserAccountBalance (account_balance)"""

GET_ACCOUNT_BALANCE = """SELECT * FROM UserAccountBalance WHERE user_id = ?"""

GET_ACCOUNT_INFO = "SELECT * FROM Accounts"

createAccountsTable = cursor.execute(CREATE_ACCOUNTS_TABLE)
createBalanceTable = cursor.execute(CREATE_USER_ACCOUNT_BALANCE_TABLE)
accountInfo = cursor.execute(GET_ACCOUNT_INFO)

# add rows to accounts table
# cursor.execute("INSERT INTO Accounts VALUES (13314, 'John', 'Adams')")
# cursor.execute("INSERT INTO Accounts VALUES (44355, 'Archie', 'Smith')")
# cursor.execute("INSERT INTO Accounts VALUES (65123, 'Brock', 'Lesnar')")

# add rows to BalanceInfo table
# cursor.execute("INSERT INTO BalanceInfo VALUES (13314, 'placeholder1', 15155.34)")
# cursor.execute("INSERT INTO BalanceInfo VALUES (44355, 'placeholder2', 335.65)")
# cursor.execute("INSERT INTO BalanceInfo VALUES (65123, 'placeholder3', 335.65)")

# get results

# balanceInfo = cursor.execute(GET_ACCOUNT_BALANCE, "13314")


def connect():
    return sqlite3.connect("my_bank_data.db")


def create_tables(connection):
    with connection:
        connection.execute(CREATE_ACCOUNTS_TABLE)
        connection.execute(CREATE_USER_ACCOUNT_BALANCE_TABLE)


def create_user_account():
    pass


def get_info(info_type):
    if info_type == 'account':
        print(accountInfo.fetchall(), " <---- account info")
    if info_type == 'balance':
        print(balanceInfo.fetchall(), " <---- balance info")


def make_user_account_deposit(user_id, deposit_amount):
    connection.execute(INSERT_DEPOSIT_INTO_USER_ACCOUNT, (user_id, deposit_amount))


def make_user_account_withdrawal(withdrawal_amount):
    user_account_sum = connection.execute(WITHDRAW_FROM_USER_ACCOUNT)

