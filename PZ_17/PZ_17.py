#В соответствии с номером варианта перейти по ссылке на прототип. Реализовать
#его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально
#приближенный к оригиналу (см. таблицу 1).




import tkinter as tk
from tkinter import ttk




def toggle_gender_button(button, label):
    if button['bg'] == 'white':
        button['bg'] = 'grey'
        label['fg'] = 'white'
    else:
        button['bg'] = 'white'
        label['fg'] = 'white'

def on_phone_entry_click(event):
    if phone_entry.get() == 'Phone':
        phone_entry.delete(0, "end")
        phone_entry.config(fg='black')

def on_phone_focusout(event):
    if phone_entry.get() == '':
        phone_entry.insert(0, 'Phone')
        phone_entry.config(fg='grey')

root = tk.Tk()

root.title('Python Window')
root.configure(bg='grey')
placeholders = ['Enter First Name', 'Enter Last Name', 'Enter Screen Name']
month_names = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
countries = ['USA', 'Canada', 'Mexico', 'UK', 'France', 'Germany', 'Spain', 'Italy', 'Russia', 'China', 'Japan', 'Australia']

for i, placeholder in enumerate(placeholders):
    label = tk.Label(root, text=f'{placeholder}:', bg='grey', fg='white')
    label.grid(row=i, column=0)
    entry = tk.Entry(root)
    entry.insert(0, placeholder)
    entry.bind('<FocusIn>', lambda event, entry=entry, default_text=placeholder: on_entry_click(event, entry, default_text))
    entry.bind('<FocusOut>', lambda event, entry=entry, default_text=placeholder: on_focusout(event, entry, default_text))
    entry.grid(row=i, column=1)


dob_label = tk.Label(root, text='Date of Birth', bg='grey', fg='white')
dob_label.grid(row=3, column=0)
day_entry = ttk.Combobox(root, state="readonly", values=list(range(1, 32)))
day_entry.grid(row=3, column=1)
month_entry = ttk.Combobox(root, state="readonly", values=month_names)
month_entry.grid(row=3, column=2)
year_entry = ttk.Combobox(root, state="readonly", values=list(range(1900, 2100)))
year_entry.grid(row=3, column=3)


gender_label = tk.Label(root, text='Gender:', bg='grey', fg='white')
gender_label.grid(row=4, column=0)
male_button = tk.Radiobutton(root, bg='white', value=1, command=lambda: toggle_gender_button(male_button, male_label))
male_button.grid(row=4, column=1)
male_label = tk.Label(root, text='Male', bg='grey', fg='white')
male_label.grid(row=4, column=2)
female_button = tk.Radiobutton(root, bg='white', value=2, command=lambda: toggle_gender_button(female_button, female_label))
female_button.grid(row=4, column=3)
female_label = tk.Label(root, text='Female', bg='grey', fg='white')
female_label.grid(row=4, column=4)


country_label = tk.Label(root, text='Country:', bg='grey', fg='white')
country_label.grid(row=5, column=0)
country_entry = ttk.Combobox(root, state="readonly", values=countries)
country_entry.grid(row=5, column=1)


phone_label = tk.Label(root, text='Phone:', bg='grey', fg='white')
phone_label.grid(row=6, column=0)
phone_entry = tk.Entry(root, fg='grey')
phone_entry.insert(0, 'Phone')
phone_entry.bind('<FocusIn>', on_phone_entry_click)
phone_entry.bind('<FocusOut>', on_phone_focusout)
phone_entry.grid(row=6, column=1)





def toggle_password_visibility():
    if password_entry.cget('show') == '*':
        password_entry.config(show='')
    else:
        password_entry.config(show='*')

# Password
password_label = tk.Label(root, text='Password:', bg='grey', fg='white')
password_label.grid(row=8, column=0)

password_entry = tk.Entry(root, show='*', fg='grey')
password_entry.grid(row=8, column=1)

password_button = tk.Button(root, text='Show Password', command=toggle_password_visibility)
password_button.grid(row=8, column=2)



def toggle_confirm_password():
    if confirm_password_entry.cget('show') == '*':
        confirm_password_entry.config(show='')
    else:
        confirm_password_entry.config(show='*')

# Confirm Password
confirm_password_label = tk.Label(root, text='Confirm Password:', bg='grey', fg='white')
confirm_password_label.grid(row=9, column=0)  # измените номера строк в соответствии с вашим местоположением

confirm_password_entry = ttk.Entry(root, show='*')
confirm_password_entry.grid(row=9, column=1)  # измените номера строк в соответствии с вашим местоположением

confirm_password_button = tk.Button(root, text='Show Password', command=toggle_confirm_password)
confirm_password_button.grid(row=9, column=2)  # измените номера строк в соответствии с вашим местоположением


def on_email_entry_click(event):
    if E_mail_label_entry.get() == 'E_mail':
        E_mail_label_entry.delete(0, "end")
        E_mail_label_entry.config(fg='black')

def on_email_focusout(event):
    if E_mail_label_entry.get() == '':
        E_mail_label_entry.insert(0, 'E_mail')
        E_mail_label_entry.config(fg='grey')

E_mail_label = tk.Label(root, text='E_mail:', bg='grey', fg='white')
E_mail_label.grid(row=7, column=0)
E_mail_label_entry = tk.Entry(root, fg='grey')
E_mail_label_entry.insert(0, 'E_mail')
E_mail_label_entry.bind('<FocusIn>', on_email_entry_click)
E_mail_label_entry.bind('<FocusOut>', on_email_focusout)
E_mail_label_entry.grid(row=7, column=1)




def toggle_terms_agreement():
    if terms_checkbutton.cget('bg') == 'white':
        terms_checkbutton.config(bg='grey')
    else:
        terms_checkbutton.config(bg='white')


terms_label = tk.Label(root, text='I agree to the Terms of Use', bg='grey', fg='white')
terms_label.grid(row=10, column=0)


terms_checkbutton = tk.Checkbutton(root, bg='white', command=toggle_terms_agreement)
terms_checkbutton.grid(row=10, column=1)













def on_entry_click(event, entry, default_text):
    # если в поле ввода содержится текст по умолчанию, удаляем его
    if event.widget.get() == default_text:
        event.widget.delete(0, "end")

def on_focusout(event, entry, default_text):
    # если поле ввода пустое, вставляем текст по умолчанию
    if entry.get() == '':
        entry.insert(0, default_text)

root.mainloop()






