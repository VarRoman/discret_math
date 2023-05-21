# edges_for_graph = [(0, 1, 7), (0, 3, 3), (1, 2, 5), (2, 3, 2), (2, 4, 3), (3, 1, 4), (4, 3, 5), (5, 2, 2),
#                    (5, 6, 8), (6, 2, 6), (5, 7, 2), (7, 6, 3), (1, 7, 4)]

# edges_for_graph = [(0, 1, 4), (0, 3, 1), (1, 2, 2), (2, 3, 6), (2, 4, 6), (3, 1, 6), (4, 3, 6), (5, 2, 3),
#                    (5, 6, 7), (6, 2, 4), (5, 7, 6), (7, 6, 1), (1, 7, 5)]

import networkx as nx
import matplotlib.pyplot as plt
from tkinter import *
from random import randint

I = 2102 % 10 + 1

G = nx.Graph()

def ran():
    return randint(0, 10)

edges_for_graph = [(0, 1, ran()), (0, 3, ran()), (1, 2, ran()), (2, 3, ran()), (2, 4, ran()), (3, 1, ran()),
    (4, 3, ran()), (5, 2, ran()), (5, 6, ran()), (6, 2, ran()), (5, 7, ran()), (7, 6, ran()), (1, 7, ran())]

numer = [i[0] for i in edges_for_graph]
edge_list = []
ribs_list = []
edge_list.extend(edges_for_graph)


def command_to_show():  # команда для проектування графа з визначеними порядками та вагою
    G.add_weighted_edges_from(edges_for_graph)
    pos = nx.circular_layout(G)
    nx.draw(G, pos, with_labels=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))
    plt.show()

    adjecity_matrix = [[0 for n in list(range(8))] for m in list(range(8))]  # матриця суміжності
    for i in edges_for_graph:
        adjecity_matrix[i[0]][i[1]] = 1
        adjecity_matrix[i[1]][i[0]] = 1
    Label(frame_3, text='Матриця\nсуміжності', font=('Arial', 10), width=9, bg='#D0C29C').grid(row=0, column=0)
    m = 1
    n = 1
    v = ['v', '0']
    w = ['v', '0']
    for a in adjecity_matrix:
        Label(frame_3, text=v[0] + v[1], font=('Arial', 10), bg='#D0C29C', width=9).grid(row=m, column=0)
        m += 1
        v[1] = str(int(v[1]) + 1)
        for b in list(range(8)):
            if n <= len(adjecity_matrix):
                Label(frame_3, text=w[0] + w[1], font=('Arial', 10), bg='#D0C29C',
                      width=3).grid(row=0, column=n)
                n += 1
                w[1] = str(int(w[1]) + 1)
            a_index = adjecity_matrix.index(a)
            Label(frame_3, text=adjecity_matrix[a_index][b], font=('Arial', 10), bg='#D0C29C',
                  width=3).grid(row=a_index + 1, column=b + 1)

def make_tree(value):
    check_list = []
    rib_to_add = edges_for_graph[numer.index(value)]

    for a in edges_for_graph:
        if a[0] == value or a[1] == value:
            if a[2] < rib_to_add[2]:
                rib_to_add = a
    ribs_list.append(rib_to_add)
    check_list.append(rib_to_add[0])
    check_list.append(rib_to_add[1])
    if rib_to_add in edge_list:
        edge_list.remove(rib_to_add)

    while len(ribs_list) != 7:
        checkout = []
        for i in edge_list:
            if i[0] in check_list or i[1] in check_list:
                ex = [i[0], i[1]]
                if len(set(ex) & set(check_list)) != 2:
                    checkout.append(i)
        rib_to_add = checkout[0]
        for i in checkout:
            if i[2] < rib_to_add[2]:
                rib_to_add = i

        ribs_list.append(rib_to_add)
        edge_list.remove(rib_to_add)
        if rib_to_add[0] not in check_list:
            check_list.append(rib_to_add[0])
        if rib_to_add[1] not in check_list:
            check_list.append(rib_to_add[1])

    G.clear_edges()
    G.add_weighted_edges_from(ribs_list)
    pos = nx.circular_layout(G)
    nx.draw(G, pos, with_labels=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))
    plt.show()


def save_func():
    with open('Список ребер', 'wt') as r:
        r.write(' '.join(map(str, list(ribs_list))))
        r.close()


def read_plurals():
    r = open('Список ребер', 'r')
    Label(win_1, font=('Arial', 12), width=40, text='(Перша вершина, друга вершина, вага)',
          bg='#E8E1C6', bd=5).pack(padx=10, pady=10)
    Label(win_1, font=('Arial', 12), width=70, text=r.read(), bd=5, bg='#E8E1C6').pack(padx=10, pady=10)
    r.close()

win_1 = Tk()
win_1.geometry(f"800x700+0+0")
win_1.title('Перше вікно')
win_1.resizable(False, False)

Label(win_1, text='Безщасний Роман Русланович', font=('Arial', 12, 'italic'), anchor='nw', padx=10, bg='#E8E1C6').pack()
Label(win_1, text='Група: ІО-21', font=('Arial', 12), bg='#E8E1C6').pack()
Label(win_1, text='Номер у списку: 2', font=('Arial', 12), bg='#E8E1C6').pack()
Label(win_1, text=f'Варіант №{I}', font=('Arial', 12), bg='#E8E1C6').pack()

frame_1 = Frame(win_1, bg='#E8E1C6', padx=5, pady=5, bd=10)
Label(frame_1, bg='#E8E1C6', text='Початкова вершина: ', font=('Arial', 12)).grid(row=0, column=0)

entry_1 = Entry(frame_1, font=('Arial', 12))
entry_1.grid(row=0, column=1)
frame_1.pack()

frame_2 = Frame(win_1, bg='#D0C29C', bd=10)
frame_2.pack()
Button(frame_2, text='Вигляд початкового графу', command=command_to_show, width=23,
       font=('Arial', 12)).grid(row=0, column=0, padx=5, pady=5)
Button(frame_2, text='Вигляд кінцевого графу', command=lambda: make_tree(int(entry_1.get())), width=23,
       font=('Arial', 12)).grid(row=0, column=1, padx=5, pady=5)
Button(frame_2, text='Зберегти у файл', command=save_func, width=23,
       font=('Arial', 12)).grid(row=1, column=0, padx=5, pady=5)
Button(frame_2, text='Зчитати з файлу', command=read_plurals, width=23,
       font=('Arial', 12)).grid(row=1, column=1, padx=5, pady=5)

frame_3 = Frame(win_1, bg='#D0C29C', bd=10)
frame_3.pack(padx=10, pady=10)

win_1.configure(bg='#E8E1C6')
win_1.mainloop()
