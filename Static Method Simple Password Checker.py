class PasswordManager:
    @staticmethod
    def validate_length(password, min_length):
        if len(password) >= min_length:
            return "+1 point for minimum 8 characters"

        return "Warning: password must contain a minimum 8 characters."
    @staticmethod
    def has_uppercase(password):
        for char in password:
            if char.isupper():
                return "+1 point for upper case characters"

        return "Warning: At least one upper case character is required!"
    @staticmethod
    def has_special_char(password):
        for char in password:
            if char in "!@#$%^&*":
                return "+1 point for special characters"

        return "Warning: At least one special character is required!"
    @staticmethod
    def get_strength_score(password):
        length = PasswordManager.validate_length(password,8)
        print (f"\n{length}")

        uppercase = PasswordManager.has_uppercase(password)
        print (f"\n{uppercase}")

        special = PasswordManager.has_special_char(password)
        print (f"\n{special}")

        for char in password:
            if char in "0,1,2,3,4,5,6,7,8,9":
                return f"\n+1 point for having at least one digit!"

        return f"\nWarning: At least one digit is required!"

print(PasswordManager.get_strength_score("Man#"))