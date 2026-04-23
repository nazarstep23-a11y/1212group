import random
from colorama import init, Fore, Style

init(autoreset=True)

enemies_hp = [50, 70, 100]
my_hp = 100
sword = 20
heal_power = 40

print(Fore.CYAN + Style.BRIGHT + "--- ПОЧАТОК ГЕРОЇЧНОЇ БИТВИ ---")

for i in range(len(enemies_hp)):
    print(f"\n>>> ВОРОГ №{i + 1} ({enemies_hp[i]} HP) <<<")

    while enemies_hp[i] > 0 and my_hp > 0:
        print(f"Ваше HP: {Fore.GREEN}{my_hp}{Style.RESET_ALL} | HP ворога: {Fore.RED}{enemies_hp[i]}")

        secret = random.randint(1, 2)
        user_input = input("Твій вибір (1 або 2): ")

        try:
            guess = int(user_input)
        except ValueError:
            print(Fore.YELLOW + "Вводь тільки цифри!")
            continue

        if guess == secret:
            crit_chance = random.randint(1, 3)
            if crit_chance == 1:
                damage = sword * 2
                print(Fore.MAGENTA + Style.BRIGHT + f"КРИТИЧНИЙ УДАР! Ти вгадав {secret} і зніс {damage} HP!")
            else:
                damage = sword
                print(Fore.GREEN + f"ВЛУЧИВ! Ти вгадав {secret}. Урон: {damage}")

            enemies_hp[i] -= damage
        else:
            my_hp -= 10
            print(Fore.RED + f"ПРОМАХ! Було число {secret}. Ворог вдарив тебе на 10 HP.")

    if my_hp <= 0:
        print(Fore.RED + Style.BRIGHT + "\nТи пав смертю хоробрих...")
        break

    print(Fore.YELLOW + f"Ворог №{i + 1} знищений!")

    if i < len(enemies_hp) - 1:
        my_hp += heal_power
        if my_hp > 100:
            my_hp = 100
        print(Fore.CYAN + f"Ти випив зілля! Тепер у тебе {my_hp} HP.")

if my_hp > 0:
    print(Fore.GREEN + Style.BRIGHT + "\n==============================")
    print(Fore.GREEN + Style.BRIGHT + "\nВІТАЮ! ТИ ПЕРЕМІГ УСІХ ВОРОГІВ!")
    print(Fore.GREEN + Style.BRIGHT + "\n==============================")