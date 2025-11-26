#!/usr/bin/env python3
"""
Simple Calculator CLI Application
For students with Roll Number % 2 = 0
"""

class Calculator:
    """A simple calculator with basic operations"""
    
    @staticmethod
    def add(a, b):
        """Add two numbers"""
        return a + b
    
    @staticmethod
    def subtract(a, b):
        """Subtract b from a"""
        return a - b
    
    @staticmethod
    def multiply(a, b):
        """Multiply two numbers"""
        return a * b
    
    @staticmethod
    def divide(a, b):
        """Divide a by b"""
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        return a / b
    
    @staticmethod
    def power(a, b):
        """Calculate a raised to power b"""
        return a ** b
    
    @staticmethod
    def modulo(a, b):
        """Calculate a modulo b"""
        if b == 0:
            raise ValueError("Cannot calculate modulo with zero!")
        return a % b


def main():
    """Main function to run the calculator CLI"""
    calculator = Calculator()
    
    print("=" * 50)
    print("       SIMPLE CALCULATOR CLI APPLICATION")
    print("=" * 50)
    print("\nAvailable Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (^)")
    print("6. Modulo (%)")
    print("7. Exit")
    print("=" * 50)
    
    while True:
        try:
            choice = input("\nEnter operation number (1-7): ").strip()
            
            if choice == '7':
                print("\nThank you for using Calculator CLI!")
                print("Goodbye! 👋")
                break
            
            if choice not in ['1', '2', '3', '4', '5', '6']:
                print("❌ Invalid choice! Please enter a number between 1-7.")
                continue
            
            # Get numbers from user
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("❌ Invalid input! Please enter valid numbers.")
                continue
            
            # Perform operation
            result = None
            operation = ""
            
            if choice == '1':
                result = calculator.add(num1, num2)
                operation = f"{num1} + {num2}"
            elif choice == '2':
                result = calculator.subtract(num1, num2)
                operation = f"{num1} - {num2}"
            elif choice == '3':
                result = calculator.multiply(num1, num2)
                operation = f"{num1} × {num2}"
            elif choice == '4':
                result = calculator.divide(num1, num2)
                operation = f"{num1} ÷ {num2}"
            elif choice == '5':
                result = calculator.power(num1, num2)
                operation = f"{num1} ^ {num2}"
            elif choice == '6':
                result = calculator.modulo(num1, num2)
                operation = f"{num1} % {num2}"
            
            print(f"\n✅ Result: {operation} = {result}")
            
        except ValueError as e:
            print(f"❌ Error: {e}")
        except KeyboardInterrupt:
            print("\n\nExiting calculator...")
            break
        except Exception as e:
            print(f"❌ An error occurred: {e}")


if __name__ == "__main__":
    main()