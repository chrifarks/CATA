from tkinter import *
import numpy as np
import math
from decimal import *
import matplotlib.pyplot as plt

getcontext().prec = 10
janela = Tk()


def project():
    t0 = 2000
    t1 = 2010
    t2 = 2020
    t3 = 2030
    t4 = 2040
    t5 = 2050
    pop_0 = int(ed.get())  # População em 2000
    pop_1 = int(ed1.get())  # População em 2010
    pop_2 = int(ed2.get())  # População em 2020
    art_ = t0, t1, t2, t3, t4, t5
    year = np.array(art_)

    # estabelecer para logistio

    # Método Aritmético
    r = (pop_2 - pop_0) / (2020 - 2000)
    P_1 = pop_0 + r * (2010 - 2000)
    P_2 = pop_0 + r * (2020 - 2000)
    P_3 = pop_0 + r * (2030 - 2000)
    P_4 = pop_0 + r * (2040 - 2000)
    P_5 = pop_0 + r * (2050 - 2000)
    art = pop_0, P_1, P_2, P_3, P_4, P_5
    lb_hab_0['text'] = int(pop_0)
    lb_hab_1['text'] = int(P_1)
    lb_hab_2['text'] = int(P_2)
    lb_hab_3['text'] = int(P_3)
    lb_hab_4['text'] = int(P_4)
    lb_hab_5['text'] = int(P_5)
    pop = np.array(art)

    # Método Geométrico
    rg = ((np.log(pop_2) - np.log(pop_0)) / (2020 - 2000))
    ex = float(math.e)
    Pg_1 = pop_0 * (ex ** (rg * (2010 - 2000)))
    Pg_2 = pop_0 * (ex ** (rg * (2020 - 2000)))
    Pg_3 = pop_0 * (ex ** (rg * (2030 - 2000)))
    Pg_4 = pop_0 * (ex ** (rg * (2040 - 2000)))
    Pg_5 = pop_0 * (ex ** (rg * (2050 - 2000)))
    geo = pop_0, Pg_1, Pg_2, Pg_3, Pg_4, Pg_5
    lb_hag_0['text'] = pop_0
    lb_hag_1['text'] = int(Pg_1)
    lb_hag_2['text'] = int(Pg_2)
    lb_hag_3['text'] = int(Pg_3)
    lb_hag_4['text'] = int(Pg_4)
    lb_hag_5['text'] = int(Pg_5)
    pop_geo = np.array(geo)

    # Método Curva Logística
    pf1: int = ((2 * pop_0 * pop_1 * pop_2) - (pop_1 ** 2) * (pop_0 + pop_2))
    pf2: int = (pop_0 * pop_2) - pop_1 ** 2
    ps1 = int(pf1 / pf2)
    ps11 = ps1, ps1, ps1, ps1, ps1, ps1
    pop_ps = np.array(ps11)
    c = Decimal((ps1 - pop_0) / pop_0)
    a1 = pop_0 * (ps1 - pop_1)
    a2 = pop_1 * (ps1 - pop_0)
    w = (1 / (t2 - t1))
    ww = math.log(a1 / a2)
    k = float("{0:.3f}".format(w * ww))
    k1 = Decimal(k)
    v_e3 = Decimal(k1 * int(t3 - t0))
    v_e4 = Decimal(k1 * int(t4 - t0))
    v_e5 = Decimal(k1 * int(t5 - t0))
    e = Decimal(math.e)
    e3 = e ** v_e3
    e4 = e ** v_e4
    e5 = e ** v_e5
    v3 = c * e3
    v4 = c * e4
    v5 = c * e5
    pz3 = ps1 / (1 + v3)
    pz4 = ps1 / (1 + v4)
    pz5 = ps1 / (1 + v5)
    pl = pop_0, pop_1, pop_2, pz3, pz4, pz5
    lb_hal_0['text'] = pop_0
    lb_hal_1['text'] = pop_1
    lb_hal_2['text'] = pop_2
    lb_hal_3['text'] = int(pz3)
    lb_hal_4['text'] = int(pz4)
    lb_hal_5['text'] = int(pz5)
    pop_log = np.array(pl)

    plt.plot(year, pop, '.-y', label='Aritmétrico')
    plt.plot(year, pop_geo, '--r', label='Geométrico')
    plt.plot(year, pop_log, 'c', label='Logístico')
    plt.plot(year, pop_ps, '-.k', label='Capidade de Suporte')
    plt.xlabel('Ano')
    plt.ylabel('População')
    plt.title('Métodos de Projeção Populacional - © Christian Farkas 2020')
    plt.legend()
    plt.show()


# Program #

janela.title('CAPTAÇÃO, ARMAZENAMENTO E TRATAMENTO DE ÁGUA')
janela["bg"] = "#7FFFD4"

