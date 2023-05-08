import plotly.graph_objs as go
import numpy as np

# Definir los datos de entrada para el hipercubo
datos = np.random.rand(100, 4)

# Definir los colores para las aristas del hipercubo
colores = ['red', 'green', 'blue', 'orange']

# Definir la figura de Plotly
fig = go.Figure()

# Agregar los nodos del hipercubo a la figura
for i in range(2**4):
    coords = []
    for j in range(4):
        coords.append((i >> j) & 1)
    fig.add_trace(go.Scatter3d(x=[coords[0]], y=[coords[1]], z=[coords[2]],
                            mode='markers', marker=dict(size=5, color=colores[coords[3]])))

# Definir la función de actualización de la figura
def actualizar_figura(datos):
    fig.data = []
    for i in range(2**4):
        coords = []
        for j in range(4):
            coords.append((i >> j) & 1)
        fig.add_trace(go.Scatter3d(x=[coords[0]], y=[coords[1]], z=[coords[2]],
                                mode='markers', marker=dict(size=5, color=colores[coords[3]])))
    tabla = go.Table(
        header=dict(values=['Nombre', 'Clase', 'Dimensión 1', 'Dimensión 2', 'Dimensión 3']),
        cells=dict(values=[['Dato {}'.format(i+1) for i in range(len(datos))],
                                ['Clase {}'.format(i+1) for i in range(len(datos))],
                                datos[:, 0], datos[:, 1], datos[:, 2]]))
    fig.add_trace(tabla)
    fig.update_layout(scene=dict(xaxis_title='Dimensión 1', yaxis_title='Dimensión 2', zaxis_title='Dimensión 3'),
                    title='Leyenda de Datos')
    
    return fig

# Actualizar la figura en un bucle
for i in range(len(datos)):
    fig_actualizada = actualizar_figura(datos[:i+1])
    fig_actualizada.show()
