import numpy as np
import matplotlib.pyplot as plt

# ==============================================================================
def Plot_Results(Prop):
    
    # Imprimiendo resultado de profundidad crítica en la pantalla
    print(r"Altura crítica yc para sección %s con un caudal de %4.2f m3/s es de:" \
          % (Prop["Shape"], Prop["Q"]))
    print('%5.2f m' % Prop["yc"])
    
    # Graficando altura de flujo (y) contra Energía Específica (E)
    fig = plt.figure(facecolor="white");
    
    # Vectores para recta identidad
    EYi = np.linspace(0, 10, 11)

            
    # Para reducir espacio (CAMBIAR DE ACUERDO CON NECESIDADES)
    Labels = [r"Energía específica $(m)$", \
              r"Recta Identidad", "Velocidad Teórica", 
             "Velocidad Real"]
    
    # Librería de colores
    Colors = ["darkmagenta","darkgreen","seagreen","dodgerblue","dimgrey"]
    FaceColors = ["lavenderblush","honeydew","mintcream","aliceblue","whitesmoke"]
    sc = 3 # Esto selecciona la paleta de colores
    width = 2.0 # Ancho de linea en graficas
    
    # Haciendo las gráficas por separado para que sea fácil poder cambiar
    # No necesito hacer ciclos porque son muy pocas. 
    # Gráfica de posiciones contra tiempo
    ax1 = plt.subplot(1, 1, 1)
    ax1.plot(Prop["E"], Prop["Y"], label = Labels[0], c = Colors[sc], lw = width, linestyle='-')
    ax1.plot(EYi, EYi, label = Labels[1], c = Colors[sc], lw = width, linestyle=':')
    ax1.set_ylim([0, 4])
    ax1.set_xlim([0, 5])
    ax1.set_facecolor(FaceColors[sc])
    ax1.set_title(r'$y(m)$ vs. $E(m)$', fontsize = 20)
    ax1.set_xlabel(r'Energía $(m)$', fontsize = 14)
    ax1.set_ylabel(r'Altura de flujo $y(m)$', fontsize = 14)
    ax1.grid(True)
 
    # Mostrando los resultados en el notebook
    plt.show()