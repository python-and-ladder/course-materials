class EnglishSpeaker:
    def greet(self):
        return "Hello!"

    def farewell(self):
        return "Goodbye!"

class SpanishSpeaker:
    def greet(self):
        return "¡Hola!"

    def farewell(self):
        return "¡Adiós!"

class FrenchSpeaker:
    def greet(self):
        return "Bonjour!"

    def farewell(self):
        return "Au revoir!"

def interact(speaker):
    """This function works with any object that has greet() and farewell() methods"""
    print(speaker.greet())
    print(speaker.farewell())
    print()

# Polymorphism in action
english = EnglishSpeaker()
spanish = SpanishSpeaker()
french = FrenchSpeaker()

interact(english)  # Hello! Goodbye!
interact(spanish)  # ¡Hola! ¡Adiós!
interact(french)   # Bonjour! Au revoir!
