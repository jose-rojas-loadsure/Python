# This is a list: It´s recognized by the symbols [,,,].

run_trigger = input("Please RUN TRIGGER, tap ENTER.")

list = [2, 4, 5, 7, 8, 9, 3, 4,10,14,22,21,70,98,100]
for i in list:  # Iterator i in our list.
    if i % 2 != 0:
        continue
    print(i)

print("Thanks for follow that instrucction.")
