nome = input("type your name: ")
idade = input('type your age: ')

if nome and idade:
    print(f"Your name is {nome}")
    print(f"your name inverted is {nome[::-1]}")
    if " " in nome:
        print("Your name have spaces")
    else:
        print("Your name don't have spaces")
    print(f"Your name have {len(nome)} letter")
    print(f"The first letter of your name is {nome[0]}")
    print(f"The last letter of your name is {nome[-1]}")
else:
    print("Sorry, you left empty spaces") 