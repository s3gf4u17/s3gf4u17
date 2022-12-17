import matplotlib.pyplot as plt
import numpy as np
import csv

def data_for_table():
    data = calc_NG0_ng0()
    stacked = np.column_stack((data))
    stacked_ever_ten = []
    for i in range(len(stacked)):
        if i % 10 == 0:
            stacked[i][0] = np.round(stacked[i][0], 2)
            stacked[i][1] = np.round(stacked[i][1], 8)
            stacked_ever_ten.append(stacked[i])

    new_row = ['Ng', 'ng', 'Długość [nm]']
    stacked_ever_ten = np.vstack([new_row, stacked_ever_ten])

    return len(stacked_ever_ten), 3, stacked_ever_ten

def calc_NG0_ng0():
    lam = np.arange(400, 1100+1)
    NG = 287.6155 + (4.8866/((lam/1000)**2)) + (0.0680/((lam/1000)**4))
    ng = (NG/(10**6))+1

    return NG, ng, lam

def plot_NG():
    fig = plt.Figure(figsize=(5, 3.5), dpi=100)
    ax = fig.add_subplot(111)
    ax.grid()

    data = calc_NG0_ng0()
    x = data[2]
    y = data[0]

    fig.tight_layout(pad=0.5)
    fig.subplots_adjust(bottom=0.15)
    fig.subplots_adjust(left=0.13)
    ax.set_ylabel('$Ng_{0}$')
    ax.set_xlabel('Długość fali [nm]')
    ax.plot(x, y)
    return fig

def plot_ng():
    fig = plt.Figure(figsize=(5,3.5), dpi=100)
    ax = fig.add_subplot(111)
    ax.grid()

    data = calc_NG0_ng0()
    x = data[2]
    y = data[1]

    fig.tight_layout(pad=1)
    fig.subplots_adjust(bottom=0.25)
    fig.subplots_adjust(left=0.13)
    ax.set_ylabel('$ng_{0}$')
    ax.set_xlabel('Długość fali [nm]')
    ax.plot(x, y)
    return fig

def correction(data):
    lam = data[0]
    temp_dry = data[1]
    temp_wet = data[2]
    pres = data[3]
    len = data[4]
    N_g0 = 287.6155 + (4.8866/((lam/1000)**2)) + (0.0680/((lam/1000)**4))

    #współczynnik N dla atmosfery standardowej
    T_s = 288.15    #temperatura
    P_s = 1013.25   #ciśnienie
    e_s = 10.87     #ciśnienie pary wodnej
    N_gs = N_g0 * 0.269578 * (P_s/T_s) - 11.27*(e_s/T_s)

    #współczynnik N dla zadanej atmosfery
    Ew = 6.1078*np.exp(17.269*(temp_wet)/(237.30+temp_wet)) #maks. prężność pary w temperaturze mokrej
    e = Ew - (0.000662*pres*(temp_dry-temp_wet)) #ciśnienie pary wodnej
    N_gr = N_g0 * 0.269578 * (pres/(temp_dry+273.15)) - 11.27*(e/(temp_dry+273.15))

    #poprawka w ppm = milimetr na kilometr
    ppm = N_gs - N_gr

    #odległość po poprawce
    new_len = len + ((len/1000)*ppm)/1000
    return [ppm, new_len]

'''
tst_data = [910, 15, 12, 1013.24, 2137]
tst = correction(tst_data)
print(tst)
'''

def circle_arc_diff():
    d = np.arange(1, 101, 1)
    r = 6370 * 8
    delta_c = (d**3/(24*r**2)) * 1000000
    return delta_c, d

def circle_arc_plot():
    fig = plt.Figure(figsize=(6, 5))
    ax = fig.add_subplot(111)
    ax.grid()
    ax.set_xticks(range(0,100+10, 10))
    ax.set_ylabel('Różnica między łukiem a cięciwą [mm]')
    ax.set_xlabel('Długość łuku [km]')

    delta_c, d= circle_arc_diff()

    fig.tight_layout(pad=0.8)
    fig.subplots_adjust(bottom=0.1)
    fig.subplots_adjust(left=0.13)
    ax.plot(d, delta_c)
    return fig

def data_for_2table():
    data = circle_arc_diff()
    delta_c = data[0]
    d = data[1]

    result = np.column_stack((d, np.round(delta_c, 6)))

    new_row = ['Długość [km]', 'Różnica [mm]']
    result = np.vstack([new_row, result])
    return [len(result), 2, result]

def read_csv(file):
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        lp = []
        lam = []
        ts = []
        tm = []
        p = []
        dl = []
        for row in csv_reader:
            if line_count != 0:
                lp.append(float(row[0]))
                lam.append(float(row[1]))
                ts.append(float(row[2]))
                tm.append(float(row[3]))
                p.append(float(row[4]))
                dl.append(float(row[5]))
            line_count += 1


        csv_file.close()
        output = np.column_stack((np.array(lp), np.array(lam), np.array(ts),
                                 np.array(tm), np.array(p), np.array(dl)))

        return output

def save_to_csv(file, ppm, new_len):
    with open(file, mode='w', newline='') as output_file:
        output_data = csv.writer(output_file, delimiter=';')

        output_data.writerow(['lp', 'popr/km', 'odl_popr'])
        for i in range(0, len(ppm)):
            output_data.writerow([i+1, float(np.round(ppm[i], 3)), np.round(new_len[i], 6)])

        output_file.close()

