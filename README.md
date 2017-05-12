# Graficador de GLPK

Recibe arhcivos con extensión `.mod`, de modelos en 2D, y grafica el poliedro de soluciones factibles, así como las rectas de restricciones. Si el modelo es en 3 dimensiones o más, lanza un error.

## Actualmente en desarrollo

- Parseo de una ecuación con "X1" o "X2" nombres de variables. Si hay otros nombres debería dar error.

## Features buscadas

- Selección de archivo de input por línea de comandos.
- Parseo de archivos de modelos. Una restricción por línea.
- Detección de variables. Regex?
- Generación de un modelo de restricciones.
- Graficado.
