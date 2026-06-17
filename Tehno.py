import random
import time
import json
import os


class TechnoGames:

    def guess_number(self):
        print("\n🎮 УГАДАЙ ЧИСЛО (1–10)")
        secret = random.randint(1, 10)

        attempts = 3

        while attempts > 0:
            guess = input("Твоя попытка: ")

            if not guess.isdigit():
                print("❌ Введи число!")
                continue

            guess = int(guess)

            if guess == secret:
                print("🎉 Победа!")
                input("Enter чтобы вернуться в меню...")
                return
            else:
                attempts -= 1
                print(f"❌ Неверно. Осталось: {attempts}")

        print(f"\n💀 Игра окончена. Было число: {secret}")
        input("Enter чтобы вернуться в меню...")

    def quiz(self):
        print("\n🧠 ВИКТОРИНА")

        questions = [
            ("Что такое Python? (язык/змея)", "язык"),
            ("2 + 2 = ?", "4"),
            ("Столица Казахстана?", "астана")
        ]

        score = 0

        for q, a in questions:
            ans = input(q + " ").lower().strip()

            if ans == a:
                print("✔ Верно")
                score += 1
            else:
                print(f"❌ Неверно (ответ: {a})")

        print(f"\n🏁 Результат: {score}/{len(questions)}")
        input("Enter чтобы вернуться в меню...")

    def reaction_test(self):
        print("\n⚡ ТЕСТ РЕАКЦИИ")
        print("Жди GO...")

        time.sleep(random.uniform(2, 5))
        print("GO! Жми Enter!")

        start = time.time()
        input()
        end = time.time()

        reaction_time = end - start
        ms = reaction_time * 1000

        print(f"\n⏱ {reaction_time:.3f} сек ({ms:.0f} мс)")

        self.save_history(reaction_time)
        self.save_best(reaction_time)

        avg = self.get_average()
        if avg:
            print(f"📈 Среднее: {avg:.3f}")

        input("Enter чтобы вернуться в меню...")

    def save_best(self, value):
        file = "best.json"

        if os.path.exists(file):
            with open(file, "r") as f:
                data = json.load(f)
        else:
            data = {"best": 999}

        if value < data["best"]:
            data["best"] = value
            print("🏆 НОВЫЙ РЕКОРД!")

        with open(file, "w") as f:
            json.dump(data, f)

    def save_history(self, value):
        with open("history.txt", "a") as f:
            f.write(f"{value}\n")

    def get_average(self):
        if not os.path.exists("history.txt"):
            return None

        with open("history.txt", "r") as f:
            times = [float(x.strip()) for x in f.readlines() if x.strip()]

        return sum(times) / len(times) if times else None