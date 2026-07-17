import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Portafolio de Python", page_icon="🐍", layout="wide")

# Menú de navegación lateral obligatorio
opcion = st.sidebar.selectbox(
    "Navegación",
    ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"]
)

# ==========================================
# SECCIÓN: HOME
# ==========================================
if opcion == "Home":
    # Título del proyecto
    st.title("🚀 Desarrollo de Aplicaciones Interactivas con Streamlit")
    st.subheader("Portafolio Profesional de Competencias en Python")
    st.divider()

    # Layout de dos columnas: Logo / Identificación | Información del Proyecto
    col_Firma, col_Info = st.columns([1, 2], gap="large")

    with col_Firma:
        # Verificación segura de la existencia de la imagen
        import os
        
        ruta_logo = "logo.png"
        if os.path.exists(ruta_logo):
            st.image(ruta_logo, width=250, caption="Python DMC - Proyecto Base")
        else:
            # Alternativa visual limpia si el archivo aún no está en la carpeta
            st.markdown("### 🐍 [Logo Representativo]")
            st.caption("(Sugerencia: Coloca una imagen llamada 'logo.png' en la raíz del proyecto)")

        
        st.divider()
        
        # Datos del Estudiante e Información General
        st.markdown("### 👤 Datos del Estudiante")
        st.write("**Nombre Completo:** [Tu Nombre y Apellidos Completos]")
        st.write("**Módulo:** Fundamentos Avanzados de Python")
        st.write("**Especialidad/Rol:** Desarrollador de Software / Analista de Datos")
        st.write("**Año:** 2026")

    with col_Info:
        # Breve descripción del proyecto
        st.markdown("### 📝 Descripción del Proyecto")
        st.write(
            "Este proyecto consiste en una aplicación web interactiva diseñada para centralizar, "
            "ejecutar y validar de forma práctica los pilares fundamentales del lenguaje Python. "
            "A través de una arquitectura limpia y modular, el portafolio actúa como evidencia "
            "de ingeniería de software, permitiendo al usuario interactuar en tiempo real con "
            "algoritmos complejos, manipulación de datos y metodologías de programación avanzadas."
        )
        
        # Tecnologías utilizadas
        st.markdown("### 🛠️ Tecnologías Utilizadas")
        st.markdown("""
        * **Lenguaje Core:** Python 3.x
        * **Framework de Interfaz:** Streamlit (UI Reactiva)
        * **Estructuración:** Programación Estructurada, Funcional y Orientada a Objetos (POO)
        """)
        
        # Cuadro de instrucciones generales
        st.info(
            "💡 **Guía de navegación:** Despliega el menú de la barra lateral izquierda "
            "(`st.sidebar.selectbox`) para interactuar con los ejercicios del 1 al 4 "
            "y evaluar los conceptos técnicos implementados."
        )

    st.divider()


# ==========================================
# SECCIÓN: EJERCICIO 1
# ==========================================
elif opcion == "Ejercicio 1":
    st.title("📝 Ejercicio 1")
    st.info("Esperando pautas para el desarrollo de esta sección...")

# ==========================================
# SECCIÓN: EJERCICIO 2
# ==========================================
elif opcion == "Ejercicio 2":
    st.title("📊 Ejercicio 2")
    st.info("Esperando pautas para el desarrollo de esta sección...")

# ==========================================
# SECCIÓN: EJERCICIO 3
# ==========================================
elif opcion == "Ejercicio 3":
    st.title("⚙️ Ejercicio 3")
    st.info("Esperando pautas para el desarrollo de esta sección...")

# ==========================================
# SECCIÓN: EJERCICIO 4
# ==========================================
elif opcion == "Ejercicio 4":
    st.title("🛠️ Ejercicio 4")
    st.info("Esperando pautas para el desarrollo de esta sección...")
