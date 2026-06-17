import json

class Portfolio:
    def __init__(self, file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            self.data = json.load(f)

    def show_about(self):
        print("\n=== О СЕБЕ ===")
        print(self.data.get("about", "Информация отсутствует"))

    def show_goal(self):
        print("\n=== ЦЕЛЬ ===")
        print(self.data.get("goal", "Информация отсутствует"))

    def show_story(self):
        print("\n=== ИСТОРИЯ ===")
        print(self.data.get("story", "Информация отсутствует"))

    def show_mentor(self):
        print("\n=== МЕНТОР ===")
        print(self.data.get("mentor", "Информация отсутствует"))

    def show_progress(self):
        print("\n=== ПРОГРЕСС ===")
        print(self.data.get("progress", "Информация отсутствует"))

    def show_hobbies(self):
        print("\n=== ХОББИ ===")
        print(self.data.get("hobbies", "Информация отсутствует"))

    def show_works(self):
        print("\n=== РАБОТЫ ===")
        print(self.data.get("works", "Информация отсутствует"))

    def show_github(self):
        print("\n=== GITHUB ===")
        print(self.data.get("github", "Информация отсутствует"))

