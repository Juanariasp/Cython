import planetas_py
import planetas_cy
import time


time_span = 400
n_steps = 2000000

tierraCy = planetas_cy.Planet()
tierraCy.x= 100*10**3
tierraCy.y= 300*10**3
tierraCy.z= 700*10**3
tierraCy.vx= 2.00*10**3
tierraCy.vy= 29.87*10**3
tierraCy.vz= 0.037*10**3
tierraCy.m= 5.97424*10**3

planetas_cy.step_time_cy(tierraCy,1,1000000)

tierra = planetas_py.Planet()
tierra.x= 100*10**3
tierra.y= 300*10**3
tierra.z= 700*10**3
tierra.vx= 2.00*10**3
tierra.vy= 29.87*10**3
tierra.vz= 0.037*10**3
tierra.m= 5.97424*10**3

formato_datos = "{:0f},{:01f}\n"

for i in range(3):

    ini_time_PY = time.time()
    planetas_py.step_time_py(tierra,time_span,n_steps)
    fin_time_PY = time.time()

    ini_time_CY = time.time()
    planetas_cy.step_time_cy(tierraCy,time_span,n_steps)
    fin_time_CY = time.time()

    time_cython = fin_time_CY-ini_time_CY 
    time_python = fin_time_PY-ini_time_PY

    with open("planeta.csv","a") as archivo:
        archivo.write(formato_datos.format(time_python,time_cython))



print("Cython Time: ",time_cython)
print("Python Time: ",time_python)

print("Cython es: ",time_cython/time_python," mas rapido")