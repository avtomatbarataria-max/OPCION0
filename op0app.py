import gradio as gr
import pandas as pd

# =============================================================================
# DATOS DE LAS TABLAS DE SUSTITUCIÓN
# =============================================================================

# Tabla de alimentos ricos en PROTEÍNA (P)
tabla_proteina = pd.DataFrame({
    'ALIMENTO': [
        'IMPACTWHEY MYPROTEIN', 'PECHUGA DE PAVO', 'PECHUGA DE POLLO SIN PIEL',
        'CLARAS DE HUEVO', 'TERNERA MAGRA', 'QUESO FRESCO BATIDO',
        'LOMO EMBUCHADO', 'GELATINA NEUTRA', 'ATUN', 'BONITO', 'GAMBAS', 'SEPIA'
    ],
    'GRAMOS_POR_100KCAL': [30, 100, 90, 200, 75, 220, 40, 25, 70, 70, 150, 140],
    'PROTEINAS_X_100KCAL': [21.5, 17, 20, 22, 16.5, 17, 16, 21, 16.7, 17, 22, 25.2],
    'CARBOS_X_100KCAL': [2.5, 4, 0, 1, 0, 7.5, 0, 0, 0, 0, 1.5, 1.1],
    'GRASAS_X_100KCAL': [0, 1, 1, 2, 3.5, 0, 3.5, 0, 3.2, 2.8, 1.5, 0.7]
})

# Tabla de alimentos ricos en PROTEÍNA+GRASA (P+G)
tabla_proteina_grasa = pd.DataFrame({
    'ALIMENTO': ['SALMON', 'TERNERA', 'HUEVO XXL', 'QUESO', 'BACON', 'JAMÓN SERRANO'],
    'GRAMOS_POR_100KCAL': [70, 45, 60, 30, 25, 50],
    'PROTEINAS_X_100KCAL': [15, 13, 8.5, 7.79, 3.5, 14],
    'CARBOS_X_100KCAL': [0, 0, 0, 0, 1, 0],
    'GRASAS_X_100KCAL': [4.5, 5, 6.6, 6, 9.25, 6]
})

# Tabla de alimentos ricos en GRASA (G)
tabla_grasa = pd.DataFrame({
    'ALIMENTO': [
        'FRUTOS SECOS', 'ACEITES', 'MANTEQUILLA DE CACAHUETE',
        'AGUACATE', 'GUACAMOLE', 'ACEITUNAS SIN HUESO',
        'CHOCOLATE NEGRO 85%', 'HUMMUS MERCADONA'
    ],
    'GRAMOS_POR_100KCAL': [17, 10, 16, 60, 50, 65, 18, 35],
    'PROTEINAS_X_100KCAL': [3, 0, 5, 1, 1, 1, 2, 2],
    'CARBOS_X_100KCAL': [4, 0, 2, 5, 5, 5, 4, 3],
    'GRASAS_X_100KCAL': [8, 11, 8, 9, 8, 10, 8, 9]
})

# Tabla de alimentos ricos en CARBOHIDRATOS (C)
tabla_carbos = pd.DataFrame({
    'ALIMENTO': [
        'ARROZ', 'PASTA', 'PATATA', 'LEGUMBRES', 'CHIPS DE PATATA',
        'PURE DE PATATA', 'PAN BARRA 100% INTEGRAL', 'PAN ESPELTA INTEGRAL MOLDE',
        'TORTITAS DE ARROZ', 'CEREALES CORNFLAKES', 'HARINA DE ARROZ',
        'COPOS DE AVENA', 'CEREALES AVENA CRUNCHY', 'PLATANO', 'DATILES',
        'HIGOS SECOS', 'MANGO', 'MANZANA'
    ],
    'GRAMOS_POR_100KCAL': [
        30, 30, 130, 30, 55, 30, 45, 45, 3.5, 25, 30, 27, 26, 100, 37, 37, 150, 200
    ],
    'PROTEINAS_X_100KCAL': [
        3, 3.5, 1.5, 7.7, 1.1, 2.2, 3.5, 3.5, 3, 2, 2.5, 4, 3.4, 1.3, 0.7, 1.3, 1, 0.6
    ],
    'CARBOS_X_100KCAL': [
        22, 20, 20, 18, 22.9, 22.8, 20, 20, 23, 21, 22, 14.68, 17.2, 27, 24.2, 20.4, 28, 24
    ],
    'GRASAS_X_100KCAL': [
        0, 1, 2.3, 0, 0, 0.1, 0, 1, 1, 0, 0, 2, 1.5, 0.4, 0.2, 0.5, 0, 0.4
    ]
})

