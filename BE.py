class Person:
    count = 0  # Class variable to count objects

    def __init__(self, name):
        self.name = name
        Person.count += 1  # Increment count when a new object is created

    @classmethod
    def get_count(cls):
        return cls.count
    
# Example usage
person1 = Person("Alice")
person2 = Person("Bob")
print("Number of Person objects created:", Person.get_count())