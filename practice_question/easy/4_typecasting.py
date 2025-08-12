# string to int, float, boolean

value = input("Enter a value")
int(value)
print(f"string to int {int(value)}")
print(f"String to float {float(value)}")
print(f"String to boolean {bool(value)}")


# type casting of list elements

list1 = ["12", "23", "34"]
integers = [int(x) for x in list1]
print(integers)

float_list = [float(x) for x in integers]
print(float_list)

string_list = [str(x) for x in float_list]
print(string_list)