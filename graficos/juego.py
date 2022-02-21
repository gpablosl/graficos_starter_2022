from OpenGL.GL import *
from glew_wish import *
import glfw
import math

velocidad = 0.8
posicion_plr = [0.0, -0.8, 0.0]
posicion_bicho1 = [0.55, 0.55, 0.0]
posicion_bicho2 = [-0.55, -0.55, 0.0]
posicion_bicho3 = [0.55, -0.55, 0.0]
posicion_bicho4 = [-0.55, 0.55, 0.0]
posicion_boss = [0.0, 0.0, 0.0]
rotacion_boss = 0
velocidad_angular_boss = 0.5
direccion_boss = 1
plr_scale = [1.0,1.0,0.0]
window = None
tiempo_anterior = 0.0
angulo_triangulo = 0.0
fase = 90.0
velocidad_rotacion_triangulo = 90.0

def actualizar_boss(tiempo_delta):
    global direccion_boss
    global velocidad_angular_boss
    global rotacion_boss
    global angulo_triangulo

    cantidad_rotacion = velocidad_angular_boss * tiempo_delta
    rotacion_boss = rotacion_boss + cantidad_rotacion
    if rotacion_boss > 360.0:
        rotacion_boss = rotacion_boss - 360.0

    cantidad_movimiento = velocidad_angular_boss * tiempo_delta
    if direccion_boss == 0:
        posicion_boss[0] = posicion_boss[0] - cantidad_movimiento
    elif direccion_boss == 1:
        posicion_boss[0] = posicion_boss[0] + cantidad_movimiento
    if posicion_boss[0] <= -0.7 and direccion_boss == 0:
        direccion_boss = 1
    if posicion_boss[0] >= 0.7 and direccion_boss == 1:
        direccion_boss = 0
    
def actualizar():
    global tiempo_anterior
    global window
    global posicion_plr
    global posicion_bicho1, posicion_bicho2, posicion_bicho3, posicion_bicho4
    global posicion_boss

    tiempo_actual =  glfw.get_time()
    tiempo_delta = tiempo_actual - tiempo_anterior
    distancia = velocidad * tiempo_delta
    
    estado_tecla_w = glfw.get_key(window, glfw.KEY_W)
    estado_tecla_s = glfw.get_key(window, glfw.KEY_S)
    estado_tecla_d = glfw.get_key(window, glfw.KEY_D)
    estado_tecla_a = glfw.get_key(window, glfw.KEY_A)

    estado_tecla_ESC = glfw.get_key(window, glfw.KEY_ESCAPE)

    actualizar_boss(tiempo_delta)
    
    if estado_tecla_w == glfw.PRESS:
        posicion_plr[1] = posicion_plr[1] + distancia
        if posicion_plr[1] >= 0.9:
            posicion_plr[1] = -0.8999

    if estado_tecla_s == glfw.PRESS:
        posicion_plr[1] = posicion_plr[1] - distancia
        if posicion_plr[1] <= -0.9:
            posicion_plr[1] = 0.8999
    if estado_tecla_d == glfw.PRESS:
        posicion_plr[0] = posicion_plr[0] + distancia
        if posicion_plr[0] >= 0.9:
            posicion_plr[0] = -0.8999
    if estado_tecla_a == glfw.PRESS:
        posicion_plr[0] = posicion_plr[0] - distancia
        if posicion_plr[0] <= -0.9:
            posicion_plr[0] = 0.8999

    if estado_tecla_ESC == glfw.PRESS:
        glfw.set_window_should_close(window, 1)
    tiempo_anterior = tiempo_actual

def colisionando_bicho1():
    colisionando = False
    if (posicion_plr[0] + 0.05 >= posicion_bicho1[0] - 0.05 
    and posicion_plr[0] - 0.05 <= posicion_bicho1[0] + 0.05 
    and posicion_plr[1] + 0.05 >= posicion_bicho1[1] - 0.05 
    and posicion_plr[1] -0.05 <= posicion_bicho1[1] + 0.05):
        colisionando = True
    return colisionando

def colisionando_bicho2():
    colisionando = False
    if (posicion_plr[0] + 0.05 >= posicion_bicho2[0] - 0.05 
    and posicion_plr[0] - 0.05 <= posicion_bicho2[0] + 0.05 
    and posicion_plr[1] + 0.05 >= posicion_bicho2[1] - 0.05 
    and posicion_plr[1] -0.05 <= posicion_bicho2[1] + 0.05):
        colisionando = True
    return colisionando

