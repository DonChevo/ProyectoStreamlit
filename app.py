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
# SECCIÓN: EJERCICIO 1 - FLUJO DE CAJA
# ==========================================
elif opcion == "Ejercicio 1":
    st.title("💰 Ejercicio 1: Registro de Flujo de Caja")
    
    # Descripción del ejercicio
    st.markdown("""
    Este módulo permite registrar movimientos financieros de manera dinámica en una lista. 
    A través de la interacción con los elementos de la interfaz, el sistema calcula de forma automática 
    el total de ingresos, gastos y el saldo final neto, determinando el estado actual de tu flujo de caja.
    """)
    st.divider()

    # Inicialización del estado de la sesión para preservar la lista de movimientos
    if "movimientos" not in st.session_state:
        st.session_state.movimientos = []

    # Layout: Formulario de entrada de datos | Visualización y Métricas
    col_formulario, col_resultados = st.columns([1, 2], gap="large")

    with col_formulario:
        st.subheader("📝 Registrar Movimiento")
        
        # Widgets para ingresar los datos del flujo
        concepto = st.text_input("Concepto del movimiento:", placeholder="Ej. Pago de Alquiler, Salario, Almuerzo")
        tipo_movimiento = st.selectbox("Tipo de movimiento:", ["Ingreso", "Gasto"])
        
        # Controlamos que el valor ingresado sea siempre positivo
        valor = st.number_input("Monto / Valor ($):", min_value=0.0, step=10.0, format="%.2f")
        
        # Botón para agregar movimientos
        btn_agregar = st.button("Agregar Movimiento", use_container_width=True)

        if btn_agregar:
            if concepto.strip() == "":
                st.warning("⚠️ Por favor, ingresa un concepto válido.")
            elif valor <= 0:
                st.warning("⚠️ El monto debe ser mayor a cero.")
            else:
                # Creación del registro como diccionario y adición a la lista del estado
                nuevo_movimiento = {
                    "Concepto": concepto,
                    "Tipo": tipo_movimiento,
                    "Valor": valor
                }
                st.session_state.movimientos.append(nuevo_movimiento)
                st.success("¡Movimiento registrado con éxito!")

        # Botón opcional para limpiar el historial y reiniciar la lista vacía
        if st.button("Limpiar Historial"):
            st.session_state.movimientos = []
            st.rerun()

    with col_resultados:
        st.subheader("📊 Análisis del Flujo")

        if not st.session_state.movimientos:
            st.info("Aún no se han registrado movimientos. Usa el formulario de la izquierda para comenzar.")
        else:
            # 1. Cálculo de totales utilizando lógica estructurada de Python
            total_ingresos = sum(m["Valor"] for m in st.session_state.movimientos if m["Tipo"] == "Ingreso")
            total_gastos = sum(m["Valor"] for m in st.session_state.movimientos if m["Tipo"] == "Gasto")
            saldo_final = total_ingresos - total_gastos

            # 2. Despliegue de métricas financieras (st.metric)
            m_col1, m_col2, m_col3 = st.columns(3)
            with m_col1:
                st.metric("Total Ingresos", f"${total_ingresos:,.2f}")
            with m_col2:
                st.metric("Total Gastos", f"${total_gastos:,.2f}", delta=f"-${total_gastos:,.2f}", delta_color="inverse")
            with m_col3:
                st.metric("Saldo Final", f"${saldo_final:,.2f}")

            st.write("---")

            # 3. Indicador del estado del flujo de caja (A favor / En contra)
            if saldo_final >= 0:
                st.success(f"🟢 **Flujo de caja a favor:** Cuentas con un superávit neto de **${saldo_final:,.2f}**.")
            else:
                st.error(f"🔴 **Flujo de caja en contra:** Tienes un déficit neto de **${abs(saldo_final):,.2f}**.")

            st.write("---")
            
            # 4. Tabla de movimientos registrados (st.dataframe)
            st.markdown("##### 📋 Listado de Movimientos Registrados")
            st.dataframe(st.session_state.movimientos, use_container_width=True)


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
