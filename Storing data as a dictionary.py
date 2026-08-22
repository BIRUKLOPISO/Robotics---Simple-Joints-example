class Payment:
    def __init__(self, amount, currency="USD"):
        self.amount = amount
        self.currency = currency
        self.fee = 0
        self.tax = 0

    def calculate_fee(self):
        """Base fee calculation: 2% of amount"""
        self.fee = self.amount * 0.02
        return self.fee

    def calculate_tax(self):
        """Base tax calculation: 10% of amount"""
        self.tax = self.amount * 0.10
        return self.tax

    def process_payment(self):
        """Main payment processing logic"""
        print(f"\n=== Processing {self.currency} {self.amount:.2f} ===")

        # Calculate fee and tax
        fee = self.calculate_fee()
        tax = self.calculate_tax()

        # Calculate total
        total = self.amount + fee + tax

        # Display breakdown
        print(f"Amount:     {self.currency} {self.amount:10.2f}")
        print(f"Fee ({self.get_fee_percentage():.1f}%):  {self.currency} {fee:10.2f}")
        print(f"Tax ({self.get_tax_percentage():.1f}%):  {self.currency} {tax:10.2f}")
        print(f"Total:      {self.currency} {total:10.2f}")

        return total

    def get_fee_percentage(self):
        return 2.0

    def get_tax_percentage(self):
        return 10.0


class CreditCardPayment(Payment):
    def __init__(self, amount, currency, card_type):
        super().__init__(amount, currency)
        self.card_type = card_type
        self.cashback = 0

    def calculate_fee(self):
        """Credit cards have higher fees: 3% + $0.30"""
        # First get base fee from parent
        base_fee = super().calculate_fee()
        # Add credit card specific fee
        additional_fee = 0.30
        self.fee = base_fee + additional_fee
        return self.fee

    def calculate_cashback(self):
        """Credit card specific: 1% cashback"""
        self.cashback = self.amount * 0.01
        return self.cashback

    def process_payment(self):
        """Extend payment processing with cashback"""
        # First, let parent do the main processing
        total = super().process_payment()

        # Then add credit card specific features
        cashback = self.calculate_cashback()
        print(f"Cashback (1%):  -{self.currency} {cashback:9.2f}")
        print(f"Final Amount:   {self.currency} {total - cashback:10.2f}")
        print(f"Paid with: {self.card_type} Credit Card")

        return total - cashback

    def get_fee_percentage(self):
        """Override to show correct percentage"""
        return 3.0  # Higher for credit cards


class InternationalPayment(Payment):
    def __init__(self, amount, currency, exchange_rate):
        super().__init__(amount, currency)
        self.exchange_rate = exchange_rate
        self.conversion_fee = 0

    def calculate_fee(self):
        """International payments have conversion fees"""
        # Get base fee
        base_fee = super().calculate_fee()
        # Add conversion fee: 1.5%
        self.conversion_fee = self.amount * 0.015
        self.fee = base_fee + self.conversion_fee
        return self.fee

    def calculate_tax(self):
        """International might have different tax rules"""
        # Convert amount to local currency first
        local_amount = self.amount * self.exchange_rate

        # Calculate tax in local currency
        local_tax = local_amount * 0.08  # Lower tax rate internationally

        # Convert back to payment currency
        self.tax = local_tax / self.exchange_rate
        return self.tax

    def process_payment(self):
        """Show conversion details"""
        print(f"\n=== International Payment ===")
        print(f"Original: {self.currency} {self.amount:.2f}")
        print(f"Exchange Rate: 1 {self.currency} = {self.exchange_rate:.2f} EUR")

        # Call parent processing
        total = super().process_payment()

        # Show converted amount
        euro_total = total * self.exchange_rate
        print(f"Total in EUR: €{euro_total:.2f}")

        return total

    def get_tax_percentage(self):
        return 8.0  # Lower international tax


# Let's test our payment system
print("=== PAYMENT PROCESSING SYSTEM ===")

# Regular payment
print("\n1. Regular Payment:")
regular = Payment(100.00)
regular.process_payment()

# Credit card payment
print("\n2. Credit Card Payment:")
credit = CreditCardPayment(100.00, "USD", "Visa")
credit.process_payment()

# International payment
print("\n3. International Payment:")
international = InternationalPayment(100.00, "USD", 0.85)
international.process_payment()