# Opciones de DESAYUNOS/COMIDA 1
opciones_desayuno = pd.DataFrame({
    'OPCION': ['OPCIÓN 1', 'OPCIÓN 2', 'OPCIÓN 3', 'OPCIÓN 4'],
    'NOMBRE': ['TOSTADAS JAMÓN', 'TOSTADAS HUEVOS', 'TORTITAS DE AVENA', 'BOWL YOGURT'],
    'INGREDIENTES': [
        '2 rebanadas pan espelta (80g) + 50g jamon serrano + 8ml AOVE + tomate',
        '2 rebanadas pan espelta (80g) + 2 huevos revueltos + 30g jamon cocido + 8ml AOVE + tomate',
        '180ml claras huevo + 40g harina avena + 15g crema cacahuete + frutos rojos',
        '250g queso fresco batido + 40g copos maiz + 20g nueces + frutos rojos'
    ]
})

# Opciones de COMIDA 2
opciones_comida2 = pd.DataFrame({
    'OPCION': ['OPCIÓN 1', 'OPCIÓN 2', 'OPCIÓN 3', 'OPCIÓN 4', 'OPCIÓN 5', 'OPCIÓN 6'],
    'NOMBRE': [
        'SPAGUETTIS AL AIILO', 'GNOCCHIS CON POLLO', 'LENTEJAS',
        'NOODLES DE POLLO', 'ENSALADA DE PASTA', 'BOLOGNESA'
    ],
    'CARBOHIDRATO': [
        '100g Spaguetti', '200g gnocchi', '200g lentejas cocidas + 150g patata',
        '100g noodles arroz', '100g pasta', '100g pasta'
    ],
    'PROTEINA': [
        '290g gambas', '200g pechuga pollo', '1 huevo + jamón',
        '200g pechuga pollo', '2 latas atun + 1 huevo', '180g ternera'
    ]
})

# Opciones de COMIDA 3
opciones_comida3 = pd.DataFrame({
    'OPCION': ['OPCIÓN 1', 'OPCIÓN 2', 'OPCIÓN 3', 'OPCIÓN 4', 'OPCIÓN 5', 'OPCIÓN 6'],
    'NOMBRE': [
        'HUEVOS ROTOS', 'HEALTHY BURGUER', 'HEALTHY BURRITOS',
        'SOPA', 'GNOCCHI TERNERA', 'HEALTHY PIZZA'
    ],
    'CARBOHIDRATO': [
        '360g patata', '1 pan burguer + 150g patata', '2 tortillas',
        '80g fideos', '175g gnocchi', '130g masa pizza'
    ],
    'PROTEINA': [
        '2 huevos + 40g jamon', '160g burger + queso light', '160g pollo + guacamole',
        '100g pollo + 1 huevo', '160g ternera + 30g queso', '160g pollo + 50g queso'
    ]
})

# Snack comodín
snack_comodin = "🍌 1 plátano + 🥤 1 yogurt proteína"

# =============================================================================
# FUNCIONES DE CONVERSIÓN
# =============================================================================

def obtener_alimentos_por_categoria(categoria):
    """Obtiene lista de alimentos de una categoría"""
    if categoria == "Proteína":
        return sorted(tabla_proteina['ALIMENTO'].tolist())
    elif categoria == "Proteína + Grasa":
        return sorted(tabla_proteina_grasa['ALIMENTO'].tolist())
    elif categoria == "Grasa":
        return sorted(tabla_grasa['ALIMENTO'].tolist())
    elif categoria == "Carbohidratos":
        return sorted(tabla_carbos['ALIMENTO'].tolist())
    return []

def obtener_tabla_por_categoria(categoria):
    """Obtiene la tabla correspondiente a la categoría"""
    if categoria == "Proteína":
        return tabla_proteina
    elif categoria == "Proteína + Grasa":
        return tabla_proteina_grasa
    elif categoria == "Grasa":
        return tabla_grasa
    elif categoria == "Carbohidratos":
        return tabla_carbos
    return None

