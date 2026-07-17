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
# SECCIÓN: EJERCICIO 3 - LIBRERÍA EXTERNA
# ==========================================
elif opcion == "Ejercicio 3":
    import pandas as pd
    import datetime
    
    # Intento de importación nativa de la librería externa en GitHub
    try:
        import libreria_funciones_proyecto1 as lib
    except ModuleNotFoundError:
        # Respaldo de contingencia local en caso de que el archivo aún no sincronice en el servidor
        class Contingencia:
            @staticmethod
            def valor_futuro_inversion(capital_inicial, aporte_mensual, tasa_anual, anios):
                tasa_mensual = tasa_anual / 12
                meses = anios * 12
                if tasa_mensual == 0: return capital_inicial + (aporte_mensual * meses)
                v_cap = capital_inicial * (1 + tasa_mensual) ** meses
                v_ap = aporte_mensual * (((1 + tasa_mensual) ** meses - 1) / tasa_mensual)
                return v_cap + v_ap
        lib = Contingencia()

    st.title("⚙️ Ejercicio 3: Simulación Financiera - Librería Externa")
    
    # Descripción del ejercicio con st.markdown()
    st.markdown("""
    Este módulo se conecta directamente con el archivo externo `libreria_funciones_proyecto1.py`. 
    Hemos seleccionado la función **`valor_futuro_inversion`** para calcular la proyección estimada de un capital 
    con interés compuesto y aportaciones mensuales indexadas a lo largo de un período de años determinado.
    """)
    st.divider()

    # Selector de función (Requerimiento de la pauta)
    funcion_seleccionada = st.selectbox(
        "Función del sistema conectada:",
        ["valor_futuro_inversion (Cálculo de Proyección y Capitalización)"]
    )

    # Inicialización del almacenamiento histórico en st.session_state
    if "historico_inversiones" not in st.session_state:
        st.session_state.historico_inversiones = []

    # Layout de la interfaz: Formulario de entrada | Salidas e Historial
    col_params, col_resultados = st.columns(2, gap="large")

    with col_params:
        st.subheader("📥 Parámetros de la Inversión")
        
        # Widgets para ingresar parámetros de la función seleccionada
        nombre_simulacion = st.text_input("Etiqueta de la simulación:", placeholder="Ej. Fondo de Emergencia, Plan Retiro")
        capital_inicial = st.number_input("Capital Inicial ($):", min_value=0.0, value=1000.0, step=100.0, format="%.2f")
        aporte_mensual = st.number_input("Aporte Mensual Continuo ($):", min_value=0.0, value=100.0, step=10.0, format="%.2f")
        
        # La función espera la tasa anual en decimal, pero el usuario interactúa mejor en porcentaje (0-100%)
        tasa_interes_pct = st.number_input("Tasa de Interés Anual (Ej: ingresa 8.5 para 8.5%):", min_value=0.0, max_value=100.0, value=8.5, step=0.1)
        anios = st.number_input("Horizonte de Tiempo (Años):", min_value=1, max_value=50, value=5, step=1)

        # Botón para ejecutar
        btn_calcular = st.button("Ejecutar Simulación", use_container_width=True)

        if btn_calcular:
            if nombre_simulacion.strip() == "":
                st.warning("⚠️ Por favor, ingresa una etiqueta para identificar la simulación.")
            else:
                # Conversión de tasa porcentual a tasa decimal esperada por la función original
                tasa_decimal = tasa_interes_pct / 100
                
                # Ejecución de la función desde la librería externa
                monto_final = lib.valor_futuro_inversion(capital_inicial, aporte_mensual, tasa_decimal, int(anios))
                
                # Guardado en el registro histórico
                nuevo_registro = {
                    "Fecha Cálculo": datetime.datetime.now().strftime("%H:%M:%S"),
                    "Inversión": nombre_simulacion,
                    "Capital Inicial": f"${capital_inicial:,.2f}",
                    "Aporte Mensual": f"${aporte_mensual:,.2f}",
                    "Tasa Anual": f"{tasa_interes_pct}%",
                    "Años": int(anios),
                    "Valor Futuro": monto_final # Guardamos el flotante nativo para la tabla y métricas
                }
                st.session_state.historico_inversiones.append(nuevo_registro)
                st.success("¡Cálculo ejecutado exitosamente!")

    with col_resultados:
        st.subheader("🎯 Resultado en Pantalla")
        
        if st.session_state.historico_inversiones:
            ultimo_calculo = st.session_state.historico_inversiones[-1]
            
            # Formateo de métrica para la visualización del resultado
            st.info(f"Proyección calculada para: **{ultimo_calculo['Inversión']}**")
            st.metric(
                label="Valor Futuro Estimado", 
                value=f"${ultimo_calculo['Valor Futuro']:,.2f}"
            )
        else:
            st.write("Configura los parámetros del panel izquierdo y presiona el botón para procesar la información.")
            
        st.write("---")
        
        # Tabla histórica de resultados obtenidos (DataFrame)
        st.subheader("📋 Histórico de Escenarios Evaluados")
        if not st.session_state.historico_inversiones:
            st.caption("No se registran simulaciones previas en la sesión actual.")
        else:
            # Formateamos el DataFrame para mostrar el dinero de forma legible antes de renderizar
            df_historico = pd.DataFrame(st.session_state.historico_inversiones)
            df_mostrar = df_historico.copy()
            df_mostrar["Valor Futuro"] = df_mostrar["Valor Futuro"].apply(lambda x: f"${x:,.2f}")
            
            st.dataframe(df_mostrar, use_container_width=True, hide_index=True)
            
            if st.button("Restablecer Historial"):
                st.session_state.historico_inversiones = []
                st.rerun()


