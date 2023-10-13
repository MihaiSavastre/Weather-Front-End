from tkinter import *
from WeatherData import display_data

from Constants import FORECAST_DISPLAY_WIDTH


def run_GUI():
    main = Tk()
    main.title("Weather for all")
    main.geometry("500x600")

    location_frame = Frame(main, bg="green")
    location_frame.grid(row=0, column=0, sticky=W + E)

    days_frame = Frame(main, bg="light green")
    days_frame.grid(row=1, column=0, sticky=W + E)

    button_frame = LabelFrame(main, bg="yellow", fg="white", padx=0, pady=15)
    button_frame.grid(row=2, column=0)

    # The list of weather forecasts; allows scrolling through the forecasts
    # credit for the implementation to blog.teclado.com
    results_frame = Frame(main)
    results_frame.grid(row=3)
    results_canvas = Canvas(results_frame, width=FORECAST_DISPLAY_WIDTH)
    scrollbar = Scrollbar(results_frame, orient="vertical", command=results_canvas.yview)

    results_scrollable_frame = Frame(results_canvas, bg="#7AC5CD")
    results_scrollable_frame.columnconfigure(0, weight=3)
    results_scrollable_frame.columnconfigure(1, weight=1)

    results_scrollable_frame.bind(
        "<Configure>",
        lambda e: results_canvas.configure(
            scrollregion=results_canvas.bbox("all")
        )
    )
    results_canvas.create_window((0, 0), window=results_scrollable_frame, anchor="nw")
    results_canvas.configure(yscrollcommand=scrollbar.set)
    results_canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # x scrolling
    # This can be necessary if the values for the width of text boxes and the size of the frame are inadequate
    # It can happen for the icons column in the results to not appear on the screen, so scrolling horizontally
    # can be necessary. With the default values set in Constants, this problem is avoided

    # scrollbar_x = Scrollbar(results_frame, orient="horizontal", command=results_canvas.xview)
    # results_canvas.configure(xscrollcommand=scrollbar_x.set)
    # scrollbar_x.pack(side="bottom", fill="x")

    # Location Field
    location_input = StringVar()
    # add a title and the input field
    location_prompt = Label(location_frame, text='Location:', font='Calibri 14 bold', bg="#66CD00")
    location_field = Entry(location_frame, textvariable=location_input, font='Calibri 16 bold')
    location_prompt.grid(row=0, column=0, sticky=N, pady=5, padx=5)
    location_field.grid(row=0, column=1, sticky=N, pady=5, padx=5)
    # and organize them in the grid
    location_frame.columnconfigure(0, weight=1)
    location_frame.columnconfigure(1, weight=3)

    # Days Field as a dropdown menu
    options = [str(i) for i in range(0, 15)]
    days = StringVar()
    days.set("0")
    dropdown = OptionMenu(days_frame, days, *options)
    dropdown.grid(row=1, column=1, pady=5, padx=5, sticky=W)
    dropdown_label = Label(days_frame, text="Number of days after today \n you wish the forecast for", bg="#66CD00")
    dropdown_label.grid(row=1, column=0, pady=5, padx=5, sticky=W)
    days_frame.columnconfigure(0, weight=1)
    days_frame.columnconfigure(1, weight=1)

    Button(button_frame,
           command=lambda: display_data(location_input.get(), results_scrollable_frame, int(days.get()) + 1),
           text="Check Weather", font="Calibri 12", bg='#FF9912', padx=5, pady=5).pack()

    main.mainloop()


run_GUI()
