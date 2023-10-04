import tkinter as tk

transition_table = {
    'Q1': {'X1': 'Q1', 'X2': 'Q4', 'X3': 'Q2'},
    'Q2': {'X1': 'Q3', 'X2': 'Q6', 'X3': 'Q5'},
    'Q3': {'X1': 'Q6', 'X2': 'Q5', 'X3': 'Q3'},
    'Q4': {'X1': 'Q1', 'X2': 'Q5', 'X3': 'Q2'},
    'Q5': {'X1': 'Q2', 'X2': 'Q4', 'X3': 'Q6'},
    'Q6': {'X1': 'Q4', 'X2': 'Q1', 'X3': 'Q3'},
}

output_table = {
    'Q1': {'X1': 'Y1', 'X2': 'Y1', 'X3': 'Y3'},
    'Q2': {'X1': 'Y2', 'X2': 'Y1', 'X3': 'Y1'},
    'Q3': {'X1': 'Y1', 'X2': 'Y2', 'X3': 'Y3'},
    'Q4': {'X1': 'Y1', 'X2': 'Y3', 'X3': 'Y3'},
    'Q5': {'X1': 'Y2', 'X2': 'Y1', 'X3': 'Y1'},
    'Q6': {'X1': 'Y2', 'X2': 'Y1', 'X3': 'Y3'},
}

# Создание главного окна
root = tk.Tk()
root.geometry('600x450')
root.title('Milli Machine')

buttons_disabled = False

# Создание полей ввода и кнопок
input_field = tk.Entry(root, width=15)
input_field.grid(row=1, column=0, padx=10, pady=10)

x1_button = tk.Button(root, text='X1', width=1, command=lambda: input_field.insert(tk.END, 'X1 '))
x1_button.grid(row=1, column=3, padx=5, pady=5)

x2_button = tk.Button(root, text='X2', width=1, command=lambda: input_field.insert(tk.END, 'X2 '))
x2_button.grid(row=1, column=4, padx=5, pady=5)

x3_button = tk.Button(root, text='X3', width=1, command=lambda: input_field.insert(tk.END, 'X3 '))
x3_button.grid(row=1, column=5, padx=5, pady=5)

buttons_disabled = False


def disable_q_buttons():
    global buttons_disabled
    q1_button.config(state=tk.DISABLED)
    q2_button.config(state=tk.DISABLED)
    q3_button.config(state=tk.DISABLED)
    q4_button.config(state=tk.DISABLED)
    q5_button.config(state=tk.DISABLED)
    q6_button.config(state=tk.DISABLED)
    buttons_disabled = True


def q_button_click(q):
    global buttons_disabled
    if not buttons_disabled:
        disable_q_buttons()
    start_state_field.insert(tk.END, q)


our_image = tk.PhotoImage(file="")
our_image = our_image.subsample(3, 3)
our_label = tk.Label(root)
our_label.image = our_image
our_label['image'] = our_label.image
our_label.place(x=0, y=200)

one_field = tk.Label(root, text='Введите входное слово')
one_field.grid(row=1, column=1, padx=10, pady=10)

two_field = tk.Label(root, text='Введите начальное состояние')
two_field.grid(row=2, column=1, padx=10, pady=10)

# Создание полей ввода и кнопок
input_field = tk.Entry(root, width=15)
input_field.grid(row=1, column=0, padx=10, pady=10)

x1_button = tk.Button(root, text='X1', width=1, command=lambda: input_field.insert(tk.END, 'X1 '))
x1_button.grid(row=1, column=3, padx=5, pady=5)

x2_button = tk.Button(root, text='X2', width=1, command=lambda: input_field.insert(tk.END, 'X2 '))
x2_button.grid(row=1, column=4, padx=5, pady=5)

x3_button = tk.Button(root, text='X3', width=1, command=lambda: input_field.insert(tk.END, 'X3 '))
x3_button.grid(row=1, column=5, padx=5, pady=5)

q1_button = tk.Button(root, text='Q1', width=1, command=lambda: q_button_click('Q1'))
q1_button.grid(row=2, column=3, padx=5, pady=5)

q2_button = tk.Button(root, text='Q2', width=1, command=lambda: q_button_click('Q2'))
q2_button.grid(row=2, column=4, padx=5, pady=5)

q3_button = tk.Button(root, text='Q3', width=1, command=lambda: q_button_click('Q3'))
q3_button.grid(row=2, column=5, padx=5, pady=5)

q4_button = tk.Button(root, text='Q4', width=1, command=lambda: q_button_click('Q4'))
q4_button.grid(row=3, column=3, padx=5, pady=5)

q5_button = tk.Button(root, text='Q5', width=1, command=lambda: q_button_click('Q5'))
q5_button.grid(row=3, column=4, padx=5, pady=5)

q6_button = tk.Button(root, text='Q6', width=1, command=lambda: q_button_click('Q6'))
q6_button.grid(row=3, column=5, padx=5, pady=5)


def disable_buttons():
    global buttons_disabled
    if not buttons_disabled:
        q1_button.config(state='disabled')
        q2_button.config(state='disabled')
        q3_button.config(state='disabled')
        q4_button.config(state='disabled')
        q5_button.config(state='disabled')
        q6_button.config(state='disabled')
        buttons_disabled = True


# Создание поля вывода и кнопок
start_state_field = tk.Entry(root, width=15)
start_state_field.grid(row=2, column=0, padx=10, pady=10)

reset_button = tk.Button(root, bg='red', text='Reset!', width=3,
                         command=lambda: clear_fields(input_field, start_state_field))
reset_button.place(x=390, y=150)

start_button = tk.Button(root, bg='green', text='Start!', width=3, command=lambda: create_output_field(root))
start_button.place(x=485, y=150)


def clear_fields(input_field, start_state_field):
    global output_field, buttons_disabled, current_state_q
    input_field.delete(0, tk.END)
    start_state_field.delete(0, tk.END)
    output_field.config(text='')
    current_state_q = ''
    current_state_field.config(text='')
    if buttons_disabled:
        q1_button.config(state=tk.NORMAL)
        q2_button.config(state=tk.NORMAL)
        q3_button.config(state=tk.NORMAL)
        q4_button.config(state=tk.NORMAL)
        q5_button.config(state=tk.NORMAL)
        q6_button.config(state=tk.NORMAL)
        buttons_disabled = False


def create_output_field(root):
    global output_field
    disable_buttons()
    output_field.config(font='Times 20', foreground='green',
                        text=f'Выходное слово равно {process_input(input_string=input_field.get(), start_state=start_state_field.get().strip())}')
    output_field.place(x=0, y=100)


current_state_field = tk.Label(root, font='Times 15', text='', foreground='green')
current_state_field.place(x=5, y=150)

current_state_q = ''


def process_input(input_string, start_state='Q1'):
    global current_state_q
    current_state = start_state
    input_tokens = input_string.split()
    output_tokens = []
    current_state_q = f'{start_state_field.get()} < '

    for token in input_tokens:
        output = output_table[current_state][token]
        current_state = transition_table[current_state][token]
        current_state_q += current_state + ' < '
        current_state_field.config(text=f'Все состояния: {current_state_q[0:-2]}', foreground='red', font='Times 20')

        output_tokens.append(output)

    return ' '.join(output_tokens)


output_field = tk.Label(root, font='Times 20', foreground='green',
                        text=f'Выходное слово равно {process_input(input_string=input_field.get())}')

root.mainloop()
