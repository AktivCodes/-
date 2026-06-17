from portfolio import Portfolio
from Tehno import TechnoGames
from logo import show_logo

p = Portfolio("data.json")
games = TechnoGames()


show_logo()
input("Enter to continue...")

def pause():
    input("\nEnter чтобы вернуться в меню...")

def menu():
    print("\n" + "═" * 35)
    print("   ⚡ PORTFOLIO SYSTEM ⚡")
    print("═" * 35)

    print("👉[1] О себе")
    print("👉[2] Моя цель")
    print("👉[3] История в IT")
    print("👉[4] Ментор")
    print("👉[5] Прогресс")
    print("👉[6] Хобби")
    print("👉[7] Мои работы")
    print("👉[8] GitHub")
    print("👉[9] Мини-игры")
    print("👉[0] Выход")

    print("═" * 35)

while True:
    menu()
    choice = input("Выбери пункт: ").strip()

    if choice == "1":
        p.show_about()
        pause()

    elif choice == "2":
        p.show_goal()
        pause()

    elif choice == "3":
        p.show_story()
        pause()

    elif choice == "4":
        p.show_mentor()
        pause()

    elif choice == "5":
        p.show_progress()
        pause()

    elif choice == "6":
        p.show_hobbies()
        pause()

    elif choice == "7":
        p.show_works()
        pause()

    elif choice == "8":
        p.show_github()
        pause()

    elif choice == "9":
        print("\n1 - Угадай число")
        print("2 - Викторина")
        print("3 - Тест реакции")

        g = input("Выбор: ").strip()

        if g == "1":
            games.guess_number()
        elif g == "2":
            games.quiz()
        elif g == "3":
            games.reaction_test()
        else:
            print("Неверный выбор")
            pause()

    elif choice == "0":
        print("Выход...")
        break

    else:
        print("Неверный пункт меню!")
        pause()