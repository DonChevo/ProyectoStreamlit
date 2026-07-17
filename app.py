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
# SECCIÓN: EJERCICIO 2 - REGISTRO CON NUMPY
# ==========================================
elif opcion == "Ejercicio 2":
    import numpy as np
    import pandas as pd

    st.title("📦 Ejercicio 2: Inventario y Ventas con NumPy")
    
    # Descripción del ejercicio
    st.markdown("""
    Este módulo gestiona el registro de productos utilizando vectores unidimensionales de **NumPy**. 
    Cada campo del formulario alimenta un arreglo independiente. Al presionar el botón, 
    estos vectores se consolidan matemáticamente y se transforman en un DataFrame reactivo para su visualización.
    """)
    st.divider()

    # Inicialización del estado de la sesión para los arreglos de NumPy
    if "np_nombres" not in st.session_state:
        st.session_state.np_nombres = np.array([], dtype=str)
        st.session_state.np_categorias = np.array([], dtype=str)
        st.session_state.np_precios = np.array([], dtype=float)
        st.session_state.np_cantidades = np.array([], dtype=int)
        st.session_state.np_totales = np.array([], dtype=float)

    # Layout de la interfaz: Formulario | Visualización del Inventario
    col_form, col_tabla = st.columns([1, 2], gap="large")

    with col_form:
        st.subheader("➕ Registro de Producto")
        
        # Widgets para ingresar datos
        nombre_prod = st.text_input("Nombre del producto:", placeholder="Ej. Laptop, Teclado, Monitor")
        categoria_prod = st.selectbox("Categoría:", ["Electrónica", "Oficina", "Hogar", "Otros"])
        precio_prod = st.number_input("Precio Unitario ($):", min_value=0.0, step=0.5, format="%.2f")
        cantidad_prod = st.number_input("Cantidad:", min_value=1, step=1)
        
        # Cálculo automático del total del registro actual
        total_prod = precio_prod * cantidad_prod
        st.caption(f"**Total calculado para este registro:** ${total_prod:,.2f}")

        # Botón para agregar nuevo registro
        btn_agregar_prod = st.button("Agregar a Inventario", use_container_width=True)

        if btn_agregar_prod:
            if nombre_prod.strip() == "":
                st.warning("⚠️ El nombre del producto no puede estar vacío.")
            elif precio_prod <= 0:
                st.warning("⚠️ El precio debe ser mayor a cero.")
            else:
                # Concatenación de nuevos elementos en los arreglos de NumPy correspondientes
                st.session_state.np_nombres = np.append(st.session_state.np_nombres, nombre_prod)
                st.session_state.np_categorias = np.append(st.session_state.np_categorias, categoria_prod)
                st.session_state.np_precios = np.append(st.session_state.np_precios, precio_prod)
                st.session_state.np_cantidades = np.append(st.session_state.np_cantidades, cantidad_prod)
                st.session_state.np_totales = np.append(st.session_state.np_totales, total_prod)
                st.success(f"¡{nombre_prod} añadido correctamente!")

        # Botón para resetear los arreglos de NumPy
        if st.button("Vaciar Inventario"):
            st.session_state.np_nombres = np.array([], dtype=str)
            st.session_state.np_categorias = np.array([], dtype=str)
            st.session_state.np_precios = np.array([], dtype=float)
            st.session_state.np_cantidades = np.array([], dtype=int)
            st.session_state.np_totales = np.array([], dtype=float)
            st.st.rerun()

    with col_tabla:
        st.subheader("📋 Tabla en DataFrame Actualizada")

        # Control de flujo: validar si el arreglo tiene elementos creados
        if len(st.session_state.np_nombres) == 0:
            st.info("El inventario está vacío. Ingresa datos en el formulario para generar los arreglos de NumPy.")
        else:
            # Construcción del DataFrame a partir de la estructura de diccionarios alimentada por NumPy
            df_inventario = pd.DataFrame({
                "Producto": st.session_state.np_nombres,
                "Categoría": st.session_state.np_categorias,
                "Precio Unitario": st.session_state.np_precios,
                "Cantidad": st.session_state.np_cantidades,
                "Total General": st.session_state.np_totales
            })

            # Mostrar la tabla en DataFrame actualizada de forma interactiva
            st.dataframe(df_inventario, use_container_width=True, hide_index=True)

            # Métricas analíticas complementarias usando funciones de NumPy en el DataFrame
            st.write("---")
            st.markdown("##### 📈 Resumen Estadístico (Operaciones NumPy)")
            
            c1, c2 = st.columns(2)
            with c1:
                suma_totales = np.sum(st.session_state.np_totales)
                st.metric("Inversión Total en Inventario", f"${suma_totales:,.2f}")
            with c2:
                promedio_precio = np.mean(st.session_state.np_precios)
                st.metric("Precio Promedio de Productos", f"${promedio_precio:,.2f}")


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
