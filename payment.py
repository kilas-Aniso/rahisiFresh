class Payment:
    def __init__(self, payment_methods):
        self.payment_methods = payment_methods
    def select_payment_method(self, method):
        # Check if the selected payment method is available
        if method in self.payment_methods:
            print(f"Selected payment method: {method}")
        else:
            print(f"{method} is not available. Please choose a different payment method.")
    def cancel_payment(self):
        # Cancel the payment transaction
        print("Payment transaction cancelled.")