import sqlite3


class AccessDB:
    # define connection and cursor
    connection = sqlite3.connect('my_bank_accounts.db')
    cursor = connection.cursor()

    # create tables
    command1 = """CREATE TABLE IF NOT EXISTS
    Accounts(user_id INTEGER PRIMARY KEY, user_fname TEXT, user_lname TEXT)"""
    cursor.execute(command1)

    command2 = """CREATE TABLE IF NOT EXISTS
    BalanceInfo(user_id INTEGER, user_fullname TEXT, account_balance FLOAT,
    FOREIGN KEY (user_id) REFERENCES accounts(user_id))"""
    cursor.execute(command2)

    # add rows to accounts table
    cursor.execute("INSERT INTO Accounts VALUES (13314, 'John', 'Adams')")
    cursor.execute("INSERT INTO Accounts VALUES (44355, 'Archie', 'Smith')")
    cursor.execute("INSERT INTO Accounts VALUES (65123, 'Brock', 'Lesnar')")

    # add rows to BalanceInfo table
    cursor.execute("INSERT INTO BalanceInfo VALUES (13314, 'placeholder1', 15155.34)")
    cursor.execute("INSERT INTO BalanceInfo VALUES (44355, 'placeholder2', 335.65)")
    cursor.execute("INSERT INTO BalanceInfo VALUES (65123, 'placeholder3', 335.65)")

    # get results
    accountInfo = cursor.execute("SELECT * FROM Accounts")
    balanceInfo = cursor.execute("SELECT * FROM BalanceInfo")

    def get_info(self, info_type):
        if info_type == 'account':
            print(self.accountInfo.fetchall(), " <---- account info")
        if info_type == 'balance':
            print(self.balanceInfo.fetchall(), " <---- balance info")
