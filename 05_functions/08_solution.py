def print_kwargs(**kwargs):
  for key, value in kwargs.items():
    print(f"{key} : {value}")

print_kwargs(name = "genius")
print_kwargs(name = "genius", email = "genius@genius.com")
print_kwargs(name = "genius", email = "genius@genius.com", password = "123456")