def convertir_alimento(categoria, alimento_origen, gramos_origen, alimento_destino):
    """Convierte gramos de un alimento a otro"""
    if not all([categoria, alimento_origen, gramos_origen, alimento_destino]):
        return None, None, None, None
    
    tabla = obtener_tabla_por_categoria(categoria)
    if tabla is None:
        return None, None, None, None
    
    # Buscar alimentos exactos
    origen_row = tabla[tabla['ALIMENTO'] == alimento_origen]
    destino_row = tabla[tabla['ALIMENTO'] == alimento_destino]
    
    if origen_row.empty or destino_row.empty:
        return None, None, None, None
    
    origen = origen_row.iloc[0]
    destino = destino_row.iloc[0]
    
    # Calcular kcal y gramos equivalentes
    kcal_base = gramos_origen / origen['GRAMOS_POR_100KCAL'] * 100
    gramos_destino = kcal_base / 100 * destino['GRAMOS_POR_100KCAL']
    
    # Calcular macros
    proteinas = kcal_base / 100 * destino['PROTEINAS_X_100KCAL']
    carbos = kcal_base / 100 * destino['CARBOS_X_100KCAL']
    grasas = kcal_base / 100 * destino['GRASAS_X_100KCAL']
    
    return round(gramos_destino, 1), round(proteinas, 1), round(carbos, 1), round(grasas, 1)

def mostrar_info_comida(tipo, opcion):
    """Muestra información detallada de la comida seleccionada"""
    if tipo == "Desayuno":
        datos = opciones_desayuno[opciones_desayuno['OPCION'] == opcion].iloc[0]
        return f"### {datos['NOMBRE']}\n\n**Ingredientes:** {datos['INGREDIENTES']}"
    elif tipo == "Comida 2":
        datos = opciones_comida2[opciones_comida2['OPCION'] == opcion].iloc[0]
        return f"### {datos['NOMBRE']}\n\n**Carbohidrato:** {datos['CARBOHIDRATO']}\n\n**Proteína:** {datos['PROTEINA']}"
    elif tipo == "Comida 3":
        datos = opciones_comida3[opciones_comida3['OPCION'] == opcion].iloc[0]
        return f"### {datos['NOMBRE']}\n\n**Carbohidrato:** {datos['CARBOHIDRATO']}\n\n**Proteína:** {datos['PROTEINA']}"
    return ""

# =============================================================================
# CONSTRUCCIÓN DE LA INTERFAZ GRADIO (SINTAXIS GRADIO 6.0)
# =============================================================================

