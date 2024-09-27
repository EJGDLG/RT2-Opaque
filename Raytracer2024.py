import pygame
from pygame.locals import *
from gl import RendererRT
from figure import *
from material import *
from lights import *
from texture import Texture

width = 400
height = 400

screen = pygame.display.set_mode((width, height), pygame.SCALED)
clock = pygame.time.Clock()

rt = RendererRT(screen)
rt.envMap = Texture("c:/Users/DeLeon/Desktop/TR2/Raytracer2024/Raytracer2024/lonemonk.bmp")

# Materiales
texture1  = Material(texture=Texture("c:/Users/DeLeon/Desktop/TR2/Raytracer2024/Raytracer2024/Texture1.bmp"))
texture2  = Material(texture=Texture("c:/Users/DeLeon/Desktop/TR2/Raytracer2024/Raytracer2024/Texture2.bmp"), spec=128, ks=0.8, matType=REFLECTIVE)

Lock1  = Material(texture=Texture("c:/Users/DeLeon/Desktop/TR2/Raytracer2024/Raytracer2024/Lock1.bmp"))
Lock2  = Material(texture=Texture("c:/Users/DeLeon/Desktop/TR2/Raytracer2024/Raytracer2024/Lock2.bmp"), spec=64, ks=0.1, matType=REFLECTIVE)

mirror = Material(diffuse=[0.2, 0.9, 0.2], spec=128, ks=0.2, matType=TRANSPARENT)
blueMirror = Material(diffuse=[0.9, 0.2, 0.9], spec=128, ks=0.2, matType=TRANSPARENT)


# Luces
rt.light.append(DirectionalLight(direction=[-1, -1, -1], intensity=0.8))
rt.light.append(DirectionalLight(direction=[0.5, -0.5, -1], intensity=0.8, color=[1, 1, 1]))
rt.light.append(AmbientLight(intensity=0.1))

# Esferas
rt.scene.append(Sphere(position=[-3.5, 2, -10], radius=1, material=Lock1))
rt.scene.append(Sphere(position=[3, 2, -10], radius=1, material=texture1))
rt.scene.append(Sphere(position=[-0.3, 2, -10], radius=1, material=mirror))

rt.scene.append(Sphere(position=[-3.5, -1, -10], radius=1, material=Lock2))
rt.scene.append(Sphere(position=[3, -1, -10], radius=1, material=texture2))
rt.scene.append(Sphere(position=[-0.3, -1, -10], radius=1, material=blueMirror))

# Renderizar la escena
rt.glRender()

# Guardar la imagen como output.bmp
pygame.image.save(screen, "output.bmp")

isRunning = True
while isRunning:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
