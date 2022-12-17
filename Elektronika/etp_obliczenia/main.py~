import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import matplotlib.pyplot as plt
import numpy as np

def button1():
    lam=[]
    for i in range(int(e11.get()),int(e12.get())+1,int(e13.get())):
        lam.append(i/1000)
    ngs=[(287.6155+4.8866/(l*l)+0.0680/(l*l*l*l))/1000000+1 for l in lam]
    Ngs=[287.6155+4.8866/(l*l)+0.0680/(l*l*l*l) for l in lam]
    # ng plot
    plt.plot(lam,ngs,label="ng")
    plt.ticklabel_format(useOffset=False)
    plt.xlabel("lambda [μm]")
    plt.ylabel("ng")
    plt.title("zależność współczynnika ng od długości fali lamda")
    plt.legend()
    plt.show()
    # Ng plot
    plt.plot(lam,Ngs,label="Ng")
    plt.ticklabel_format(useOffset=False)
    plt.xlabel("lambda [μm]")
    plt.ylabel("Ng")
    plt.title("zależność współczynnika Ng od długości fali lamda")
    plt.legend()
    plt.show()

def button2():
    lam=[]
    for i in range(int(e11.get()),int(e12.get())+1,int(e13.get())):
        lam.append(i/1000)
    ngs=[(287.6155+4.8866/(l*l)+0.0680/(l*l*l*l))/1000000+1 for l in lam]
    Ngs=[287.6155+4.8866/(l*l)+0.0680/(l*l*l*l) for l in lam]
    file=fd.asksaveasfilename()
    with open(file,"w+") as f:
        f.write("lambda_um,ng,Ng\n")
        for i in range(0,len(lam)):	
            f.write(str(lam[i])+","+str(ngs[i])+","+str(Ngs[i])+"\n")

def button3():
    lam=float(e21.get())
    temp_dry=float(e22.get())
    temp_wet=float(e23.get())
    pres=float(e24.get())
    len=float(e25.get())
    N_g0=287.6155 + (4.8866/((lam/1000)**2)) + (0.0680/((lam/1000)**4))
    # dla atmosfery standardowej
    T_s = 288.15
    P_s = 1013.25
    e_s = 10.87
    N_gs = N_g0 * 0.269578 * (P_s/T_s) - 11.27*(e_s/T_s)
    Ew = 6.1078*np.exp(17.269*(temp_wet)/(237.30+temp_wet))
    e = Ew - (0.000662*pres*(temp_dry-temp_wet))
    N_gr = N_g0 * 0.269578 * (pres/(temp_dry+273.15)) - 11.27*(e/(temp_dry+273.15))
    ppm = N_gs - N_gr
    new_len = len + ((len/1000)*ppm)/1000
    content1="Poprawka na km: "+str(ppm)+"mm"
    content2="d poprawione: "+str(new_len)+"m"
    l27.config(text=content1)
    l28.config(text=content2)

def button4():
    T_s = 288.15
    P_s = 1013.25
    e_s = 10.87
    datafile=fd.askopenfilename()
    lines=[]
    response=["id;ppm;poprawiona_odleglosc"]
    with open(datafile,"r+") as f:
        lines=f.readlines()
    for line in lines:
        data=line.split(";")
        lam=float(data[1])
        temp_dry=float(data[2])
        temp_wet=float(data[3])
        pres=float(data[4])
        len=float(data[5])
        N_g0=287.6155 + (4.8866/((lam/1000)**2)) + (0.0680/((lam/1000)**4))
        N_gs = N_g0 * 0.269578 * (P_s/T_s) - 11.27*(e_s/T_s)
        Ew = 6.1078*np.exp(17.269*(temp_wet)/(237.30+temp_wet))
        e = Ew - (0.000662*pres*(temp_dry-temp_wet))
        N_gr = N_g0 * 0.269578 * (pres/(temp_dry+273.15)) - 11.27*(e/(temp_dry+273.15))
        ppm = N_gs - N_gr
        new_len = len + ((len/1000)*ppm)/1000
        response.append(data[0]+";"+str(ppm)+";"+str(new_len))
    response='\n'.join(response)
    file=fd.asksaveasfilename()
    with open(file,"w+") as f:
        f.write(response)

def button5():
    ds=[]
    r=8*6378.14
    for i in range(int(e31.get()),int(e32.get())+int(e33.get()),int(e33.get())):
        ds.append(i)
    c=[abs(-((d*d*d)/24/r/r))*1000000 for d in ds]
    plt.ticklabel_format(useOffset=False)
    plt.plot(ds,c,label="c")
    plt.xlabel("d [km]")
    plt.ylabel("delta c [mm]")
    plt.title("roznica dlugosci cieciwy i luku")
    plt.legend()
    plt.show()

