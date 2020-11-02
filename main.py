import tkinter as tk
from tkinter import ttk

from components import IntEntry, FloatEntry

from util import warning_box

window = tk.Tk()

TAB_CONTROL = ttk.Notebook(window, width=600, height=300)

CALVERT_TAB = tk.Frame(TAB_CONTROL)
RITUXAN_TAB = tk.Frame(TAB_CONTROL)

TAB_CONTROL.add(CALVERT_TAB, text="Calvert Formula")
TAB_CONTROL.add(RITUXAN_TAB, text="Rituxan Dosage")

TAB_CONTROL.pack(expand=True, fill="both")

### CALVERT FORMULA ###

tk.Label(CALVERT_TAB, text="Patient Age (yr):").grid(row = 0, column = 0, padx = 10, pady = 10, sticky="E")
calvert_age_entry = FloatEntry(CALVERT_TAB)
calvert_age_entry.grid(row = 0, column = 1, padx = 10, pady = 10)


tk.Label(CALVERT_TAB, text="Patient Weight (kg):").grid(row = 1, column = 0, padx = 10, pady = 10, sticky="E")
calvert_weight_entry = FloatEntry(CALVERT_TAB)
calvert_weight_entry.grid(row = 1, column = 1, padx = 10, pady = 10)


tk.Label(CALVERT_TAB, text="Patient Sex:").grid(row = 2, column = 0, padx = 10, pady = 10, sticky="E")

calvert_sex_var = tk.StringVar(window)
calvert_sex_var.set("male")

calvert_sex_menu = tk.OptionMenu(CALVERT_TAB, calvert_sex_var, *{"male", "female"})
calvert_sex_menu.grid(row = 2, column = 1, padx = 10, pady = 10, sticky = "ew")


tk.Label(CALVERT_TAB, text="Creatinine (mg/dL):").grid(row = 0, column = 2, padx = 10, pady = 10, sticky="E")
calvert_creat_entry = FloatEntry(CALVERT_TAB)
calvert_creat_entry.grid(row = 0, column = 3, padx = 10, pady = 10)


tk.Label(CALVERT_TAB, text="Target AUC:").grid(row = 1, column = 2, padx = 10, pady = 10, sticky="E")
calvert_auc_entry = FloatEntry(CALVERT_TAB)
calvert_auc_entry.grid(row = 1, column = 3, padx = 10, pady = 10)


calvert_solution_variable = tk.StringVar()
calvert_solution_label = tk.Label(CALVERT_TAB, textvariable = calvert_solution_variable, font = ("TkDefaultFont", 40))
calvert_solution_label.grid(row = 3, column = 0, padx = 10, pady = 10, rowspan = 3, columnspan = 4, sticky="NESW")


def calvert_calculate():
	from util import calvert_formula

	age = calvert_age_entry.get_float()
	weight = calvert_weight_entry.get_float()
	sex = calvert_sex_var.get()
	creat = calvert_creat_entry.get_float()
	auc = calvert_auc_entry.get_float()

	if age <= 0: return warning_box("Age must be greater than zero!")
	if age >= 130: warning_box("Age exceeds normal range!")

	if weight <= 0: return warning_box("Weight must be greater than zero!")
	if weight < 8 or weight >= 300: warning_box("Weight outside of normal range!")


	try:
		solution = calvert_formula(age, weight, creat, sex, auc)
	except ZeroDivisionError:
		return

	solution = max(solution, 0)

	calvert_solution_variable.set("{}mg".format(round(solution, 2)))

def calvert_clear():
	calvert_age_entry.set("")
	calvert_weight_entry.set("")
	calvert_sex_var.set("male")
	calvert_creat_entry.set("")
	calvert_auc_entry.set("")
	calvert_solution_variable.set("")

calvert_calculate_button = tk.Button(CALVERT_TAB, text='Calculate', command=calvert_calculate)
calvert_calculate_button.grid(row = 2, column = 3, padx = 10, pady = 10, sticky="NESW")

calvert_clear_button = tk.Button(CALVERT_TAB, text='Clear', command=calvert_clear)
calvert_clear_button.grid(row = 2, column = 2, padx = 10, pady = 10, sticky="NESW")

### RITUXAN DOSAGE ###

tk.Label(RITUXAN_TAB, text="Rituxan Rate (mg/h):").grid(row = 0, column = 0, padx = 10, pady = 10, sticky="E")
rituxan_rate_entry = FloatEntry(RITUXAN_TAB)
rituxan_rate_entry.grid(row = 0, column = 1, padx = 10, pady = 10)


tk.Label(RITUXAN_TAB, text="Bag Volume (mg):").grid(row = 1, column = 0, padx = 10, pady = 10, sticky="E")
rituxan_bag_volume_entry = FloatEntry(RITUXAN_TAB)
rituxan_bag_volume_entry.grid(row = 1, column = 1, padx = 10, pady = 10)


tk.Label(RITUXAN_TAB, text="Dose Volume (mg):").grid(row = 0, column = 2, padx = 10, pady = 10, sticky="E")
rituxan_total_dose_entry = FloatEntry(RITUXAN_TAB)
rituxan_total_dose_entry.grid(row = 0, column = 3, padx = 10, pady = 10, columnspan = 1)


rituxan_solution_variable = tk.StringVar()
rituxan_solution_label = tk.Label(RITUXAN_TAB, textvariable = rituxan_solution_variable, font = ("TkDefaultFont", 40))
rituxan_solution_label.grid(row = 3, column = 0, padx = 10, pady = 10, rowspan = 4, columnspan = 4, sticky="NESW")


def rituxan_calculate():
	from util import rituxan_dose_formula

	rate = rituxan_rate_entry.get_float()
	bag_volume = rituxan_bag_volume_entry.get_float()
	total_dose = rituxan_total_dose_entry.get_float()

	if total_dose <= 0: return warning_box("Dose Volume must be greater than zero!")
	if bag_volume <= 0: return warning_box("Bag Volume must be greater than zero!")

	try:
		solution = rituxan_dose_formula(rate, bag_volume, total_dose)
	except ZeroDivisionError:
		return

	solution = max(solution, 0)

	if solution < 100 or solution >= 1000:
		warning_box("Dosage outside of normal range! Ensure your values are correct!")

	rituxan_solution_variable.set("{}mg".format(round(solution, 2)))

def rituxan_clear():
	rituxan_rate_entry.set("")
	rituxan_bag_volume_entry.set("")
	rituxan_total_dose_entry.set("")
	rituxan_solution_variable.set("")

rituxan_calculate_button = tk.Button(RITUXAN_TAB, text='Calculate', command=rituxan_calculate)
rituxan_calculate_button.grid(row = 1, column = 3, padx = 10, pady = 10, sticky="NESW")

rituxan_clear_button = tk.Button(RITUXAN_TAB, text='Clear', command=rituxan_clear)
rituxan_clear_button.grid(row = 1, column = 2, padx = 10, pady = 10, sticky="NESW")


### RUN THE WINDOW ###

window.title("NurseAlert")
window.geometry("560x260")
window.resizable(False, False)
window.mainloop()