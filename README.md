# Diseño Hidrodinámico de Redes de Acuicultura
### Optimización de Modelos Hidrodinámicos para Redes de Acuicultura
*Giamportone, Ariel Lujan* 
*ALG Data&Engineering Solutions*

## Introducción
Este proyecto busca optimizar los modelos hidrodinámicos para redes de acuicultura mediante técnicas de ciencia de datos. La idea es utilizar datos generados sintéticamente para entrenar y evaluar un modelo predictivo que pueda estimar las fuerzas hidrodinámicas sobre diferentes tipos de redes de acuicultura bajo diversas condiciones de flujo.

## Objetivo del Proyecto
Desarrollar un modelo predictivo que estime con precisión las fuerzas hidrodinámicas sobre las redes de acuicultura utilizando datos sintéticos generados con la librería Faker.

## Metodología
1. Generación de Datos Sintéticos
2. Preprocesamiento de Datos
3. Análisis Exploratorio de Datos (EDA)
4. Desarrollo del Modelo
5. Optimización del Modelo
6. Implementación y Visualización



## Funcionalidades del Dashboard
Para mayor divulgación se realizarón dos versiones del dashboard. La primera en el registro del notebook de jupyter con Dash, y una segunda para el deploy en Straemlit.

**"Predicción de Fuerzas Hidrodinámicas en Redes de Acuicultura".**
 Un gráfico de dispersión que muestra la relación entre la velocidad de la corriente y la fuerza hidrodinámica, con la posibilidad de filtrar los datos según el ángulo de entrada.

**Componentes Interactivos:**

Gráfico de Dispersión (Scatter Plot): Muestra los datos con las siguientes características:

- Eje X: Velocidad de la corriente (en m/s).
- Eje Y: Fuerza hidrodinámica (en N).
- Colores: Representan la solidez de la red.
- Tamaño de los puntos: Representa el diámetro del hilo.
- Nombre al pasar el ratón: Muestra el ángulo de entrada.
- Slider de Ángulo (Angle Slider): Permite filtrar los datos mostrados en el gráfico de dispersión según el ángulo de entrada de la corriente. El slider va desde 0° hasta 90°.

Al interactuar con el gráfico, los usuarios pueden obtener varias conclusiones importantes basadas en los estudios hidrodinámicos y las relaciones exploradas en el artículo. Algunas de las conclusiones clave podrían ser:

1. Relación entre Velocidad de la Corriente y Fuerza Hidrodinámica
Conclusión: A medida que la velocidad de la corriente aumenta, la fuerza hidrodinámica sobre la red de acuicultura también incrementa. Esta relación es crucial para diseñar redes que puedan soportar diferentes velocidades de corriente, garantizando la integridad estructural y la seguridad del cultivo acuícola.

2. Impacto de la Solidez de la Red
Conclusión: La solidez de la red tiene un impacto significativo en la fuerza hidrodinámica. Redes con mayor solidez (mayor coeficiente de resistencia) tienden a experimentar mayores fuerzas hidrodinámicas para la misma velocidad de corriente. Esto indica que el diseño óptimo de la red debe balancear la solidez con la capacidad de soportar fuerzas hidrodinámicas, optimizando tanto la protección de los peces como la durabilidad de la red.

3. Influencia del Diámetro del Hilo
Conclusión: El diámetro del hilo también afecta la fuerza hidrodinámica. Hilos más gruesos generan una mayor resistencia al flujo de agua, resultando en mayores fuerzas hidrodinámicas. Este aspecto debe ser considerado al seleccionar el material y diseño del hilo para las redes, asegurando que puedan manejar las condiciones hidrodinámicas esperadas sin comprometer la estabilidad estructural.

4. Efecto del Ángulo de Entrada
Conclusión: El ángulo de entrada del flujo de agua respecto a la red influye en la fuerza hidrodinámica. Diferentes ángulos pueden cambiar la distribución de la fuerza en la red, y los datos interpolados permiten a los diseñadores entender mejor cómo se comportan las fuerzas hidrodinámicas en ángulos no directamente medidos. Esto es esencial para diseñar redes que puedan adaptarse a una variedad de condiciones de flujo en un entorno real.

