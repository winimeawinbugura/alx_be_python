#!/usr/bin/env python3
"""
BankAccount class implementation
"""

class BankAccount:
    def __init__(self, initial_balance: float = 0.0):
        """
        Initialize the bank account with an optional initial balance.
        """
        self.__account_balance = initial_balance

    def deposit(self, amount: float) -> None:
        """
        Add money to the account balance.
        """
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount: float) -> bool:
        """
        Withdraw money from the account if sufficient funds exist.
        Returns True if successful, otherwise False.
        """
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self) -> None:
        """
        Print the current account balance.
        """
        print(f"Current Balance: ${self.__account_balance}")
