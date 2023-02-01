import customtkinter as ctk
import re

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("dark-blue")

def check_citation():
    if option_1.get() == type[0]:
        journal()
    if option_1.get() == type[1]:
        book()
    if option_1.get() == type[2]:
        webpage()
    if option_1.get() == type[3]:
        webpage_nd()
    if option_1.get() == type[4]:
        newspaper()
    if option_1.get() == type[5]:
        film()

def journal():
    pattern = r"^(([A-Z][a-z]+,( [A-Z][.])+)([,] [A-Z][a-z]+,( [A-Z][.])+)*([,] & [A-Z][a-z]+,( [A-Z][.])+)?)( \([0-9]{4}\)[.])( [\w\s]+[.])( [\w\s]+[,])( [\d]+\([\d]+\)[,])( [\d]+[-|–][\d]+[.])(( https:\/\/doi.org\/[A-Za-z0-9.,':/_!\-\$\*\+\(\)]+)|( http[A-Za-z0-9.,':/_!\-\$\*\+\(\)]+))$"

    exp = [r"^(([A-Z][a-z]+,( [A-Z][.])+)([,] [A-Z][a-z]+,( [A-Z][.])+)*([,] & [A-Z][a-z]+,( [A-Z][.])+)?)", r"( \([0-9]{4}\)[.])", r"( [A-Z][\w\s]+[.])", r"( [\w\s]+[,])", r"( [\d]+\([\d]+\)[,])", r"( [\d]+[-|–][\d]+[.])", r"(( https:\/\/doi.org\/[A-Za-z0-9.,':/_!\-\$\*\+\(\)]+)|( http[A-Za-z0-9.,':/_!\-\$\*\+\(\)]+))$"]
    name = ["Author(s) Last Name & Initial", "Publication Year", "Article Title", "Journal Title", "Volume & Issue No.", "Pages", "DOI/URL"]

    citation = entry.get("0.0", "end")
    temp = citation
    to_print = ""

    match = re.search(pattern, citation)

    if match:
        to_print += "Valid Citation.\n\n"
    else:
        to_print += "Invalid Citation.\n\n"

    for i in range(7):
        to_print += "["+name[i]+":]\n"

        if re.search(exp[i], temp):
            to_print += (re.search(exp[i], temp).group() + "\n\n")
            temp = re.sub(exp[i], "", temp, count=1)
        else:
            to_print += name[i]+" not found or not in correct format.\n\n"
    
    output(to_print)

def book():
    pattern = r"^(([A-Z][a-z]+,( [A-Z][.])+)([,] [A-Z][a-z]+,( [A-Z][.])+)*([,] & [A-Z][a-z]+,( [A-Z][.])+)?)( \([\d]{4}\)[.])(([\w\s]+)(\([\w.]+ ed.\))?[.])( [A-Z][\w\s]+[.])(( https:\/\/doi.org\/[A-Za-z0-9.,':/_!\-\$\*\+\(\)]+)|( http[A-Za-z0-9.,':/_!\-\$\*\+\(\)]+))?$"

    exp = [r"^(([A-Z][a-z]+,( [A-Z][.])+)([,] [A-Z][a-z]+,( [A-Z][.])+)*([,] & [A-Z][a-z]+,( [A-Z][.])+)?)", r"( \([\d]{4}\)[.])", r"(([\w\s]+)(\([\w.]+ ed.\))?[.])", r"( [A-Z][\w\s]+[.])", r"(( https:\/\/doi.org\/[A-Za-z0-9.,':/_!\-\$\*\+\(\)]+)|( http[A-Za-z0-9.,':/_!\-\$\*\+\(\)]+))?$"]
    name = ["Author(s) Last Name & Initial", "Publication Year", "Book Title", "Publisher", "DOI/URL"]

    citation = entry.get("0.0", "end")
    temp = citation
    to_print = ""

    match = re.search(pattern, citation)

    if match:
        to_print += "Valid Citation.\n\n"
    else:
        to_print += "Invalid Citation.\n\n"

    for i in range(5):
        to_print += "["+name[i]+":]\n"

        if re.search(exp[i], temp):
            to_print += (re.search(exp[i], temp).group() + "\n\n")
            temp = re.sub(exp[i], "", temp, count=1)
        else:
            to_print += name[i]+" not found or not in correct format.\n\n"
    
    if re.search(exp[4], temp).group() == "":
                to_print += "No DOI/URL is accepted in Book Citation."

    output(to_print)

