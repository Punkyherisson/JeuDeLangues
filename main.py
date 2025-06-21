import tkinter as tk
from tkinter import ttk
import json
import random

LANGUAGES = {
    "Français": "fr",
    "Anglais": "en",
    "Allemand": "de",
    "Espagnol": "es"
}

class ColorQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Multilingue")
        self.score = 0
        self.total = 0
        self.asked_questions = set()

        self.theme = tk.StringVar(value="Couleurs")
        self.source_lang = tk.StringVar(value="Anglais")
        self.target_lang = tk.StringVar(value="Français")

        self.setup_menu()
        self.load_themes()
        self.setup_quiz()

    def setup_menu(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        tk.Label(frame, text="Langue source :").grid(row=0, column=0)
        self.source_menu = ttk.Combobox(frame, textvariable=self.source_lang, values=list(LANGUAGES.keys()), state="readonly")
        self.source_menu.grid(row=0, column=1)

        tk.Label(frame, text="Langue cible :").grid(row=1, column=0)
        self.target_menu = ttk.Combobox(frame, textvariable=self.target_lang, values=list(LANGUAGES.keys()), state="readonly")
        self.target_menu.grid(row=1, column=1)

        tk.Label(frame, text="Thème :").grid(row=2, column=0)
        self.theme_menu = ttk.Combobox(frame, textvariable=self.theme, values=[], state="readonly")
        self.theme_menu.grid(row=2, column=1)

        tk.Button(frame, text="Démarrer le quiz", command=self.start_quiz).grid(row=3, column=0, columnspan=2, pady=5)
        tk.Button(frame, text="Quitter", command=self.root.quit).grid(row=4, column=0, columnspan=2, pady=5)

    def load_themes(self):
        with open("quiz_data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        self.all_data = data["themes"]
        self.theme_menu["values"] = list(self.all_data.keys())
        self.theme.set(list(self.all_data.keys())[0])

    def setup_quiz(self):
        self.quiz_frame = tk.Frame(self.root)

        self.question_label = tk.Label(self.quiz_frame, text="", font=("Arial", 16))
        self.question_label.pack(pady=10)

        self.entry = tk.Entry(self.quiz_frame, font=("Arial", 14))
        self.entry.pack()

        self.submit_btn = tk.Button(self.quiz_frame, text="Valider", command=self.check_answer)
        self.submit_btn.pack(pady=5)

        self.feedback = tk.Label(self.quiz_frame, text="", font=("Arial", 14))
        self.feedback.pack()

        self.score_label = tk.Label(self.quiz_frame, text="Score : 0", font=("Arial", 12))
        self.score_label.pack()

    def start_quiz(self):
        self.src = LANGUAGES[self.source_lang.get()]
        self.tgt = LANGUAGES[self.target_lang.get()]
        selected_theme = self.theme.get()

        if self.src == self.tgt:
            self.feedback.config(text="❌ Langue source et cible identiques !", fg="red")
            return

        self.current_data = self.all_data[selected_theme]
        for word in self.current_data:
            self.current_data[word]["en"] = word

        self.words_list = list(self.current_data.keys())
        self.asked_questions.clear()
        self.score = 0
        self.total = 0

        self.quiz_frame.pack_forget()
        self.quiz_frame.pack(pady=10)
        self.ask_question()

    def ask_question(self):
        if len(self.asked_questions) == len(self.words_list):
            self.question_label.config(text="🎉 Fin du quiz !")
            self.submit_btn.config(state="disabled")
            self.entry.config(state="disabled")
            return

        remaining_words = list(set(self.words_list) - self.asked_questions)
        self.current_word = random.choice(remaining_words)
        self.asked_questions.add(self.current_word)

        self.question_text = self.current_data[self.current_word].get(self.src, self.current_word)
        self.current_answer = self.current_data[self.current_word].get(self.tgt, self.current_word)

        self.question_label.config(text=f"Traduire : {self.question_text}")
        self.entry.delete(0, tk.END)
        self.feedback.config(text="")

    def check_answer(self):
        user_input = self.entry.get().strip().lower()
        correct = self.current_answer.lower()
        self.total += 1

        if user_input == correct:
            self.score += 10
            self.feedback.config(text="✅ Correct !", fg="green")
        else:
            self.score = max(0, self.score - 5)
            self.feedback.config(text=f"❌ Faux ! Rép. : {self.current_answer}", fg="red")

        self.score_label.config(text=f"Score : {self.score}")
        self.root.after(1500, self.ask_question)

# Lancer l'application
if __name__ == "__main__":
    root = tk.Tk()
    app = ColorQuizApp(root)
    root.mainloop()