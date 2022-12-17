from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from calc import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class CreateToolTip(object):
    """
    create a tooltip for a given widget
    """
    def __init__(self, widget, text='widget info'):
        self.waittime = 20     #miliseconds
        self.wraplength = 180   #pixels
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<ButtonPress>", self.leave)
        self.id = None
        self.tw = None

    def enter(self, event=None):
        self.schedule()

    def leave(self, event=None):
        self.unschedule()
        self.hidetip()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.showtip)

    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)

    def showtip(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        # creates a toplevel window
        self.tw = Toplevel(self.widget)
        # Leaves only the label and removes the app window
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(self.tw, text=self.text, justify='left',
                       background="#ffffff", relief='solid', borderwidth=1,
                       wraplength = self.wraplength)
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tw
        self.tw= None
        if tw:
            tw.destroy()

class Table:
    def __init__(self, root, total_rows, total_columns, lst):
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(root, width=10, fg='black', font=('Arial', 13, 'bold'))
                if j == 0:
                    self.e = Entry(root, width=7, fg='black', font=('Arial', 13, 'bold'))
                if j == 2:
                    self.e = Entry(root, width=12, fg='black', font=('Arial', 13, 'bold'))

                self.e.grid(row=i, column=j)

                if j == 2 and i != 0:
                    self.e.insert(END, str(int(float(lst[i][j]))))
                else:
                    self.e.insert(END, lst[i][j])

                self.e.config(state='disabled', disabledbackground='white', disabledforeground='black')
                if i == 0:
                    self.e.config(state='disabled', disabledbackground='#f0f073', disabledforeground='black',
                                  highlightbackground="black", highlightthickness=1)


class Table2:
    def __init__(self, root, total_rows, total_columns, lst):
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(root, width=12, fg='black', font=('Arial', 12, 'bold'))

                self.e.grid(row=i, column=j)
                if i == 0:
                    self.e.insert(END, lst[i][j])

                if j == 0 and i != 0:
                    self.e.insert(END, str(int(float(lst[i][j]))))
                elif j == 1 and i != 0:
                    temp = f'{float(lst[i][j]):.6f}'
                    self.e.insert(END, temp)

                self.e.config(state='disabled', disabledbackground='white', disabledforeground='black')
                if i == 0:
                    self.e.config(state='disabled', disabledbackground='#f0f073', disabledforeground='black',
                                  highlightbackground="black", highlightthickness=1)

class myWindow:
    def __init__(self, wnd, title, geom):
        self.window = wnd
        self.window.title(title)
        self.window.geometry(geom)
        self.widget_init()
        self.window.resizable(False, False)

    def widget_init(self):
        self.all_tabs = ttk.Notebook(self.window)
        self.all_tabs.pack(fill='both', expand=1)

        self.tab1 = Frame(self.all_tabs)
        self.tab1.pack()
        first_tab(self.tab1)

        self.tab2 = Frame(self.all_tabs)
        self.tab2.pack()
        second_tab(self.tab2)

        self.tab3 = Frame(self.all_tabs)
        self.tab3.pack()
        third_tab(self.tab3)

        self.all_tabs.add(self.tab1, text='Ng i ng (wykres i tabela)')
        self.all_tabs.add(self.tab2, text='Obliczenie poprawki')
        self.all_tabs.add(self.tab3, text='Różnica między łukiem a cięciwą')

class first_tab:

    def __init__(self, parent_frame):
        self.frame = parent_frame
        self.widget_init()

    def widget_init(self):
        #frame na wykresy
        plot_frame = Frame(self.frame)
        plot_frame.pack(side=LEFT, pady=5, padx=5)

        #wykres górny
        fig_NG = plot_NG()
        canvas = FigureCanvasTkAgg(fig_NG, plot_frame)
        canvas.draw()
        canvas.get_tk_widget().grid(column=0, row=0)

        #wykres dolny
        fig_ng = plot_ng()
        canvas = FigureCanvasTkAgg(fig_ng, plot_frame)
        canvas.draw()
        canvas.get_tk_widget().grid(column=0, row=1)

        #Scrollbar
        right_frame = Frame(self.frame)
        right_frame.pack(fill=BOTH, expand=1)

        my_canvas = Canvas(right_frame)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        my_scrollbar = Scrollbar(right_frame, orient='vertical', command=my_canvas.yview)
        my_scrollbar.place(x=370, y=0, height=675) #place zamiast pack, żeby ustawić scrollbar tak żeby był widoczny

        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))

        frame_in_canvas = Frame(my_canvas)
            #tym wyśrodkowałem tabelkę
        my_canvas.create_window((45,0), window=frame_in_canvas, anchor='nw')

        #tabelka
        data = data_for_table()
        Table(frame_in_canvas, data[0], data[1], data[2])


