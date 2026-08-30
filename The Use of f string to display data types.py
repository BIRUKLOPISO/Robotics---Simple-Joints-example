# Abstract base class (using ABC module)
from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        """Process payment - must be implemented by subclasses"""
        pass

    def generate_receipt(self, amount):
        """Common functionality for all payment methods"""
        return f"Receipt for ${amount:.2f}"


# Concrete implementations
class CreditCardProcessor(PaymentProcessor):
    def __init__(self, card_number, expiry_date):
        self.card_number = card_number[-4:]  # Store only last 4 digits
        self.expiry_date = expiry_date

    def process_payment(self, amount):
        # Simulate credit card processing logic
        print(f"Authorizing credit card ending in {self.card_number}...")
        print(f"Checking expiration: {self.expiry_date}")
        return f"Credit card payment of ${amount:.2f} processed successfully"

    def generate_receipt(self, amount):
        # Override with payment-specific details
        base_receipt = super().generate_receipt(amount)
        return f"{base_receipt}\nPayment method: Credit Card (****{self.card_number})"


class PayPalProcessor(PaymentProcessor):
    def __init__(self, email):
        self.email = email

    def process_payment(self, amount):
        # Simulate PayPal processing logic
        print(f"Redirecting to PayPal for {self.email}...")
        print(f"Verifying PayPal account...")
        return f"PayPal payment of ${amount:.2f} processed successfully"

    def refund_payment(self, amount):
        # PayPal-specific method
        return f"Refund of ${amount:.2f} initiated via PayPal"


class CryptoProcessor(PaymentProcessor):
    def __init__(self, wallet_address):
        self.wallet_address = wallet_address

    def process_payment(self, amount):
        # Simulate crypto processing
        print(f"Confirming transaction on blockchain...")
        print(f"Wallet: {self.wallet_address[:8]}...{self.wallet_address[-6:]}")
        return f"Crypto payment of ${amount:.2f} (0.001 BTC) processed"

    def get_transaction_hash(self):
        # Crypto-specific method
        import uuid
        return f"txn_{uuid.uuid4().hex[:16]}"


# Shopping cart that uses polymorphism
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price):
        self.items.append((name, price))

    def checkout(self, payment_processor):
        """Polymorphic method - works with ANY PaymentProcessor"""
        total = sum(price for _, price in self.items)

        print("\n" + "=" * 50)
        print("CHECKOUT SUMMARY")
        print("=" * 50)

        # Process payment (polymorphic call)
        result = payment_processor.process_payment(total)
        print(f"\nPayment Result: {result}")

        # Generate receipt (also polymorphic)
        receipt = payment_processor.generate_receipt(total)
        print(f"\n{receipt}")

        # Show items
        print(f"\nItems purchased:")
        for name, price in self.items:
            print(f"  - {name}: ${price:.2f}")

        print(f"\nTotal: ${total:.2f}")
        return result


# Using the system
def main():
    # Create shopping cart
    cart = ShoppingCart()
    cart.add_item("Python Book", 29.99)
    cart.add_item("USB Cable", 12.50)
    cart.add_item("Coffee Mug", 15.75)

    # Different payment processors
    credit_card = CreditCardProcessor("4111111111111111", "12/25")
    paypal = PayPalProcessor("user@example.com")
    crypto = CryptoProcessor("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa")

    # POLYMORPHISM IN ACTION
    # Same checkout method works with different payment processors

    print("=== CREDIT CARD CHECKOUT ===")
    cart.checkout(credit_card)

    print("\n\n=== PAYPAL CHECKOUT ===")
    cart.checkout(paypal)

    print("\n\n=== CRYPTO CHECKOUT ===")
    cart.checkout(crypto)

    # Demonstrate payment-specific methods
    print("\n" + "=" * 50)
    print("PAYMENT-SPECIFIC FEATURES")
    print("=" * 50)
    print(paypal.refund_payment(29.99))  # PayPal-specific
    print(f"Crypto Transaction: {crypto.get_transaction_hash()}")  # Crypto-specific


if __name__ == "__main__":
    main()