# 🧬 Clasificador de Pokémon por Tipo y Clustering con KMeans + RandomForest

Este proyecto realiza análisis y clasificación de Pokémon utilizando técnicas de **Clustering** no supervisado con **KMeans** y un modelo de **clasificación supervisada con RandomForest**. Además, incorpora limpieza de datos, codificación de variables categóricas, visualizaciones de clusters y análisis de rendimiento del modelo.

## 📁 Dataset utilizado

El dataset contiene información de 809 Pokémon, incluyendo su tipo primario (`Type1`), tipo secundario (`Type2`) y su evolución.
Los datos fueron preprocesados para aplicar técnicas de aprendizaje automático.

Ejemplo de columnas usadas:

| Name       | Type1  | Type2   | Evolution |
|------------|--------|---------|-----------|
| bulbasaur  | Grass  | Poison  | ivysaur   |
| charmander | Fire   | NaN     | charmeleon|
| squirtle   | Water  | NaN     | wartortle |

---

## 🧠 Proceso de análisis

1. **Preprocesamiento:**
   - Se completaron valores faltantes en `Type2` con `"None"`.
   - Se aplicó One-Hot Encoding a `Type1` y `Type2`.
2. **Clustering con KMeans:**
   - Se determinó el número óptimo de clusters usando el método del codo.
   - Se asignaron etiquetas de cluster al dataset.
3. **Clasificación con RandomForest:**
   - El modelo fue entrenado para predecir el cluster usando los datos codificados.
   - Se "ensució" el 30% del conjunto de prueba reemplazando los valores por 0 para simular ruido en los datos.
4. **Evaluación:**
   - Se evaluó el modelo con clasificación y matriz de confusión.
   - Se graficaron los clusters en 2D con PCA.
   - Se construyó un gráfico de barras para mostrar la distribución de tipos (`Type1`) en cada cluster.

---

## 📊 Visualizaciones Generadas

- 📌 **Método del Codo** para encontrar el número óptimo de clusters.
- 🎯 **Scatter plot** de los Pokémon por cluster (usando PCA).
- 🔥 **Matriz de Confusión** visual con Seaborn.
- 📊 **Gráfico de barras** por tipo de Pokémon y su cluster correspondiente.

---

## 🛠 Librerías utilizadas

- `pandas`, `numpy`
- `matplotlib`, `seaborn`
- `scikit-learn` (`KMeans`, `RandomForestClassifier`, `train_test_split`, `PCA`)
- `pickle` para guardar el modelo

---

## 💾 Exportación del modelo

El modelo de clasificación fue exportado en formato `.pkl` para poder ser reutilizado fácilmente en otros entornos:

```python
import pickle
with open('modelo_clasificador.pkl', 'wb') as f:
    pickle.dump(clf, f)
```

---

## 🚀 Cómo ejecutar el análisis

1. Asegúrate de tener Python 3.x y las librerías necesarias (`pip install pandas scikit-learn seaborn matplotlib`)
2. Ejecuta el archivo Python con el análisis completo (`.ipynb` o `.py`)
3. Observa las gráficas generadas y el rendimiento del modelo en consola

---

## 📎 Enlace al proyecto (Google Colab)

👉 [Ver en Google Colab](https://colab.research.google.com/drive/19fRow6ncG6gn1QD3fCbz6R8QNvbY3SmZ?usp=sharing)

---

## 👤 Autor

**Nicolas :^)**
Clustering & Clasificación de Pokémon con Sklearn