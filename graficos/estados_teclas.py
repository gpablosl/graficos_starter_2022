#Comandos para librerías
#pip install pyopengl
#pip install glfw

#Importar librerias

from OpenGL.GL import *
from glew_wish import *
import glfw
import math


velocidad = 0.5
posicion = [0.2, -0.7, 0.0]
posicion_cuadrado = [0.0, 0.0, 0.0]
window = None

tiempo_anterior = 0.0

def actualizar():
    global tiempo_anterior
    global window
    global posicion
    global posicion_cuadrado

    tiempo_actual =  glfw.get_time()
    #Cuanto tiempo paso entre la ejecución actual y la inmediata anterior de esta función
    tiempo_delta = tiempo_actual - tiempo_anterior
    distancia = velocidad * tiempo_delta
    
    #leer estados
    estado_tecla_arriba = glfw.get_key(window, glfw.KEY_UP)
    estado_tecla_abajo = glfw.get_key(window, glfw.KEY_DOWN)
    estado_tecla_derecha = glfw.get_key(window, glfw.KEY_RIGHT)
    estado_tecla_izquierda = glfw.get_key(window, glfw.KEY_LEFT)

    estado_tecla_w = glfw.get_key(window, glfw.KEY_W)
    estado_tecla_s = glfw.get_key(window, glfw.KEY_S)
    estado_tecla_d = glfw.get_key(window, glfw.KEY_D)
    estado_tecla_a = glfw.get_key(window, glfw.KEY_A)

#revisar estados y realizamos acciones
    if estado_tecla_arriba == glfw.PRESS:
        posicion[1] = posicion[1] + distancia
    if estado_tecla_abajo == glfw.PRESS:
        posicion[1] = posicion[1] - distancia
    if estado_tecla_derecha == glfw.PRESS:
        posicion[0] = posicion[0] + distancia
    if estado_tecla_izquierda == glfw.PRESS:
        posicion[0] = posicion[0] - distancia

    if estado_tecla_w == glfw.PRESS:
        posicion_cuadrado[1] = posicion_cuadrado[1] + distancia
    if estado_tecla_s == glfw.PRESS:
        posicion_cuadrado[1] = posicion_cuadrado[1] - distancia
    if estado_tecla_d == glfw.PRESS:
        posicion_cuadrado[0] = posicion_cuadrado[0] + distancia
    if estado_tecla_a == glfw.PRESS:
        posicion_cuadrado[0] = posicion_cuadrado[0] - distancia

    #Determinar tiempo

    tiempo_anterior = tiempo_actual


def draw():
    global posicion
    glPushMatrix()
    glTranslatef(posicion[0], posicion[1],0.0)
    glBegin(GL_TRIANGLES)
    glColor3f(1,0,0)
    glVertex3f(-0.05,-0.05,0)
    glVertex3f(0.0,0.05,0)
    glVertex3f(0.05,-0.05,0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(posicion_cuadrado[0], posicion_cuadrado[1],0.0)
    glBegin(GL_QUADS)
    glColor3f(.5,0,1)
    glVertex3f(-0.05,0.05,0)
    glVertex3f(0.05,0.05,0)
    glVertex3f(0.05,-0.05,0)
    glVertex3f(-0.05,-0.05,0)
    glEnd()
    glPopMatrix()

def main():
    global window
    width = 700
    height = 700
    #Inicializar GLFW
    if not glfw.init():
        return

    #declarar ventana
    window = glfw.create_window(width, height, "Mi ventana", None, None)

    #Configuraciones de OpenGL
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    #Verificamos la creacion de la ventana
    if not window:
        glfw.terminate()
        return

    #Establecer el contexto
    glfw.make_context_current(window)

    #Le dice a GLEW que si usaremos el GPU
    glewExperimental = True

    #Inicializar glew
    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return

    #imprimir version
    version = glGetString(GL_VERSION)
    print(version)

    #Draw loop
    while not glfw.window_should_close(window):
        #Establecer el viewport
        #glViewport(0,0,width,height)
        #Establecer color de borrado
        glClearColor(0.7,0.7,0.7,1)
        #Borrar el contenido del viewport
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        actualizar()
        #Dibujar
        draw()


        #Polling de inputs
        glfw.poll_events()

        #Cambia los buffers
        glfw.swap_buffers(window)

    glfw.destroy_window(window)
    glfw.terminate()

if __name__ == "__main__":
    main()