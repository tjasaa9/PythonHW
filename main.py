import json

with open("results_file.json", "r") as results:
    results = json.loads(results_file.read())
    print("Top results: " + str(results))

user_name = input("Dobrodošel/a v kvizu! Za začetek mi zaupaj tvoje ime: ")
print(f"Pozdravljen/a, {user_name} :). To je kviz, na katerega odgovarjaš le z eno (začetno) črko. Primer: Na katero črko se začne beseda 'pes'? Odgovor: p.  Razumljivo? Pa začniva!")

answer = input("Na katero črko se začne programski jezik, ki se ga trenutno učiš?")           #1
if answer == "p":
    print("Pravilno!")
else:
    print("Žal je tvoj odgovor napačen.")


answer = input("flsijf")               #2
if answer == "f":
    print("Pravilno!")
else:
    print("Žal je tvoj odgovor napačen.")


answer = input("flsijf")            #3
if answer == "f":
    print("Pravilno!")
else:
    print("Žal je tvoj odgovor napačen.")


answer = input("flsijf")            #4
if answer == "f":
    print("Pravilno!")
else:
    print("Žal je tvoj odgovor napačen.")


answer = input("flsijf")            #5
if answer == "f":
    print("Pravilno!")
else:
    print("Žal je tvoj odgovor napačen.")


answer = input("flsijf")            #6
if answer == "f":
    print("Pravilno!")
else:
    print("Žal je tvoj odgovor napačen.")


answer = input("flsijf")            #7
if answer == "f":
    print("Pravilno!")
else:
    print("Žal je tvoj odgovor napačen.")


answer = input("flsijf")            #8
if answer == "f":
    print("Pravilno!")
else:
    print("Žal je tvoj odgovor napačen.")


answer = input("flsijf")            #9
if answer == "f":
    print("Pravilno!")
else:
    print("Žal je tvoj odgovor napačen.")


answer = input("flsijf")            #10
if answer == "f":
    print("Pravilno!")
else:
    print("Žal je tvoj odgovor napačen.")
