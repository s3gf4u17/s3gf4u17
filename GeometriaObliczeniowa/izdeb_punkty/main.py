import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import matplotlib.pyplot as plt
from shapely.geometry import Point as shPoint
from shapely.geometry.polygon import Polygon as shPolygon
import numpy as np

def calculate_angle(a, b, c):
    # wektory
    ab=[b.y-a.y,b.x-a.x]
    ac=[c.y-a.y,b.x-a.x]
    # katy kierunkowy
    A=np.arctan2(ac[0],ac[1])-np.arctan2(ab[0],ab[1])
    if A<-np.pi:return np.degrees(A+2*np.pi)
    if A>np.pi:np.degrees(A-2*np.pi)

# polygon - object with points
# point - object wuth x and y
def in_polygon(polygon,point):
    if not point.inBBOX:return False
    s = 0
    x = polygon[:,0]
    y = polygon[:,1]
    # sprawdzenie wierzcholka
    for i in range(len(polygon)):
        if point.x == x[i] and point.y == y[i]:
            return True
    # sprawdzenie środka
    for i in range(len(polygon)):
        if i != len(polygon) - 1:
            diff = calculate_angle(point, Point(x[i], y[i]), Point(x[i+1], y[i+1]))
            s += diff
    if 359.90 < s and s < 360.1:
        return True
    else:
        return False

class Window:
    def __init__(self):
        self.pol=None
        self.poi=None
        self.plo=None
        self.root=tk.Tk()
        self.root.title("Geometria Obliczeniowa")
        self.root.geometry("300x510")
        self.root.resizable(False,False)
        l1=ttk.Label(self.root,text ="Zaimportuj dane poligonu:")
        b1=ttk.Button(self.root,text="Wczytaj plik",command=self.read_polygon)
        self.l3=ttk.Label(self.root,text ="Liczba wierzchołków:")
        s1=ttk.Separator(self.root, orient='horizontal')
        l2=ttk.Label(self.root,text ="Zaimportuj dane punktów:")
        b2=ttk.Button(self.root,text="Wczytaj plik",command=self.read_points)
        self.l4=ttk.Label(self.root,text ="Całkowita liczba punktów:")
        self.l5=ttk.Label(self.root,text ="Liczba punktów w poligonie:")
        self.l6=ttk.Label(self.root,text ="Liczba punktów w bbox:")
        s2=ttk.Separator(self.root, orient='horizontal')
        l7=ttk.Label(self.root,text ="Zbadaj pojedynczy punkt:")
        l8=ttk.Label(self.root,text ="Współrzędna x:")
        self.e1=ttk.Entry(self.root)
        l9=ttk.Label(self.root,text ="Współrzędna y:")
        self.e2=ttk.Entry(self.root)
        b3=ttk.Button(self.root,text="Sprawdź punkt",command=self.check_point)
        self.l10=ttk.Label(self.root,text ="W poligonie:")
        self.l11=ttk.Label(self.root,text ="W bbox:")
        s3=ttk.Separator(self.root, orient='horizontal')
        b4=ttk.Button(self.root,text="Wizualizuj pojedynczy punkt",command=self.plot_point)
        b5=ttk.Button(self.root,text="Wizualizuj zaimportowane punkty",command=self.plot_points)
        elements=[l1,b1,self.l3,s1,l2,b2,self.l4,self.l5,self.l6,s2,l7,l8,self.e1,l9,self.e2,b3,self.l10,self.l11,s3,b4,b5]
        for element in elements: element.pack(padx=10,pady=3,fill=tk.X)

    def read_polygon(self):
        datafile=fd.askopenfilename()
        self.pol=Polygon(datafile)
        content="Liczba wierzchołków: "+str(len(self.pol.x))
        self.l3.config(text=content)

    def read_points(self):
        datafile=fd.askopenfilename()
        self.poi=Points(datafile)
        content="Całkowita liczba punktów: "+str(len(self.poi.points))
        self.l4.config(text=content)
        self.poi.check_points(self.pol)
        ibbox=0
        ipoly=0
        for point in self.poi.points:
            if point.insideBbox: ibbox+=1
            if point.insidePolygon: ipoly+=1
        content="Liczba punktów w poligonie: "+str(ipoly)
        self.l5.config(text=content)
        content="Liczba punktów w bbox: "+str(ibbox)
        self.l6.config(text=content)

    def check_point(self):
        vertices=[(self.pol.x[i],self.pol.y[i]) for i in range(0,len(self.pol.x))]
        p=Point(float(self.e1.get()),float(self.e2.get()))
        newpoint = shPoint(p.x,p.y)
        newpolygon =  shPolygon(vertices)
        if newpolygon.buffer(0.001).contains(newpoint): p.insidePolygon = True
        content="W poligonie: " + str(p.insidePolygon)
        self.l10.config(text=content)
        content="W bbox: " + str(self.pol.minX <= p.x <= self.pol.maxX and self.pol.minY <= p.y <= self.pol.maxY)
        self.l11.config(text=content)

    def plot_point(self):
        vertices=[(self.pol.x[i],self.pol.y[i]) for i in range(0,len(self.pol.x))]
        p=Point(float(self.e1.get()),float(self.e2.get()))
        newpoint = shPoint(p.x,p.y)
        newpolygon =  shPolygon(vertices)
        if [p.x,p.y] in vertices:p.insidePolygon=True
        if self.pol.minX <= p.x <= self.pol.maxX and self.pol.minY <= p.y <= self.pol.maxY: p.insideBbox=True
        if newpolygon.buffer(0.001).contains(newpoint): p.insidePolygon = True
        plo=Plotter([p],self.pol)
        plo.plot_env()

    def plot_points(self):
        vertices=[(self.pol.x[i],self.pol.y[i]) for i in range(0,len(self.pol.x))]
        plo=Plotter(self.poi.points,self.pol)
        plo.plot_env()

    def run(self):
        self.root.mainloop()

