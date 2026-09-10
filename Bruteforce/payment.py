class Payment :
    def process_payment(self , payment_type, amount):
        if payment_type == "credit_card":
            print(f"Processing {amount} using Credit Card")
        elif payment_type == "upi":
            print(f"Processing {amount} using UPI")
        elif payment_type == "cash":
            print(f"Processing {amount} using Cash")

    def validate_payment(self,payment_type, amount):
        if amount <= 0 :
            print("Invalid amount")
            return False
        if payment_type == "credit_card":
            print("Credit card payment validated")
        elif payment_type == "upi":
            print("Upi payment validated")
        elif payment_type == "cash":
            print("Cash payment validated")
        else :
            print("Invalid payment type")
    

    def refund_payment(self, payment_type, amount):

        if payment_type == "credit_card":
            print(f"{amount} refunded successfully")
        elif payment_type == "upi":
            print(f"{amount} refunded successfully")
        elif payment_type == "cash":
            print(f"{amount} refunded successfully")

        else:
            print("Invalid payment type")


payment = Payment()
payment.validate_payment("credit_card", 1000)
payment.process_payment("credit_card", 1000)
payment.refund_payment("credit_card", 1000)
