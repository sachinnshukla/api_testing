from faker import Faker

def generate_fake_user():
    fake = Faker()
    name = fake.name()
    gender = fake.random_element(elements=("male", "female"))
    email = fake.email()
    status = "active"
    return {
        "name": name,
        "gender": gender,
        "email": email,
        "status": status
    }