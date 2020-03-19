import Box
import Pyramid
import Sphere

shape = input("Choose which shape you want to calculate: Box, Sphere, or Pyramid ")

if shape == 'Box':
  l = int(input("Type the Length of your Box "))
  w = int(input("Type the Width of your Box "))
  h = int(input("Type the Height of your Box "))
  b = Box.Box(l,w,h)
  print('This is the Surface Area of your Box | ', b.getSurfaceArea())
  print('This is the Volume of your Box | ', b.getVolume())
elif shape == 'Pyramid':
  l = int(input("Type the Length of your Pyramid "))
  w = int(input("Type the Width of your Pyramid "))
  h = int(input("Type the Height of your Pyramid "))
  p = Pyramid.Pyramid(l,w,h)
  print('This is the Surface Area of your Pyramid | ', p.getSurfaceArea())
  print('This is the Volume of your Pyramid | ', p.getVolume())
elif shape == 'Sphere':
  r = int(input("Type the Radius of your Sphere "))
  s = Sphere.Sphere(r)
  print('This is the Surface Area of your Sphere | ', s.getSurfaceArea())
  print('This is the Volume of your Sphere | ', s.getVolume())