class Points:
    def __init__(self,file):
        self.points=[]
        with open(file,"r") as f:points_str=[point[:-1] for point in f.readlines()]
        for point in points_str:self.points.append(Point(float(point.split(" ")[0]),float(point.split(" ")[1])))

    def check_points(self,pol):
        for p in self.points:
            # checks if point in bbox
            if pol.minX <= p.x <= pol.maxX and pol.minY <= p.y <= pol.maxY:p.insideBbox=True
            if p.insideBbox:
                # checks if point is a vertex
                vertices=[(pol.x[i],pol.y[i]) for i in range(0,len(pol.x))]
                if [p.x,p.y] in vertices:p.insidePolygon=True
                newpoint = shPoint(p.x,p.y)
                newpolygon =  shPolygon(vertices)
                if newpolygon.buffer(0.001).contains(newpoint): p.insidePolygon = True

class Point:
    def __init__(self,x,y):
        self.insidePolygon=False
        self.insideBbox=False
        self.x=x
        self.y=y

class Polygon:
    def __init__(self,file):
        with open(file,"r") as f:vertices=[vertex[:-1] for vertex in f.readlines()]
        self.x=[float(vertex.split(";")[0]) for vertex in vertices]
        self.y=[float(vertex.split(";")[1]) for vertex in vertices]
        self.maxX = max(self.x)
        self.maxY = max(self.y)
        self.minX = min(self.x)
        self.minY = min(self.y)

class Plotter:
    def __init__(self,points,polygon):
        self.points=points
        self.polygon=polygon
    
    def plot_env(self):
        plt.plot(self.polygon.y,self.polygon.x)
        xs_i=[]
        ys_i=[]
        xs_b=[]
        ys_b=[]
        for p in self.points:
            if p.insidePolygon:
                xs_i.append(p.x)
                ys_i.append(p.y)
            elif p.insideBbox:
                xs_b.append(p.x)
                ys_b.append(p.y)
        plt.scatter(ys_i,xs_i,marker="X",color="g")
        plt.scatter(ys_b,xs_b,marker="x",color="r")
        plt.show()

if __name__=="__main__":
    #plo=Plotter(poi.points,pol)
    #plo.plot_env()
    win=Window()
    win.run()