def webpage():
    pattern = r"^(([A-Z][a-z]+,( [A-Z][.])+)([,] [A-Z][a-z]+,( [A-Z][.])+)*([,] & [A-Z][a-z]+,( [A-Z][.])+)?)( \([0-9]{4}(, [A-Z][a-z]+ [0-9]{2})?\)[.])( [A-Z][\w\s]+[.])((\s[A-Z][a-z]+)+[.])( http[A-Za-z0-9.,':/_!\-\$\*\+\(\)]+)$"

    exp = [r"^(([A-Z][a-z]+,( [A-Z][.])+)([,] [A-Z][a-z]+,( [A-Z][.])+)*([,] & [A-Z][a-z]+,( [A-Z][.])+)?)", r"( \([0-9]{4}(, [A-Z][a-z]+ [0-9]{2})?\)[.])", r"( [A-Z][\w\s]+[.])", r"((\s[A-Z][a-z]+)+[.])", r"( http[A-Za-z0-9.,':/_!\-\$\*\+\(\)]+)$"]
    name = ["Author(s) Last Name & Initial", "Publication Date", "Title of work", "Website", "URL"]

    citation = entry.get("0.0", "end")
    temp = citation
    to_print = ""

    match = re.search(pattern, citation)

    if match:
        to_print += "Valid Citation.\n\n"
    else:
        to_print += "Invalid Citation.\n\n"

    for i in range(5):
        to_print += "["+name[i]+":]\n"

        if re.search(exp[i], temp):
            to_print += (re.search(exp[i], temp).group() + "\n\n")
            temp = re.sub(exp[i], "", temp, count=1)
        else:
            to_print += name[i]+" not found or not in correct format.\n\n"

    output(to_print)

def webpage_nd():
    pattern = r"^(([A-Z][a-z]+,( [A-Z][.])+)([,] [A-Z][a-z]+,( [A-Z][.])+)*([,] & [A-Z][a-z]+,( [A-Z][.])+)?)( \(n\.d\.\)[.])( [A-Z][\w\s]+[.])((\s[A-Z][a-z]+)+[.])( Retrieved ([A-Z][a-z]+) [0-9]{2}[,] [0-9]{4}[,] from)( http[A-Za-z0-9.,':/_!\-\$\*\+\(\)]+)$"

    exp = [r"^(([A-Z][a-z]+,( [A-Z][.])+)([,] [A-Z][a-z]+,( [A-Z][.])+)*([,] & [A-Z][a-z]+,( [A-Z][.])+)?)", r"( \(n\.d\.\)[.])", r"( [A-Z][\w\s]+[.])", r"((\s[A-Z][a-z]+)+[.])", r"( Retrieved ([A-Z][a-z]+) [0-9]{2}[,] [0-9]{4}[,] from)", r"( http[A-Za-z0-9.,':/_!\-\$\*\+\(\)]+)$"]
    name = ["Author(s) Last Name & Initial", "Publication Date", "Title of work", "Website", "Date retrieved", "URL"]

    citation = entry.get("0.0", "end")
    temp = citation
    to_print = ""

    match = re.search(pattern, citation)

    if match:
        to_print += "Valid Citation.\n\n"
    else:
        to_print += "Invalid Citation.\n\n"

    for i in range(6):
        to_print += "["+name[i]+":]\n"

        if re.search(exp[i], temp):
            to_print += (re.search(exp[i], temp).group() + "\n\n")
            temp = re.sub(exp[i], "", temp, count=1)
        else:
            to_print += name[i]+" not found or not in correct format.\n\n"

    output(to_print)

