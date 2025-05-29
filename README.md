# Proyecto-Final
# Sistema de Gestión de Comedores Comunitarios

## Descripción del Proyecto

Este sistema permite gestionar comedores comunitarios, incluyendo el manejo de inventarios de alimentos, registro de beneficiarios y distribución de comida. El proyecto está desarrollado siguiendo el patrón de arquitectura MVC (Modelo-Vista-Controlador) para garantizar una separación clara de responsabilidades.

## Características Principales

- **Gestión de Comedores**: Administración de 15 comedores comunitarios ubicados en diferentes zonas de Bogotá
- **Control de Inventario**: Seguimiento de alimentos por categorías (cereales, proteínas, verduras, frutas, bebidas)
- **Registro de Beneficiarios**: Sistema de inscripción con evaluación de vulnerabilidad
- **Distribución de Alimentos**: Cálculo automático de platos disponibles y distribución
- **Sistema de Puntajes**: Evaluación de vulnerabilidad para determinar elegibilidad

## Estructura del Proyecto

```
proyecto_comedores/
├── main.py              # Punto de entrada del programa
├── models.py            # Modelos de datos (Comedor, Alimentos, Beneficiario)
├── views.py             # Interfaz de usuario y presentación
├── controllers.py       # Lógica de control y coordinación
├── README.md           # Documentación del proyecto
└── docs/               # Documentación técnica y diagramas
    ├── diagrama_clases.md
    ├── diagrama_casos_uso.md
    └── arquitectura_mvc.md
```

## Instalación y Uso

### Requisitos del Sistema
- Python 3.7 o superior
- No requiere librerías externas adicionales

### Instalación
1. Clona o descarga el proyecto
2. Navega al directorio del proyecto
3. Ejecuta el programa principal:

```bash
python main.py
```

### Uso del Sistema

1. **Selección de Comedor**: Al iniciar, selecciona el comedor donde deseas trabajar
2. **Menú Principal**: Accede a las siguientes opciones:
   - Inventario de Comida
   - Entrega de Comida
   - Repartir comida
   - Beneficiarios inscritos
   - Añadir beneficiario
   - Retirar Beneficiario

## Funcionalidades Detalladas

### Gestión de Inventario
- Visualización de stock actual por categoría de alimento
- Cálculo automático de platos disponibles
- Simulación de entregas de alimentos

### Sistema de Beneficiarios
- Registro con datos personales completos
- Evaluación de vulnerabilidad basada en:
  - Número de comidas diarias
  - Ingresos económicos
  - Personas a cargo
  - Tipo de vivienda
  - Condiciones especiales (discapacidad, desplazamiento, menores a cargo)

### Criterios de Elegibilidad
Un beneficiario es apto si obtiene un puntaje de vulnerabilidad ≥ 15 puntos:
- **Comidas diarias**: 1 comida (5 pts), 2 comidas (3 pts), 3 comidas (0 pts)
- **Ingresos**: <$200,000 per cápita (5 pts), $200,000-$300,000 (3 pts), >$300,000 (0 pts)
- **Discapacidad**: Sí (5 pts), No (0 pts)
- **Vivienda**: Calle (5 pts), Arriendo (3 pts), Propia (0 pts)
- **Desplazamiento**: Sí (5 pts)
- **Menores a cargo**: Sí (5 pts)

## Comedores Disponibles

El sistema incluye 15 comedores comunitarios:

1. **Los Luceros** - Cra 17F No. 69A-32 Sur (Capacidad: 250)
2. **Potosí** - Calle 81 Sur No. 42-09 (Capacidad: 230)
3. **Caracolí** - Calle 76A Sur No. 74B-05 (Capacidad: 220)
4. **La Estrella** - Cra 18 No. 74A Sur-87 (Capacidad: 240)
5. **Bella Flor - La Torre** - Cra 27 No. 75A-50 Sur (Capacidad: 230)
6. **Altos de la Cruz** - Transv 22 No. 69K-19 Sur (Capacidad: 225)
7. **Juan Pablo II** - Diag 68B Sur No. 18P-40 (Capacidad: 220)
8. **Naciones Unidas** - Cra 18R No. 77A Sur-27 (Capacidad: 235)
9. **Jerusalén Canteras** - Cra 47D No. 68G-08 Sur (Capacidad: 250)
10. **Estrella del Sur** - Calle 74 No. 18 Bis-18 (Capacidad: 230)
11. **Santa Viviana** - Calle 75D Sur No. 75C-03 Sur (Capacidad: 220)
12. **Arborizadora** - Cra 40 No. 63I-25 Sur (Capacidad: 230)
13. **Perdomo** - Av. Villavicencio No. 60B-05 Sur (Capacidad: 240)
14. **El Tesoro** - Cra 18F No. 76 Sur (Capacidad: 225)
15. **Vista Hermosa** - Calle 80B Sur No. 44-10 (Capacidad: 230)

## Arquitectura del Sistema

### Patrón MVC

**Modelo (models.py):**
- `Comedor`: Representa un comedor comunitario
- `Alimentos`: Maneja el inventario y distribución de alimentos
- `Beneficiario`: Gestiona datos y evaluación de beneficiarios
- `ComedorComunitario`: Clase principal que integra todos los componentes

**Vista (views.py):**
- `ComedorView`: Maneja toda la interacción con el usuario
- Presentación de menús y formularios
- Validación de entrada de datos

**Controlador (controllers.py):**
- `ComedorController`: Coordina la lógica de negocio
- Procesamiento de datos
- Flujo de control de la aplicación

## Ejemplos de Uso

### Agregar un Beneficiario
```
1. Seleccionar comedor
2. Elegir opción "Añadir beneficiario"
3. Ingresar datos personales
4. Completar evaluación de vulnerabilidad
5. El sistema determina automáticamente la elegibilidad
```

### Repartir Comida
```
1. Seleccionar comedor
2. Elegir opción "Repartir comida"
3. El sistema calcula automáticamente las porciones disponibles
4. Distribuye según el número de beneficiarios registrados
```

## Contribución

Para contribuir al proyecto:
1. Fork el repositorio
2. Crea una rama para tu feature
3. Realiza tus cambios
4. Envía un pull request

## Licencia

Este proyecto está desarrollado con fines educativos y de apoyo social comunitario.

## Contacto

Para dudas o sugerencias sobre el sistema, contacta al equipo de desarrollo.

---

*Sistema de Gestión de Comedores Comunitarios - Versión 1.0*
