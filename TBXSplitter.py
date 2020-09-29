import tkinter as tk
from tkinter import filedialog as fd
from tkinter.filedialog import askopenfilename
from XMLReader import XMLReader


def open_file():
    filename = askopenfilename(filetypes=[("TBX Files", "*.tbx"), ("All Files", "*.")])
    if not filename:
        return
    entry_input_file_name.delete(0, tk.END)
    entry_input_file_name.insert(0, filename)


def get_path():
    filepath = fd.askdirectory()

    if not filepath:
        return
    entry_output_file_name.delete(0, tk.END)
    entry_output_file_name.insert(0, filepath)


def quit_program():
    window.destroy()


def hello_script():
    split_file_name = entry_input_file_name.get()
    save_file_path = entry_output_file_name.get()

    concept_entry_count = entry_concept_count.get()
    XMLReader.readXML(split_file_name, save_file_path, concept_entry_count)
    # os.system(f"XMLReader.py {split_file_name} {save_file_path} {concept_entry_count}")


window = tk.Tk()
window.title("TBX Splitter")
window.maxsize(600, 180)
window.minsize(600, 180)

# Configure window
window.rowconfigure([0, 1, 2], weight=1)
window.columnconfigure(0, weight=1)

# create containers
frame_input_text = tk.Frame(window, width=300, height=40, borderwidth=1)
frame_input_file_select = tk.Frame(window, width=300, height=110)
frame_output_text = tk.Frame(window, width=300, height=40, borderwidth=1)
frame_output_file_select = tk.Frame(window, width=300, height=110)
frame_buttons = tk.Frame(window, width=300, height=40, borderwidth=1)
frame_concept_count = tk.Frame(window, width=300, height=40, borderwidth=1)

# set frames
frame_input_text.grid(row=0, sticky="nsew")
frame_input_file_select.grid(row=1, sticky="nsew")
frame_output_text.grid(row=2, sticky="nsew")
frame_output_file_select.grid(row=3, sticky="nsew")
frame_concept_count.grid(row=4, sticky="nsew")
frame_buttons.grid(row=5, sticky="nsew")

# Create widgets for top frame
file_input_message = "Please select a file to split: "
label_input_file_select = tk.Label(frame_input_text, text=file_input_message)
label_input_file_select.pack()

# Create widgets for input file frame
entry_input_file_name = tk.Entry(frame_input_file_select, width=80)
browse_input_file_btn = tk.Button(frame_input_file_select, text="Select File..", command=open_file)
entry_input_file_name.pack(side=tk.LEFT, expand=True)
browse_input_file_btn.pack(side=tk.RIGHT, expand=True)

# Create widgets for output file text frame
file_output_message = "Please select a directory save split files to: "
label_output_file_select = tk.Label(frame_output_text, text=file_output_message)
label_output_file_select.pack()

# Create widgets for output file frame
entry_output_file_name = tk.Entry(frame_output_file_select, width=80)
browse_output_file_btn = tk.Button(frame_output_file_select, text="Select File..", command=get_path)
entry_output_file_name.pack(side=tk.LEFT, expand=True)
browse_output_file_btn.pack(side=tk.RIGHT, expand=True)

# Create widgets for the number of conceptEntries frame
conceptLabel = "Enter the number of conceptEntries for each file: "
concept_count_text = tk.Label(frame_concept_count, text=conceptLabel)
entry_concept_count = tk.Entry(frame_concept_count, width=10)
concept_count_text.pack(side=tk.LEFT, padx=10)
entry_concept_count.pack(side=tk.LEFT, pady=5)

# create widgets for bottom frame
go_button = tk.Button(frame_buttons, text="Run", width=15, command=hello_script)
cancel_button = tk.Button(frame_buttons, text="Quit", width=15, command=quit_program)

go_button.pack(side=tk.RIGHT, padx=10, pady=5)
cancel_button.pack(side=tk.RIGHT)

window.mainloop()