def newspaper():
    pattern = r"^(([A-Z][a-z]+,( [A-Z][.])+)([,] [A-Z][a-z]+,( [A-Z][.])+)*([,] & [A-Z][a-z]+,( [A-Z][.])+)?)(( \([0-9]{4}(, [A-Z][a-z]+ [0-9]{2})?\)[.])|( \(n\.d\.\)\.))( [A-Z][\w\s]+[.])((\s[A-Z][a-z]+)+[.])( http[A-Za-z0-9.,':/_!\-\$\*\+\(\)]+)$"

    exp = [r"^(([A-Z][a-z]+,( [A-Z][.])+)([,] [A-Z][a-z]+,( [A-Z][.])+)*([,] & [A-Z][a-z]+,( [A-Z][.])+)?)", r"(( \([0-9]{4}(, [A-Z][a-z]+ [0-9]{2})?\)[.])|( \(n\.d\.\)\.))", r"( [A-Z][\w\s]+[.])", r"((\s[A-Z][a-z]+)+[.])", r"( http[A-Za-z0-9.,':/_!\-\$\*\+\(\)]+)$"]
    name = ["Author(s) Last Name & Initial", "Publication Date", "Title of work", "Newspaper", "URL"]

    citation = entry.get("0.0", "end")
    temp = citation
    to_print = ""

    match = re.search(pattern, citation)

    if match:
        to_print += "Valid Citation.\n\n"
    else:
        to_print += "Invalid Citation.\n\n"

    for i in range(5):
        to_print += "["+name[i]+":]\n"

        if re.search(exp[i], temp):
            to_print += (re.search(exp[i], temp).group() + "\n\n")
            temp = re.sub(exp[i], "", temp, count=1)
        else:
            to_print += name[i]+" not found or not in correct format.\n\n"

    to_print += "*No date is accepted in Newspaper Citation"

    output(to_print)

def film():
    pattern = r"^([A-Z][a-z]+,( [A-Z].)+ \([A-Z][a-z]+\)\.)( \([0-9]{4}\)\.)( [\w\s]+\[Film\]\.)(( [A-Z][a-z]+)+\.)$"

    exp = [r"^([A-Z][a-z]+,( [A-Z].)+ \([A-Z][a-z]+\)\.)", r"( \([0-9]{4}\)\.)", r"( [\w\s]+\[Film\]\.)", r"(( [A-Z][a-z]+)+\.)$"]
    name = ["Primary Contributor", "Year", "Title of work", "Publisher/Production Company"]

    citation = entry.get("0.0", "end")
    temp = citation
    to_print = ""

    match = re.search(pattern, citation)

    if match:
        to_print += "Valid Citation.\n\n"
    else:
        to_print += "Invalid Citation.\n\n"

    for i in range(4):
        to_print += "["+name[i]+":]\n"

        if re.search(exp[i], temp):
            to_print += (re.search(exp[i], temp).group() + "\n\n")
            temp = re.sub(exp[i], "", temp, count=1)
        else:
            to_print += name[i]+" not found or not in correct format.\n\n"

    output(to_print)

def output(to_print):
    result = ctk.CTkTextbox(master=frame_1, width=560, height=190)
    result.grid(row=3, column=0, rowspan=4, columnspan=4, pady=10, padx=10)
    result.insert("0.0", to_print)
    result.configure(state="disabled")

app = ctk.CTk()
app.geometry("630x390")
app.title("APA 7 Citation Checker")

type = ["Journal article", "Book", "Webpage", "Webpage (No Date)", "Newspaper", "Film"]

entry = ctk.CTkTextbox(master=app, width=400, height=100)
entry.grid(row=0, column=0, rowspan=3, columnspan=3, pady=(30,0), padx=(30,30), sticky="w")
entry.insert("0.0", "Enter Citation")

option_1 = ctk.CTkOptionMenu(master=app, values=type)
option_1.grid(row=0, column=3, pady=(30,0), padx=(0,30), sticky="w")
check_button = ctk.CTkButton(master=app, text="Check Citation", command=check_citation).grid(row=1, column=3, pady=(10,0), padx=(0,30))

frame_1 = ctk.CTkFrame(master=app, width=570, height=200).grid(row=3, column=0, rowspan=4, columnspan=4, pady=30, padx=30)
result = ctk.CTkTextbox(master=frame_1, width=560, height=190)
result.grid(row=3, column=0, rowspan=4, columnspan=4, pady=10, padx=10)
result.configure(state="disabled")

app.mainloop()