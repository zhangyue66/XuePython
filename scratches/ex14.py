from sys import argv

script,user_name,love = argv

prompt = " :)"

print(f"Hi {user_name},I'm the {script} script.")
print("i'd like to ask you a few questions.")
print(f"do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer doo you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me. You live in {lives}. Not sure where that is:
And you have a {computer} computer.Nice!
""")

print(f"I would like to say i love you , {love}!")