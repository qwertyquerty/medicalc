import tkinter.messagebox

def calvert_formula(age, weight, creatinine, gender, AUC):
    GFR = ((140 - age) * weight) / (72 * creatinine)

    GFR = min(GFR, 125)

    if gender == "female":
        GFR *= 0.85

    return (GFR + 25) * AUC


def rituxan_dose_formula(mg_per_hour, bag_volume, dose_volume):
    return mg_per_hour * (bag_volume / dose_volume)


def string_is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def string_is_int(string):
    return string.isdigit()

def warning_box(message):
    return tkinter.messagebox.showwarning(title="WARNING", message=message)