def profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

profile(name="raj", age=25, city="delhi")