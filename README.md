# 🐧 Clasificador de Pingüinos con Flask + AdaBoost + Docker

Este proyecto es una aplicación web desarrollada con Flask que permite predecir el sexo de un pingüino a partir de características físicas como la longitud y profundidad del pico, la longitud de la aleta y la masa corporal. El modelo de clasificación se ha entrenado utilizando **AdaBoost** con los datos balanceados mediante **SMOTE**, y ha sido guardado en un archivo `.pkl`.

## Repo  Github para ver el modelo de cluster y clasificación
- https://colab.research.google.com/drive/12EStdQl64hvilsOjBrDpspTpqB1tLgBc?usp=sharing

## 📦 Características del proyecto

- Modelo de clasificación entrenado con AdaBoost (`scikit-learn`)
- Interfaz web amigable y en español (con Bootstrap)
- Explicación de cada característica de entrada
- Estilo visual en modo oscuro
- Valores predeterminados en los formularios
- Implementación y despliegue en contenedores Docker

---

## 📊 Variables utilizadas

Las siguientes características del pingüino se utilizan como entrada del modelo:

| Variable               | Descripción |
|------------------------|-------------|
| `bill_length_mm`       | Longitud del pico en milímetros |
| `bill_depth_mm`        | Profundidad del pico en milímetros |
| `flipper_length_mm`    | Longitud de la aleta en milímetros |
| `body_mass_g`          | Masa corporal en gramos |

---

## 🚀 Cómo ejecutar el proyecto

### 1. Clona el repositorio

```bash
git clone https://github.com/tu_usuario/clasificador-pinguinos.git
cd clasificador-pinguinos

```bash
docker-compose up --build

🧑‍💻 Autor
Nombre: GHS

