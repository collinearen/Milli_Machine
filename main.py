import tkinter as tk


class Window(object):
    def __init__(self):
        #       <----  TRANSITION AND OUTPUT TABLES  ---->
        self.transition_table = {
            'Q1': {'X1': 'Q1', 'X2': 'Q4', 'X3': 'Q2'},
            'Q2': {'X1': 'Q3', 'X2': 'Q6', 'X3': 'Q5'},
            'Q3': {'X1': 'Q6', 'X2': 'Q5', 'X3': 'Q3'},
            'Q4': {'X1': 'Q1', 'X2': 'Q5', 'X3': 'Q2'},
            'Q5': {'X1': 'Q2', 'X2': 'Q4', 'X3': 'Q6'},
            'Q6': {'X1': 'Q4', 'X2': 'Q1', 'X3': 'Q3'},
        }

        self.output_table = {
            'Q1': {'X1': 'Y1', 'X2': 'Y1', 'X3': 'Y3'},
            'Q2': {'X1': 'Y2', 'X2': 'Y1', 'X3': 'Y1'},
            'Q3': {'X1': 'Y1', 'X2': 'Y2', 'X3': 'Y3'},
            'Q4': {'X1': 'Y1', 'X2': 'Y3', 'X3': 'Y3'},
            'Q5': {'X1': 'Y2', 'X2': 'Y1', 'X3': 'Y1'},
            'Q6': {'X1': 'Y2', 'X2': 'Y1', 'X3': 'Y3'},
        }

        #       <----  SETTINGS WINDOW  ---->
        self.root = tk.Tk()
        self.root.geometry('600x700')
        self.root.title('Milli Machine')
        self.buttons_disabled = False
        self.our_image = tk.PhotoImage(file="images/Mealy_machine.png")
        self.our_image = self.our_image.subsample(3, 3)
        self.our_label = tk.Label(self.root)
        self.our_label.image = self.our_image
        self.our_label['image'] = self.our_label.image
        self.our_label.place(x=0, y=200)

        #        <----  CREATING INPUT FIELDS AND BUTTONS   ---->
        self.current_state_q = ''

        self.input_field = tk.Entry(self.root, width=15)
        self.input_field.grid(row=1, column=0, padx=10, pady=10)

        self.x1_button = tk.Button(self.root, text='X1', width=1,
                                   command=lambda: self.input_field.insert(tk.END, 'X1 '))
        self.x1_button.grid(row=1, column=3, padx=5, pady=5)

        self.x2_button = tk.Button(self.root, text='X2', width=1,
                                   command=lambda: self.input_field.insert(tk.END, 'X2 '))
        self.x2_button.grid(row=1, column=4, padx=5, pady=5)

        self.x3_button = tk.Button(self.root, text='X3', width=1,
                                   command=lambda: self.input_field.insert(tk.END, 'X3 '))
        self.x3_button.grid(row=1, column=5, padx=5, pady=5)

        self.q1_button = tk.Button(self.root, text='Q1', width=1, command=lambda: self.q_button_click('Q1'))
        self.q1_button.grid(row=2, column=3, padx=5, pady=5)

        self.q2_button = tk.Button(self.root, text='Q2', width=1, command=lambda: self.q_button_click('Q2'))
        self.q2_button.grid(row=2, column=4, padx=5, pady=5)

        self.q3_button = tk.Button(self.root, text='Q3', width=1, command=lambda: self.q_button_click('Q3'))
        self.q3_button.grid(row=2, column=5, padx=5, pady=5)

        self.q4_button = tk.Button(self.root, text='Q4', width=1, command=lambda: self.q_button_click('Q4'))
        self.q4_button.grid(row=3, column=3, padx=5, pady=5)

        self.q5_button = tk.Button(self.root, text='Q5', width=1, command=lambda: self.q_button_click('Q5'))
        self.q5_button.grid(row=3, column=4, padx=5, pady=5)

        self.q6_button = tk.Button(self.root, text='Q6', width=1, command=lambda: self.q_button_click('Q6'))
        self.q6_button.grid(row=3, column=5, padx=5, pady=5)

        #           <----   CREATING AN OUTPUT FIELD AND BUTTONS    ---->
        self.start_state_field = tk.Entry(self.root, width=15)
        self.start_state_field.grid(row=2, column=0, padx=10, pady=10)

        self.reset_button = tk.Button(self.root, bg='red', text='Reset!', width=3,
                                      command=lambda: self.clear_fields(self.input_field, self.start_state_field))
        self.reset_button.place(x=390, y=150)

        self.start_button = tk.Button(self.root, bg='green', text='Start!', width=3,
                                      command=lambda: self.create_output_field(self.root))
        self.start_button.place(x=485, y=150)

        self.one_field = tk.Label(self.root, text='Введите входное слово')
        self.one_field.grid(row=1, column=1, padx=10, pady=10)

        self.two_field = tk.Label(self.root, text='Введите начальное состояние')
        self.two_field.grid(row=2, column=1, padx=10, pady=10)

        self.output_field = tk.Label(self.root, font='Times 20', foreground='green',
                                     text=f'Выходное слово равно {self.process_input(input_string=self.input_field.get())}')

        self.current_state_field = tk.Label(self.root, font='Times 15', text='', foreground='green')
        self.current_state_field.place(x=5, y=150)

    def disable_q_buttons(self):
        self.q1_button.config(state=tk.DISABLED)
        self.q2_button.config(state=tk.DISABLED)
        self.q3_button.config(state=tk.DISABLED)
        self.q4_button.config(state=tk.DISABLED)
        self.q5_button.config(state=tk.DISABLED)
        self.q6_button.config(state=tk.DISABLED)
        self.buttons_disabled = True

    def q_button_click(self, q):
        if not self.buttons_disabled:
            self.disable_q_buttons()
        self.start_state_field.insert(tk.END, q)

    def disable_buttons(self):
        if not self.buttons_disabled:
            self.q1_button.config(state='disabled')
            self.q2_button.config(state='disabled')
            self.q3_button.config(state='disabled')
            self.q4_button.config(state='disabled')
            self.q5_button.config(state='disabled')
            self.q6_button.config(state='disabled')
            self.buttons_disabled = True

    def clear_fields(self, input_field, start_state_field):
        input_field.delete(0, tk.END)
        start_state_field.delete(0, tk.END)
        self.output_field.config(text='')
        self.current_state_q = ''
        self.current_state_field.config(text='')
        if self.buttons_disabled:
            self.q1_button.config(state=tk.NORMAL)
            self.q2_button.config(state=tk.NORMAL)
            self.q3_button.config(state=tk.NORMAL)
            self.q4_button.config(state=tk.NORMAL)
            self.q5_button.config(state=tk.NORMAL)
            self.q6_button.config(state=tk.NORMAL)
            self.buttons_disabled = False

    def create_output_field(self, root):
        self.disable_buttons()
        self.output_field.config(font='Times 20', foreground='green',
                                 text=f'Выходное слово равно '
                                      f'{self.process_input(input_string=self.input_field.get(), start_state=self.start_state_field.get().strip())}')
        self.output_field.place(x=0, y=100)

    def process_input(self, input_string, start_state='Q1'):
        current_state = start_state
        input_tokens = input_string.split()
        output_tokens = []
        current_state_q = f'{self.start_state_field.get()} < '

        for token in input_tokens:
            output = self.output_table[current_state][token]
            current_state = self.transition_table[current_state][token]
            current_state_q += current_state + ' < '
            self.current_state_field.config(text=f'Все состояния: {current_state_q[0:-2]}', foreground='red',
                                            font='Times 20')

            output_tokens.append(output)

        return ' '.join(output_tokens)


if __name__ == '__main__':
    wnd = Window()
    wnd.root.mainloop()