with gr.Blocks(title="🍽️ Planificador de Comidas Fitness") as demo:
    gr.Markdown("# 🍽️ Planificador de Comidas Fitness")
    gr.Markdown("Herramienta para planificar tus comidas y calcular sustituciones de alimentos basadas en equivalencias calóricas.")
    
    with gr.Row():
        with gr.Column(scale=1):
            with gr.Accordion("📋 Información General", open=False):
                gr.Markdown("""
                ### Categorías de alimentos:
                - **Proteína**: Alimentos bajos en grasa
                - **Proteína + Grasa**: Alimentos con proteína y grasa
                - **Grasa**: Alimentos ricos en grasas saludables
                - **Carbohidratos**: Cereales, tubérculos, legumbres
                
                ### Reglas generales:
                - **Verdura**: Cantidad libre en todas las comidas
                - **Fruta**: 100-200g de temporada
                """)
            
            with gr.Accordion("🍌 Snack Comodín", open=False):
                gr.Markdown(snack_comodin)
            
            with gr.Accordion("📊 Ver Tablas", open=False):
                with gr.Tab("Proteína"):
                    gr.Dataframe(tabla_proteina)
                with gr.Tab("Proteína+Grasa"):
                    gr.Dataframe(tabla_proteina_grasa)
                with gr.Tab("Grasa"):
                    gr.Dataframe(tabla_grasa)
                with gr.Tab("Carbohidratos"):
                    gr.Dataframe(tabla_carbos)
        
        with gr.Column(scale=3):
            # Pestañas principales
            with gr.Tabs():
                # PESTAÑA 1: DESAYUNO
                with gr.Tab("🍳 COMIDA 1 (Desayuno)"):
                    desayuno_select = gr.Dropdown(
                        choices=opciones_desayuno['OPCION'].tolist(),
                        label="Selecciona opción de desayuno",
                        value="OPCIÓN 1"
                    )
                    desayuno_info = gr.Markdown()
                    
                    desayuno_select.change(
                        fn=lambda x: mostrar_info_comida("Desayuno", x),
                        inputs=desayuno_select,
                        outputs=desayuno_info
                    )
                    # Mostrar información inicial
                    desayuno_info.value = mostrar_info_comida("Desayuno", "OPCIÓN 1")
                
                # PESTAÑA 2: COMIDA 2
                with gr.Tab("🥗 COMIDA 2"):
                    comida2_select = gr.Dropdown(
                        choices=opciones_comida2['OPCION'].tolist(),
                        label="Selecciona opción de Comida 2",
                        value="OPCIÓN 1"
                    )
                    comida2_info = gr.Markdown()
                    
                    comida2_select.change(
                        fn=lambda x: mostrar_info_comida("Comida 2", x),
                        inputs=comida2_select,
                        outputs=comida2_info
                    )
                    comida2_info.value = mostrar_info_comida("Comida 2", "OPCIÓN 1")
                
                # PESTAÑA 3: COMIDA 3
                with gr.Tab("🍽️ COMIDA 3"):
                    comida3_select = gr.Dropdown(
                        choices=opciones_comida3['OPCION'].tolist(),
                        label="Selecciona opción de Comida 3",
                        value="OPCIÓN 1"
                    )
                    comida3_info = gr.Markdown()
                    
                    comida3_select.change(
                        fn=lambda x: mostrar_info_comida("Comida 3", x),
                        inputs=comida3_select,
                        outputs=comida3_info
                    )
                    comida3_info.value = mostrar_info_comida("Comida 3", "OPCIÓN 1")
                
                # PESTAÑA 4: CONVERSOR UNIVERSAL (VERSIÓN SIMPLIFICADA)
                with gr.Tab("🔄 Conversor Universal"):
                    gr.Markdown("### Calcula equivalencias entre alimentos de la MISMA categoría")
                    
                    conv_categoria = gr.Dropdown(
                        choices=["Proteína", "Proteína + Grasa", "Grasa", "Carbohidratos"],
                        label="1. Selecciona la categoría",
                        value="Proteína"
                    )
                    
                    with gr.Row():
                        with gr.Column():
                            gr.Markdown("**2. Elige alimento de origen**")
                            conv_origen = gr.Dropdown(
                                choices=obtener_alimentos_por_categoria("Proteína"),
                                label="Alimento original",
                                value=obtener_alimentos_por_categoria("Proteína")[0] if obtener_alimentos_por_categoria("Proteína") else None
                            )
                            conv_gramos = gr.Number(
                                label="Gramos",
                                value=100,
                                minimum=0,
                                step=10
                            )
                        
                        with gr.Column():
                            gr.Markdown("**3. Elige alimento destino**")
                            conv_destino = gr.Dropdown(
                                choices=obtener_alimentos_por_categoria("Proteína"),
                                label="Alimento sustituto",
                                value=obtener_alimentos_por_categoria("Proteína")[1] if len(obtener_alimentos_por_categoria("Proteína")) > 1 else obtener_alimentos_por_categoria("Proteína")[0]
                            )
                    
                    # Actualizar listas cuando cambia la categoría
                    def actualizar_alimentos(categoria):
                        alimentos = obtener_alimentos_por_categoria(categoria)
                        if len(alimentos) >= 2:
                            return [
                                gr.Dropdown(choices=alimentos, value=alimentos[0]),
                                gr.Dropdown(choices=alimentos, value=alimentos[1])
                            ]
                        elif len(alimentos) == 1:
                            return [
                                gr.Dropdown(choices=alimentos, value=alimentos[0]),
                                gr.Dropdown(choices=alimentos, value=alimentos[0])
                            ]
                        else:
                            return [
                                gr.Dropdown(choices=[], value=None),
                                gr.Dropdown(choices=[], value=None)
                            ]
                    
                    conv_categoria.change(
                        fn=actualizar_alimentos,
                        inputs=conv_categoria,
                        outputs=[conv_origen, conv_destino]
                    )
                    
                    conv_btn = gr.Button("Calcular equivalencia", variant="primary")
                    
                    conv_resultado = gr.Markdown()
                    
                    def calcular_equivalencia(cat, origen, gramos, destino):
                        if not origen or not destino:
                            return "❌ Por favor, selecciona ambos alimentos"
                        
                        if origen == destino:
                            return "❌ Elige alimentos diferentes"
                        
                        resultado = convertir_alimento(cat, origen, gramos, destino)
                        
                        if resultado[0] is not None:
                            gramos_dest, prot, carb, gras = resultado
                            return f"""
                            ## ✅ RESULTADO:
                            
                            ### {gramos}g de **{origen}** = **{gramos_dest}g** de **{destino}**
                            
                            ### 📊 Macros:
                            - **Proteínas:** {prot}g
                            - **Carbohidratos:** {carb}g
                            - **Grasas:** {gras}g
                            """
                        else:
                            return "❌ No se pudo calcular la equivalencia."
                    
                    conv_btn.click(
                        fn=calcular_equivalencia,
                        inputs=[conv_categoria, conv_origen, conv_gramos, conv_destino],
                        outputs=conv_resultado
                    )

# =============================================================================
# LANZAR LA APLICACIÓN
# =============================================================================
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 7860))
    demo.launch(server_name="0.0.0.0", server_port=port)
