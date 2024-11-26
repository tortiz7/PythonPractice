# Write a Python function fahrenheit_to_celsius(fahrenheit) that converts a temperature from Fahrenheit to Celsius. The script should prompt the user for a temperature in Fahrenheit, use the function to convert it and print the result.
while True:
    temp_far = input("Hello there! please give me a temperature in fahrenheit, and I will happily convert it to celcisus for you!: ")

    def convert_f_to_c(temp_far):
        temp_far = float(temp_far)
        temp_cel = (temp_far - 32) * 5.00 / 9.00
        print(f"{temp_far}°F is: {round(temp_cel, 2)}°C!")

    convert_f_to_c(temp_far)
    try_again = input("Would you like to convert another temperature from Fahrenheit to Celsius? y/n: ").casefold()
    if try_again == "y":
        continue
    else: 
        break

 


