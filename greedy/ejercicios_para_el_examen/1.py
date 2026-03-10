"""
Una empresa de tecnología tiene una lista de n trabajos que pueden realizarse en un único procesador. Cada trabajo i está asociado a:

Un tiempo límite (deadline): el trabajo debe completarse antes o en ese tiempo (1 unidad de tiempo por trabajo).
Una ganancia (profit): si el trabajo se completa dentro de su plazo, se obtiene esta ganancia; si no, la ganancia es 0.
El procesador solo puede realizar un trabajo por unidad de tiempo, y cada trabajo dura exactamente 1 unidad.

👉 El objetivo es seleccionar y ordenar los trabajos de manera que la ganancia total sea máxima.

Ejemplo
Entrada: Trabajos = [(J1, deadline=2, profit=100), (J2, deadline=1, profit=19), (J3, deadline=2, profit=27), (J4, deadline=1, profit=25), (J5, deadline=3, profit=15)]

Salida: Secuencia = [J1, J3, J5], Ganancia = 142

Explicación:

J1 se programa en la unidad de tiempo 2.
J3 se programa en la unidad de tiempo 1.
J5 se programa en la unidad de tiempo 3. Ganancia total = 100 + 27 + 15 = 142.
"""

def job_scheduling(jobs):
    
    # ordenar por ganancia descendente
    jobs.sort(key=lambda x: x[2], reverse=True)

    max_deadline = max(job[1] for job in jobs)

    slots = [None] * (max_deadline + 1)

    total_profit = 0
    seleccionados = []

    for job in jobs:
        name, deadline, profit = job

        for t in range(deadline, 0, -1):
            if slots[t] is None:
                slots[t] = name
                total_profit += profit
                seleccionados.append(name)
                break

    return seleccionados, total_profit

jobs = [
("J1",2,100),
("J2",1,19),
("J3",2,27),
("J4",1,25),
("J5",3,15)
]

print(job_scheduling(jobs))


def job_scheduling_deadline(jobs):

    # ordenar por deadline y luego por profit (mayor primero)
    jobs = sorted(jobs, key=lambda x: (x[1], -x[2]))

    trabajos_elegidos = []
    profit_total = 0
    deadlines_usados = set()

    for id_trabajo, deadline, profit in jobs:

        if deadline not in deadlines_usados:
            trabajos_elegidos.append(id_trabajo)
            profit_total += profit
            deadlines_usados.add(deadline)

    return trabajos_elegidos, profit_total

jobs = [
("J1",2,100),
("J2",1,19),
("J3",2,27),
("J4",1,25),
("J5",3,15)
]

print(job_scheduling_deadline(jobs))