Implicaciones Prácticas
Diseño Optimizado de Redes: Los ingenieros pesqueros pueden utilizar estos insights para diseñar redes de acuicultura que maximicen la resistencia a fuerzas hidrodinámicas mientras minimizan el estrés en los materiales.
Selección de Materiales: La selección de materiales adecuados para las redes, en términos de solidez y diámetro del hilo, puede ser optimizada para diferentes condiciones ambientales.
Implementación de Ángulos de Instalación: Comprender cómo los diferentes ángulos de entrada afectan la fuerza puede influir en la orientación y colocación de las redes en el entorno acuático, mejorando la eficiencia y seguridad de las operaciones de acuicultura.
Conclusión General
Conclusión General: El análisis hidrodinámico es fundamental para el diseño eficiente y seguro de redes de acuicultura. Los modelos matemáticos y gráficos interactivos proporcionan a los ingenieros pesqueros herramientas valiosas para tomar decisiones informadas sobre el diseño y la implementación de redes, mejorando así la sostenibilidad y rentabilidad de las operaciones acuícolas.Al interactuar con el gráfico, los usuarios pueden obtener varias conclusiones importantes basadas en los estudios hidrodinámicos y las relaciones exploradas en el artículo. Algunas de las conclusiones clave podrían ser:

1. Relación entre Velocidad de la Corriente y Fuerza Hidrodinámica
Conclusión: A medida que la velocidad de la corriente aumenta, la fuerza hidrodinámica sobre la red de acuicultura también incrementa. Esta relación es crucial para diseñar redes que puedan soportar diferentes velocidades de corriente, garantizando la integridad estructural y la seguridad del cultivo acuícola.

2. Impacto de la Solidez de la Red
Conclusión: La solidez de la red tiene un impacto significativo en la fuerza hidrodinámica. Redes con mayor solidez (mayor coeficiente de resistencia) tienden a experimentar mayores fuerzas hidrodinámicas para la misma velocidad de corriente. Esto indica que el diseño óptimo de la red debe balancear la solidez con la capacidad de soportar fuerzas hidrodinámicas, optimizando tanto la protección de los peces como la durabilidad de la red.

3. Influencia del Diámetro del Hilo
Conclusión: El diámetro del hilo también afecta la fuerza hidrodinámica. Hilos más gruesos generan una mayor resistencia al flujo de agua, resultando en mayores fuerzas hidrodinámicas. Este aspecto debe ser considerado al seleccionar el material y diseño del hilo para las redes, asegurando que puedan manejar las condiciones hidrodinámicas esperadas sin comprometer la estabilidad estructural.

4. Efecto del Ángulo de Entrada
Conclusión: El ángulo de entrada del flujo de agua respecto a la red influye en la fuerza hidrodinámica. Diferentes ángulos pueden cambiar la distribución de la fuerza en la red, y los datos interpolados permiten a los diseñadores entender mejor cómo se comportan las fuerzas hidrodinámicas en ángulos no directamente medidos. Esto es esencial para diseñar redes que puedan adaptarse a una variedad de condiciones de flujo en un entorno real.

## Implicaciones Prácticas
**Diseño Optimizado de Redes**: Los ingenieros pesqueros pueden utilizar estos insights para diseñar redes de acuicultura que maximicen la resistencia a fuerzas hidrodinámicas mientras minimizan el estrés en los materiales.
**Selección de Materiales**: La selección de materiales adecuados para las redes, en términos de solidez y diámetro del hilo, puede ser optimizada para diferentes condiciones ambientales.
**Implementación de Ángulos de Instalación**: Comprender cómo los diferentes ángulos de entrada afectan la fuerza puede influir en la orientación y colocación de las redes en el entorno acuático, mejorando la eficiencia y seguridad de las operaciones de acuicultura.
**Conclusión General**: El análisis hidrodinámico es fundamental para el diseño eficiente y seguro de redes de acuicultura. Los modelos matemáticos y gráficos interactivos proporcionan a los ingenieros pesqueros herramientas valiosas para tomar decisiones informadas sobre el diseño y la implementación de redes, mejorando así la sostenibilidad y rentabilidad de las operaciones acuícolas.