class second_tab:
    def __init__(self, parent_frame):
        self.frame = parent_frame
        self.widget_init()

    def widget_init(self):
        entries = Frame(self.frame)
        entries.grid(column=0, row=0, pady=10, padx=10)

        #opisy pól entry
        lam_label = Label(entries, text='Długość fali [nm]:', font=('Arial', 15, 'bold'))
        lam_label.grid(column=0, row=0, ipady=5, sticky='w')
        temp_label = Label(entries, text='Temperatura sucha [°C]:', font=('Arial', 15, 'bold'))
        temp_label.grid(column=0, row=1, ipady=5, sticky='w')
        tempw_label = Label(entries, text='Temperatura mokra [°C]:', font=('Arial', 15, 'bold'))
        tempw_label.grid(column=0, row=2, ipady=5, sticky='w')
        pres_label = Label(entries, text='Ciśnienie [hPa]:', font=('Arial', 15, 'bold'))
        pres_label.grid(column=0, row=3, ipady=5, sticky='w')
        len_label = Label(entries, text='Pomierzona długość [m]:', font=('Arial', 15, 'bold'))
        len_label.grid(column=0, row=4, ipady=5, sticky='w')

        #pola entry
        self.lam_entry = Entry(entries, font=('Arial', 15), width=57)
        self.lam_entry.grid(column=1, row=0, sticky='nsew')
        self.temp_entry = Entry(entries, font=('Arial', 15), width=57)
        self.temp_entry.grid(column=1, row=1, sticky='nsew')
        self.tempw_entry = Entry(entries, font=('Arial', 15), width=57)
        self.tempw_entry.grid(column=1, row=2, sticky='nsew')
        self.pres_entry = Entry(entries, font=('Arial', 15), width=57)
        self.pres_entry.grid(column=1, row=3, sticky='nsew')
        self.len_entry = Entry(entries, font=('Arial', 15), width=57)
        self.len_entry.grid(column=1, row=4, sticky='nsew')
        self.entry_fields = [self.lam_entry, self.temp_entry, self.tempw_entry, self.pres_entry, self.len_entry]

        #przycisk oblicz
        count_frame = Frame(self.frame)
        count_frame.grid(column=0, row=1, sticky='nsew')
        self.count_btn = Button(count_frame, text='Oblicz', font=('Arial', 15, 'bold'), command=self.count, width=30, bd=3)
        self.count_btn.pack(fill=Y, expand=1, padx=10)

        result = Frame(self.frame)
        result.grid(column=0, row=2, padx=10, pady=10,  sticky='w')

        #wyniki (poprawka i długość)
        correction_label = Label(result, text='Poprawka na km:', font=('Arial', 15, 'bold'))
        correction_label.grid(column=0, row=0, ipady=5, sticky='w')
        new_len_label = Label(result, text='Poprawiona odległość [m]:', font=('Arial', 15, 'bold'))
        new_len_label.grid(column=0, row=1, ipady=5, sticky='w')

        self.correction_entry = Entry(result, font=('Arial', 15), width=56)
        self.correction_entry.grid(column=1, row=0, sticky='nsw')
        self.new_len_entry = Entry(result, font=('Arial', 15), width=56)
        self.new_len_entry.grid(column=1, row=1, sticky='nsw')

        button = Frame(self.frame)
        button.grid(column=0, row=3, sticky='nsew', padx=10, pady=65)

        #przycisk do importowania
        self.import_btn = Button(button, text='Odczytaj dane z pliku csv', font=('Arial', 15, 'bold'), bd=3, width=30, height=6, command=self.save_csv)
        self.import_btn.pack(side=TOP, expand=1)
        CreateToolTip (self.import_btn, text='Format pliku: \n lp;lam;ts;tm;p;dl \n'
                                             'Aby otworzyć plik w excelu należy zaimportować plik csv do excela.'
                                             '\nBezpośrednie otwarcie pliku w excelu może spowodować zmianę niektórych wartości na datę.')

    def get_entries(self):
        lam = float(self.lam_entry.get())
        temp_dry = float(self.temp_entry.get())
        temp_wet = float(self.tempw_entry.get())
        pres = float(self.pres_entry.get())
        len = float(self.len_entry.get())

        return lam, temp_dry, temp_wet, pres, len

    def count(self):
        self.correction_entry.delete(0, END)
        self.new_len_entry.delete(0, END)

        ppm, new_len = correction(self.get_entries())
        self.correction_entry.insert(0, str(np.round(ppm, 2)))
        self.new_len_entry.insert(0, str(np.round(new_len, 4)))

    def save_csv(self):
        #odczyt
        csv_file = filedialog.askopenfilename(initialdir='C:/', title='Zaimportuj plik csv', filetypes=[("Csv files", "*.csv")])

        #to co ma się zapisać
        data = read_csv(csv_file)
        ppm = []
        dl = []
        for i in data:
            temp_data = correction(i[1:6])
            ppm.append(temp_data[0])
            dl.append(temp_data[1])

        #zapis
        f = filedialog.asksaveasfile(initialfile='result.csv', title='Zapisz plik wynikowy jako:', mode='w', defaultextension=".csv")

        save_to_csv(f.name, ppm, dl)

class third_tab:
    def __init__(self, parent_frame):
        self.frame = parent_frame
        self.widget_init()

    def widget_init(self):
        plot_frame = Frame(self.frame)
        plot_frame.pack(side=LEFT)

        fig = circle_arc_plot()
        canvas = FigureCanvasTkAgg(fig, plot_frame)
        canvas.draw()
        canvas.get_tk_widget().grid(column=0, row=0, padx=10, pady=5)

        #Scrollbar
        right_frame = Frame(self.frame)
        right_frame.pack(fill=BOTH, expand=1)

        my_canvas = Canvas(right_frame)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        my_scrollbar = Scrollbar(right_frame, orient='vertical', command=my_canvas.yview)
        my_scrollbar.place(x=260, y=0, height=675)

        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))

        frame_in_canvas = Frame(my_canvas)
            #tym wyśrodkowałem tabelkę
        my_canvas.create_window((10,0), window=frame_in_canvas, anchor='nw')

        data = data_for_2table()
        Table2(frame_in_canvas, data[0], data[1], data[2])