lb = Label(janela, text='Este programa calcula a projeção populacional através dos métodos:'
                        ' Aritmético, Geométricos e Logístico.', bg="#7FFFD4")
lb.place(x=200, y=0)

lb1 = Label(janela, text="Entre com quantidade populacional no ano de 2000: ", bg="#7FFFD4")  # ano 2000
lb1.place(x=20, y=50)
ed = Entry()
ed.place(x=300, y=50)

lb2 = Label(janela, text="  ano 2010: ", bg="#7FFFD4")  # ano 2010
lb2.place(x=390, y=50)
ed1 = Entry()
ed1.place(x=450, y=50)

lb3 = Label(janela, text="  ano 2020: ", bg="#7FFFD4")  # ano 2020
lb3.place(x=550, y=50)
ed2 = Entry()
ed2.place(x=610, y=50)

bt = Button(janela, text="Gerar Gráfico", width=10, command=project, bg='#5F9EA0')  # Botão
bt.place(x=750, y=46)

lb4 = Label(janela, text="This program was developed by", bg="#7FFFD4")
lb4.place(x=350, y=260)
lb5 = Label(janela, text="© Christian Farkas 2020", bg="#7FFFD4")
lb5.place(x=370, y=280)

####################
# Table of Methods #
####################


lb_hab = Label(janela, text="|_Aritmético_|", bg="#7FFFD4")
lb_hab.place(x=20, y=100)
lb_hag = Label(janela, text="|Geométrico|", bg="#7FFFD4")
lb_hag.place(x=20, y=130)
lb_hal = Label(janela, text="|__Logístico_|", bg="#7FFFD4")
lb_hal.place(x=20, y=160)

lb_hab_0 = Label(janela, text="x", bg="#7FFFD4")
lb_hab_0.place(x=120, y=100)
lb_hab_1 = Label(janela, text="x", bg="#7FFFD4")
lb_hab_1.place(x=220, y=100)
lb_hab_2 = Label(janela, text="x", bg="#7FFFD4")
lb_hab_2.place(x=320, y=100)
lb_hab_3 = Label(janela, text="x", bg="#7FFFD4")
lb_hab_3.place(x=420, y=100)
lb_hab_4 = Label(janela, text="x", bg="#7FFFD4")
lb_hab_4.place(x=520, y=100)
lb_hab_5 = Label(janela, text="x", bg="#7FFFD4")
lb_hab_5.place(x=620, y=100)

lb_hag_0 = Label(janela, text="x", bg="#7FFFD4")
lb_hag_0.place(x=120, y=130)
lb_hag_1 = Label(janela, text="x", bg="#7FFFD4")
lb_hag_1.place(x=220, y=130)
lb_hag_2 = Label(janela, text="x", bg="#7FFFD4")
lb_hag_2.place(x=320, y=130)
lb_hag_3 = Label(janela, text="x", bg="#7FFFD4")
lb_hag_3.place(x=420, y=130)
lb_hag_4 = Label(janela, text="x", bg="#7FFFD4")
lb_hag_4.place(x=520, y=130)
lb_hag_5 = Label(janela, text="x", bg="#7FFFD4")
lb_hag_5.place(x=620, y=130)

lb_hal_0 = Label(janela, text="x", bg="#7FFFD4")
lb_hal_0.place(x=120, y=160)
lb_hal_1 = Label(janela, text="x", bg="#7FFFD4")
lb_hal_1.place(x=220, y=160)
lb_hal_2 = Label(janela, text="x", bg="#7FFFD4")
lb_hal_2.place(x=320, y=160)
lb_hal_3 = Label(janela, text="x", bg="#7FFFD4")
lb_hal_3.place(x=420, y=160)
lb_hal_4 = Label(janela, text="x", bg="#7FFFD4")
lb_hal_4.place(x=520, y=160)
lb_hal_5 = Label(janela, text="x", bg="#7FFFD4")
lb_hal_5.place(x=620, y=160)

ano1 = Label(janela, text="| 2000 |", bg="#7FFFD4")  # Table
ano1.place(x=120, y=80)
ano2 = Label(janela, text="| 2010 |", bg="#7FFFD4")  # Table
ano2.place(x=220, y=80)
ano3 = Label(janela, text="| 2020 |", bg="#7FFFD4")  # Table
ano3.place(x=320, y=80)
ano4 = Label(janela, text="| 2030 |", bg="#7FFFD4")  # Table
ano4.place(x=420, y=80)
ano5 = Label(janela, text="| 2040 |", bg="#7FFFD4")  # Table
ano5.place(x=520, y=80)
ano6 = Label(janela, text="| 2050 |", bg="#7FFFD4")  # Table
ano6.place(x=620, y=80)

janela.geometry("900x300+300+300")
janela.mainloop()
