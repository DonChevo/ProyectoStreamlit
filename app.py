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
    st.title("👋 Bienvenido a mi Portafolio Interactivos de Python")
    st.write("Esta aplicación interactiva sirve como evidencia de conceptos fundamentales de programación.")
    st.write("Utiliza el menú de la izquierda para explorar los diferentes ejercicios prácticos desarrollados.")

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