def button6():
    ds=[]
    r=8*6378140
    for i in range(int(e31.get()),int(e32.get())+int(e33.get()),int(e33.get())):
        ds.append(i)
    c=[abs(-((d*d*d)/24/r/r))*1000000*1000000 for d in ds]
    file=fd.asksaveasfilename()
    with open(file,"w+") as f:
        f.write("d[km],dc[mm]\n")
        for i in range(0,len(ds)):
            f.write(str(ds[i])+","+str(c[i])+"\n")

root=tk.Tk()
root.title("ETP obliczenia")
root.geometry("300x435")
root.resizable(False,False)
tabControl=ttk.Notebook(root)

tab1=ttk.Frame(tabControl)
tab2=ttk.Frame(tabControl)
tab3=ttk.Frame(tabControl)

tabControl.add(tab1,text='ng i Ng')
tabControl.add(tab2,text='poprawki atmosferyczne')
tabControl.add(tab3,text='łuk i cięciwa')
tabControl.pack(expand=1,fill="both")

# zakladka 1
l11=ttk.Label(tab1,text ="Obliczenie ng i Ng dla fal:")
l12=ttk.Label(tab1,text ="λ0[nm]:")
l13=ttk.Label(tab1,text ="λ1[nm]:")
l14=ttk.Label(tab1,text ="Δλ[nm]:")
e11=ttk.Entry(tab1,width=24)
e12=ttk.Entry(tab1,width=24)
e13=ttk.Entry(tab1,width=24)
e11.insert(0,'400')
e12.insert(0,'1100')
e13.insert(0,'10')
s11=ttk.Separator(tab1, orient='horizontal')
b11=ttk.Button(tab1,text="Zwizualizuj otrzymane wartości",command=button1)
b12=ttk.Button(tab1,text="Wygeneruj tabelę otrzymanych wartości",command=button2)
elements=[l11,l12,e11,l13,e12,l14,e13,s11,b11,b12]
for element in elements: element.pack(padx=10,pady=3,fill=tk.X)

# zakladka 2
l21=ttk.Label(tab2,text ="Obliczenie poprawki atmosferycznej:")
l22=ttk.Label(tab2,text ="λ[nm]:")
l23=ttk.Label(tab2,text="Ts[C]:")
l24=ttk.Label(tab2,text="Tm[C]:")
l25=ttk.Label(tab2,text="p[hPa]:")
l26=ttk.Label(tab2,text="d[m]:")
l27=ttk.Label(tab2,text="Poprawka na km: ")
l28=ttk.Label(tab2,text="d poprawione: ")
e21=ttk.Entry(tab2,width=24)
e22=ttk.Entry(tab2,width=24)
e23=ttk.Entry(tab2,width=24)
e24=ttk.Entry(tab2,width=24)
e25=ttk.Entry(tab2,width=24)
e21.insert(0,'910')
e22.insert(0,'15')
e23.insert(0,'12')
e24.insert(0,'1013.24')
e25.insert(0,'2000')
s21=ttk.Separator(tab2, orient='horizontal')
s22=ttk.Separator(tab2, orient='horizontal')
b21=ttk.Button(tab2,text="Oblicz dla danych",command=button3)
b22=ttk.Button(tab2,text="Oblicz dla pliku",command=button4)
elements=[l21,l22,e21,l23,e22,l24,e23,l25,e24,l26,e25,s21,l27,l28,s22,b21,b22]
for element in elements: element.pack(padx=10,pady=3,fill=tk.X)

# zakladka 3
l31=ttk.Label(tab3,text ="Obliczenie różnicy między łukiem a cięciwą:")
l32=ttk.Label(tab3,text ="d0[km]:")
l33=ttk.Label(tab3,text ="d1[km]:")
l34=ttk.Label(tab3,text ="Δd[km]:")
e31=ttk.Entry(tab3,width=24)
e32=ttk.Entry(tab3,width=24)
e33=ttk.Entry(tab3,width=24)
e31.insert(0,'1')
e32.insert(0,'100')
e33.insert(0,'1')
s31=ttk.Separator(tab3, orient='horizontal')
b31=ttk.Button(tab3,text="Zwizualizuj otrzymane wartości",command=button5)
b32=ttk.Button(tab3,text="Wygeneruj tabelę otrzymanych wartości",command=button6)
elements=[l31,l32,e31,l33,e32,l34,e33,s31,b31,b32]
for element in elements: element.pack(padx=10,pady=3,fill=tk.X)

if __name__ == "__main__":
    root.mainloop()