def colisionando_bicho3():
    colisionando = False
    if (posicion_plr[0] + 0.05 >= posicion_bicho3[0] - 0.05 
    and posicion_plr[0] - 0.05 <= posicion_bicho3[0] + 0.05 
    and posicion_plr[1] + 0.05 >= posicion_bicho3[1] - 0.05 
    and posicion_plr[1] -0.05 <= posicion_bicho3[1] + 0.05):
        colisionando = True
    return colisionando

def colisionando_bicho4():
    colisionando = False
    if (posicion_plr[0] + 0.05 >= posicion_bicho4[0] - 0.05 
    and posicion_plr[0] - 0.05 <= posicion_bicho4[0] + 0.05 
    and posicion_plr[1] + 0.05 >= posicion_bicho4[1] - 0.05 
    and posicion_plr[1] -0.05 <= posicion_bicho4[1] + 0.05):
        colisionando = True
    return colisionando

def colisionando_boss():
    colisionando = False
    if (posicion_plr[0] + 0.05 >= posicion_boss[0] - 0.05 
        and posicion_plr[0] - 0.05 <= posicion_boss[0] + 0.05 
        and posicion_plr[1] + 0.05 >= posicion_boss[1] - 0.05 
        and posicion_plr[1] - 0.05 <= posicion_boss[1] + 0.05):
        colisionando = True 
    return colisionando


def draw_plr():
    global posicion_plr
    global posicion_bicho1
    global posicion_bicho2
    global posicion_bicho3
    global posicion_bicho4
    global posicion_boss
    global velocidad
    global plr_scale
    glPushMatrix()
    glTranslatef(posicion_plr[0], posicion_plr[1],0.0)
    glScalef(plr_scale[0],plr_scale[1],0.0)
    glBegin(GL_TRIANGLES)


    if colisionando_bicho1():
            posicion_bicho1 = [1.5,1.5,0]
    if colisionando_bicho2():
            posicion_bicho2 = [1.5,1.5,0]
    if colisionando_bicho3():
            posicion_bicho3 = [1.5,1.5,0]
    if colisionando_bicho4():
            posicion_bicho4 = [1.5,1.5,0]
    if colisionando_boss():
            posicion_boss = [0.0,2.0,0]
            velocidad = 0.3
            plr_scale = [0.5,0.5,0.0]

    else:
        glColor3f(1,0,0)
    glVertex3f(-0.05,-0.05,0)
    glVertex3f(0.0,0.05,0)
    glVertex3f(0.05,-0.05,0)
    glEnd()
    glPopMatrix()

def draw_boss():
    global posicion_boss
    glPushMatrix()
    glTranslatef(posicion_boss[0], posicion_boss[1], 0.0)
    glRotatef(rotacion_boss,0.0,0.0,1.0)
    glScalef(3,3,0)
    glBegin(GL_POLYGON)
    glColor3f(0.5, 0.1, 0.4)
    glVertex3f(-0.01,0.01,0.0)
    glVertex3f(0.00,0.01,0.0)
    glVertex3f(0.01,-0.00,0.0)
    glVertex3f(0.01,-0.01,0.0)
    glVertex3f(0.0,-0.02,0.0)
    glVertex3f(-0.01,-0.02,0.0)
    glVertex3f(-0.02,-0.01,0.0)
    glVertex3f(-0.02,-0.00,0.0)
    glEnd()
    glPopMatrix()