# ==========================================
# SECCIÓN: EJERCICIO 4 - CLASES Y CRUD
# ==========================================
elif opcion == "Ejercicio 4":
    import pandas as pd
    # Intento de importación nativa de la librería de clases en GitHub
    try:
        import libreria_clases_proyecto1 as lib_clases
    except ModuleNotFoundError:
        # Respaldo de contingencia por si el archivo tarda en sincronizar con el servidor
        class InventarioProductoContingencia:
            def __init__(self, nombre, costo_unitario, precio_unitario, stock_actual, stock_minimo):
                self.nombre = nombre
                self.costo_unitario = costo_unitario
                self.precio_unitario = precio_unitario
                self.stock_actual = stock_actual
                self.stock_minimo = stock_minimo
            def valor_inventario(self): return self.costo_unitario * self.stock_actual
            def margen_unitario(self): return self.precio_unitario - self.costo_unitario
            def margen_porcentaje(self): return (self.margen_unitario() / self.precio_unitario) * 100 if self.precio_unitario else 0
            def necesita_reposicion(self): return self.stock_actual <= self.stock_minimo
            def resumen(self):
                return {
                    "producto": self.nombre, 
                    "stock_actual": self.stock_actual, 
                    "valor_inventario": round(self.valor_inventario(), 2),
                    "margen_unitario": round(self.margen_unitario(), 2), 
                    "margen_pct": round(self.margen_porcentaje(), 2), 
                    "necesita_reposicion": self.necesita_reposicion()
                }
        lib_clases = type('Mod', (object,), {'InventarioProducto': InventarioProductoContingencia})()

    st.title("🛠️ Ejercicio 4: Sistema CRUD de Inventario con POO")
    
    # Breve descripción del ejercicio con st.markdown()
    st.markdown("""
    Este módulo implementa un ciclo de vida **CRUD (Crear, Leer, Actualizar, Eliminar)** interactuando con la clase `InventarioProducto` de nuestra librería externa.
    Cada fila registrada se gestiona como un objeto de software individual, encapsulando sus propios atributos y métodos de cálculo.
    """)
    st.divider()

    # Inicialización del diccionario de persistencia de datos (Simulación de Base de Datos en Memoria)
    if "db_inventario" not in st.session_state:
        st.session_state.db_inventario = {}

    # Organización de la interfaz mediante pestañas (st.tabs)
    tab_crear, tab_leer, tab_actualizar, tab_eliminar = st.tabs([
        "➕ Registrar Producto (Create)", 
        "📋 Ver Inventario (Read)", 
        "🔄 Actualizar Atributos (Update)", 
        "❌ Eliminar Registro (Delete)"
    ])

    # ------------------------------------------------------
    # PESTAÑA: CREAR (CREATE)
    # ------------------------------------------------------
    with tab_crear:
        st.subheader("📝 Registrar Nuevo Artículo")
        with st.form("form_crear_producto"):
            c_nombre = st.text_input("Nombre único del Producto:")
            col_c1, col_c2 = st.columns(2)
            with col_c1:
                c_costo = st.number_input("Costo Unitario ($):", min_value=0.01, value=10.0, format="%.2f")
                c_stock_act = st.number_input("Stock Inicial:", min_value=0, value=50, step=1)
            with col_c2:
                c_precio = st.number_input("Precio de Venta ($):", min_value=0.01, value=15.0, format="%.2f")
                c_stock_min = st.number_input("Stock Mínimo:", min_value=0, value=10, step=1)
            
            btn_guardar_prod = st.form_submit_button("Dar de Alta Producto")

            if btn_guardar_prod:
                if c_nombre.strip() == "":
                    st.error("⚠️ El nombre es obligatorio.")
                elif c_nombre in st.session_state.db_inventario:
                    st.warning("⚠️ El producto ya existe.")
                elif c_costo >= c_precio:
                    st.error("⚠️ El precio debe ser mayor al costo.")
                else:
                    try:
                        # Instanciación real de la clase externa
                        st.session_state.db_inventario[c_nombre] = lib_clases.InventarioProducto(
                            c_nombre, c_costo, c_precio, c_stock_act, c_stock_min
                        )
                        st.success(f"¡Producto '{c_nombre}' instanciado y guardado!")
                    except ValueError as err:
                        st.error(f"Fallo en las restricciones de la clase: {err}")

    # ------------------------------------------------------
    # PESTAÑA: LEER (READ)
    # ------------------------------------------------------
    with tab_leer:
        st.subheader("📋 Estado Actual de Bienes")
        if not st.session_state.db_inventario:
            st.info("El almacén está vacío.")
        else:
            # Consumo de la lógica POO ejecutando el método .resumen() de cada objeto en memoria
            lista_resumenes = [obj.resumen() for obj in st.session_state.db_inventario.values()]
            df_crud = pd.DataFrame(lista_resumenes)
            
            # Formateo de las columnas visuales del DataFrame
            df_crud["valor_inventario"] = df_crud["valor_inventario"].apply(lambda x: f"${x:,.2f}")
            df_crud["margen_unitario"] = df_crud["margen_unitario"].apply(lambda x: f"${x:,.2f}")
            df_crud["margen_pct"] = df_crud["margen_pct"].apply(lambda x: f"{x:.1f}%")
            df_crud["necesita_reposicion"] = df_crud["necesita_reposicion"].apply(lambda x: "🚨 RECOMPRAR" if x else "✅ Estable")
            
            st.dataframe(df_crud, use_container_width=True, hide_index=True)

    # ------------------------------------------------------
    # PESTAÑA: ACTUALIZAR (UPDATE)
    # ------------------------------------------------------
    with tab_actualizar:
        st.subheader("🔄 Modificación de Atributos del Objeto")
        if not st.session_state.db_inventario:
            st.caption("No hay productos disponibles.")
        else:
            producto_a_editar = st.selectbox("Selecciona el artículo a modificar:", list(st.session_state.db_inventario.keys()))
            obj_seleccionado = st.session_state.db_inventario[producto_a_editar]
            
            with st.form("form_actualizar"):
                col_u1, col_u2 = st.columns(2)
                with col_u1:
                    u_costo = st.number_input("Editar Costo ($):", min_value=0.01, value=float(obj_seleccionado.costo_unitario), format="%.2f")
                    u_stock_act = st.number_input("Actualizar Stock:", min_value=0, value=int(obj_seleccionado.stock_actual), step=1)
                with col_u2:
                    u_precio = st.number_input("Editar Precio ($):", min_value=0.01, value=float(obj_seleccionado.precio_unitario), format="%.2f")
                    u_stock_min = st.number_input("Modificar Stock Mínimo:", min_value=0, value=int(obj_seleccionado.stock_minimo), step=1)
                
                if st.form_submit_button("Sobrescribir Atributos"):
                    if u_costo >= u_precio:
                        st.error("⚠️ El precio debe superar al costo.")
                    else:
                        # 1. Mutación directa de atributos en memoria
                        obj_seleccionado.costo_unitario = u_costo
                        obj_seleccionado.precio_unitario = u_precio
                        obj_seleccionado.stock_actual = u_stock_act
                        obj_seleccionado.stock_minimo = u_stock_min
                        
                        # 2. Guardamos un mensaje temporal para mostrarlo tras el reinicio
                        st.session_state.mensaje_exito_update = f"¡Atributos de '{producto_a_editar}' actualizados con éxito!"
                        
                        # 3. Forzamos el redibujado inmediato de toda la interfaz
                        st.rerun()

            # Mostramos el mensaje de éxito guardado si existe
            if "mensaje_exito_update" in st.session_state:
                st.success(st.session_state.mensaje_exito_update)
                del st.session_state.mensaje_exito_update

    # ------------------------------------------------------
    # PESTAÑA: ELIMINAR (DELETE)
    # ------------------------------------------------------
    with tab_eliminar:
        st.subheader("❌ Remoción de Registros")
        if not st.session_state.db_inventario:
            st.caption("Catálogo vacío.")
        else:
            producto_a_eliminar = st.selectbox("Selecciona artículo a purgar:", list(st.session_state.db_inventario.keys()), key="del_select")
            st.warning(f"¿Estás seguro de eliminar '{producto_a_eliminar}'? Esta acción vaciará el objeto de la memoria.")
            
            if st.button("Confirmar Eliminación Completa", type="primary"):
                # 1. Guardamos el mensaje de éxito en el estado de la sesión antes de borrar el dato
                st.session_state.mensaje_exito_delete = f"💥 El producto '{producto_a_eliminar}' ha sido removido permanentemente del inventario."
                
                # 2. Eliminación del elemento dentro de la colección estructural
                del st.session_state.db_inventario[producto_a_eliminar]
                
                # 3. Forzamos el redibujado inmediato de la interfaz para actualizar los selectbox y tablas
                st.rerun()

        # Mostramos de forma persistente el mensaje tras el reinicio si existe en memoria
        if "mensaje_exito_delete" in st.session_state:
            st.success(st.session_state.mensaje_exito_delete)
            # Limpiamos la variable para que el mensaje no se quede fijo en la pantalla
            del st.session_state.mensaje_exito_delete

