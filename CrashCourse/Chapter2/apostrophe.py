message = "Python’s standard library is massive, and just about every function one needs to perform is available in its library."
print(message)

print(f"Removing suffix {message.removesuffix('library.')}")

message = message.removesuffix(', and just about every function one needs to perform is available in its library.')
print(message)