def draw_bichos():
    global posicion_bicho1, posicion_bicho2, posicion_bicho3, posicion_bicho4
    #bicho 1
    glPushMatrix()
    glTranslatef(posicion_bicho1[0], posicion_bicho1[1],0.0)
    glRotatef(-90,0,0,1)
    glScalef(2,2,0)
    glBegin(GL_POLYGON)
    glColor3f(.3,0.2,.46)
    glVertex3f(-0.02,0.01,0)
    glVertex3f(-0.01,0.0,0)
    glVertex3f(-0.02,-0.01,0)
    glVertex3f(-0.0,-0.03,0)
    glVertex3f(0.02,-0.01,0)
    glVertex3f(0.01,0.00,0)
    glVertex3f(0.02,0.01,0)
    glVertex3f(0.00,0.03,0)
    glEnd()
    glPopMatrix()
    #bicho 2
    glPushMatrix()
    glTranslatef(posicion_bicho2[0], posicion_bicho2[1],0.0)
    glRotatef(90,0,0,1)
    glScalef(2,2,0)
    glBegin(GL_POLYGON)
    glColor3f(.55,0.26,.40)
    glVertex3f(-0.02,0.01,0)
    glVertex3f(-0.01,0.0,0)
    glVertex3f(-0.02,-0.01,0)
    glVertex3f(-0.0,-0.03,0)
    glVertex3f(0.02,-0.01,0)
    glVertex3f(0.01,0.00,0)
    glVertex3f(0.02,0.01,0)
    glVertex3f(0.00,0.03,0)
    glEnd()
    glPopMatrix()
    #bicho 3
    glPushMatrix()
    glTranslatef(posicion_bicho3[0], posicion_bicho3[1],0.0)
    glRotatef(90,0,0,1)
    glScalef(2,2,0)
    glBegin(GL_POLYGON)
    glColor3f(.75,0.18,.38)
    glVertex3f(-0.02,0.01,0)
    glVertex3f(-0.01,0.0,0)
    glVertex3f(-0.02,-0.01,0)
    glVertex3f(-0.0,-0.03,0)
    glVertex3f(0.02,-0.01,0)
    glVertex3f(0.01,0.00,0)
    glVertex3f(0.02,0.01,0)
    glVertex3f(0.00,0.03,0)
    glEnd()
    glPopMatrix()
    #bicho 4
    glPushMatrix()
    glTranslatef(posicion_bicho4[0], posicion_bicho4[1],0.0)
    glRotatef(-90,0,0,1)
    glScalef(2,2,0)
    glBegin(GL_POLYGON)
    glColor3f(.86,0.36,.55)
    glVertex3f(-0.02,0.01,0)
    glVertex3f(-0.01,0.0,0)
    glVertex3f(-0.02,-0.01,0)
    glVertex3f(-0.0,-0.03,0)
    glVertex3f(0.02,-0.01,0)
    glVertex3f(0.01,0.00,0)
    glVertex3f(0.02,0.01,0)
    glVertex3f(0.00,0.03,0)
    glEnd()
    glPopMatrix()

def draw_walls():
    glBegin(GL_LINE_LOOP)
    glColor3f(0.0,0.0,0.0)
    glVertex3f(-0.9,-0.9,0.0)
    glVertex3f(0.9,-0.9,0.0)
    glVertex3f(0.9,0.9,0.0)
    glVertex3f(-0.9, 0.9,0.0)
    glVertex3f(-0.9,-0.9,0.0)
    glEnd()
    #wall 1
    glBegin(GL_QUADS)
    glColor3f(0.4,0.65,0.15)
    glVertex3f(-1,-1,0)
    glVertex3f(-1,1,0)
    glVertex3f(-0.9,1,0)
    glVertex3f(-0.9, -1,0.0)
    glEnd()
    #wall 2
    glBegin(GL_QUADS)
    glColor3f(0.28,0.7,0.17)
    glVertex3f(-1,1,0)
    glVertex3f(-1,0.9,0)
    glVertex3f(1,0.9,0)
    glVertex3f(1,1,0.0)
    glEnd()
    #wall 3
    glBegin(GL_QUADS)
    glColor3f(0.42,0.65,0.22)
    glVertex3f(-1,-1,0)
    glVertex3f(-1,-0.9,0)
    glVertex3f(1,-0.9,0)
    glVertex3f(1,-1,0.0)
    glEnd()
    #wall 4
    glBegin(GL_QUADS)
    glColor3f(0.28,0.5,0.17)
    glVertex3f(1,-1,0)
    glVertex3f(1,1,0)
    glVertex3f(0.9,1,0)
    glVertex3f(0.9, -1,0.0)
    glEnd()

def decos():
    glBegin(GL_QUADS)
    glColor3f(0.34,0.7,0.342)
    glVertex3f(0.56,0.56,0)
    glVertex3f(0.56,0.21,0)
    glVertex3f(0.21, 0.21,.0)
    glVertex3f(0.21,0.56,0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.25,0.5,0.22)
    glVertex3f(-0.36,-0.36,0)
    glVertex3f(-0.36,-.11,0)
    glVertex3f(-0.11, -0.11,.0)
    glVertex3f(-0.11,-0.36,0)
    glEnd()


    glBegin(GL_TRIANGLES)
    glColor3f(0.27,0.68,0.22)
    glVertex3f(-0.85, -0.74,.0)
    glVertex3f(-0.66,-.80,0)
    glVertex3f(-0.76,-0.87,0)
    glEnd()

def draw():
    decos()
    draw_plr()
    draw_walls()
    draw_boss()
    draw_bichos()

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
        glClearColor(0.22,0.58,0.2,1)
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
