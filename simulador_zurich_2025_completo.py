
import streamlit as st

def format_currency(value):
    return "${:,.2f}".format(value)

st.set_page_config(page_title="Simulador Bonos Zurich 2025", layout="centered")

st.markdown("<h1 style='text-align: center;'>Simulador de Bonos</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>Zurich 2025</h2>", unsafe_allow_html=True)

# Paso 1: Nombre del agente
nombre_agente = st.text_input("Nombre del agente")

if nombre_agente:
    # Paso 2: Selección del plan
    plan = st.selectbox("Selecciona el plan:", ["IMPULZA", "CIZ"])

    # Paso 3: Selección del ramo según plan
    if plan == "IMPULZA":
        ramo = st.selectbox("Selecciona el ramo:", ["Auto", "Flotillas", "Daños", "Vida + GMM", "Accidentes Personales", "Universal Assistance"])
    else:
        ramo = st.selectbox("Selecciona el ramo:", ["Auto", "Flotillas", "Daños", "Vida", "GMM", "Conservación"])

    total_bono = 0
    resultados = []

    # Paso 4: Campos dinámicos por ramo
    if plan == "IMPULZA":
        if ramo == "Auto":
            pol = st.number_input("Pólizas pagadas mensuales (Auto)", min_value=0, step=1)
            if pol >= 5:
                bono = 0.05
                comentario = "✅ 5% por 5+ pólizas"
            elif pol >= 3:
                bono = 0.04
                comentario = "✅ 4% por 3-4 pólizas"
            elif pol >= 1:
                bono = 0.03
                comentario = "✅ 3% por 1-2 pólizas"
            else:
                bono = 0
                comentario = "❌ No aplica bono"
            total_bono = pol * 1000 * bono
            resultados.append(f"**Auto:** {format_currency(total_bono)} ({bono*100:.1f}%) - {comentario}")

        elif ramo == "Flotillas":
            pol = st.number_input("Pólizas pagadas mensuales (Flotillas)", min_value=0, step=1)
            if pol >= 7:
                bono = 0.035
                comentario = "✅ 3.5% por 7+ pólizas"
            elif pol >= 5:
                bono = 0.025
                comentario = "✅ 2.5% por 5-6 pólizas"
            elif pol >= 3:
                bono = 0.015
                comentario = "✅ 1.5% por 3-4 pólizas"
            else:
                bono = 0
                comentario = "❌ No aplica bono"
            total_bono = pol * 1000 * bono
            resultados.append(f"**Flotillas:** {format_currency(total_bono)} ({bono*100:.1f}%) - {comentario}")

        elif ramo == "Daños":
            canal = st.radio("¿Por dónde emite?", ["Portal", "Mesa de trámites"])
            pol = st.number_input("Pólizas pagadas mensuales (Daños)", min_value=0, step=1)
            if pol >= 5:
                bono = 0.07
            elif pol >= 3:
                bono = 0.06
            elif pol >= 1:
                bono = 0.03
            else:
                bono = 0
            comentario = f"{'✅' if bono else '❌'} {'Aplica' if bono else 'No aplica'} bono"
            total_bono = pol * 1000 * bono
            resultados.append(f"**Daños ({canal}):** {format_currency(total_bono)} ({bono*100:.1f}%) - {comentario}")

        elif ramo == "Vida + GMM":
            pol = st.number_input("Pólizas acumulables (Vida + GMM)", min_value=0, step=1)
            if pol >= 11:
                bono = 0.08
                comentario = "✅ 3% GMM + 5% Vida"
            elif pol >= 4:
                bono = 0.06
                comentario = "✅ 2% GMM + 4% Vida"
            elif pol >= 1:
                bono = 0.04
                comentario = "✅ 1% GMM + 3% Vida"
            else:
                bono = 0
                comentario = "❌ No aplica bono"
            total_bono = pol * 1000 * bono
            resultados.append(f"**Vida + GMM:** {format_currency(total_bono)} ({bono*100:.1f}%) - {comentario}")

        elif ramo == "Accidentes Personales":
            prima = st.number_input("Prima mensual acumulada (Accidentes Personales)", min_value=0, step=1000)
            if prima >= 1_000_000:
                bono = 0.12
            elif prima >= 400_000:
                bono = 0.08
            elif prima >= 45_000:
                bono = 0.04
            else:
                bono = 0
            comentario = f"{'✅' if bono else '❌'} {'Aplica' if bono else 'No aplica'} bono"
            total_bono = prima * bono
            resultados.append(f"**Accidentes Personales:** {format_currency(total_bono)} ({bono*100:.1f}%) - {comentario}")

        elif ramo == "Universal Assistance":
            prima = st.number_input("Prima mensual (USD)", min_value=0, step=100)
            if prima >= 8500:
                bono = 0.10
            elif prima >= 4000:
                bono = 0.07
            elif prima >= 2000:
                bono = 0.05
            else:
                bono = 0
            comentario = f"{'✅' if bono else '❌'} {'Aplica' if bono else 'No aplica'} bono"
            total_bono = prima * bono
            resultados.append(f"**Universal Assistance:** {format_currency(total_bono)} ({bono*100:.1f}%) - {comentario}")

    elif plan == "CIZ":
        if ramo == "Auto":
            prima = st.number_input("Prima mensual Auto", min_value=0, step=1000)
            siniestralidad = st.number_input("Siniestralidad (%)", min_value=0.0, max_value=100.0)
            if siniestralidad <= 65:
                if prima >= 100_000:
                    bono = 0.055
                elif prima >= 50_000:
                    bono = 0.045
                elif prima >= 20_000:
                    bono = 0.035
                else:
                    bono = 0
            else:
                bono = 0
            comentario = f"{'✅' if bono else '❌'} {'Aplica' if bono else 'No aplica'} bono"
            total_bono = prima * bono
            resultados.append(f"**Auto CIZ:** {format_currency(total_bono)} ({bono*100:.1f}%) - {comentario}")

    # Paso 5: Botón al final
    if st.button("Calcular Bonos"):
        st.markdown("### Resultados")
        for r in resultados:
            st.markdown(f"- {r}")
        st.markdown(f"### Total bono estimado: **{format_currency(total_bono)}**")
        st.markdown("---")
        st.markdown("<p style='text-align: center; color: gray;'>Aplican restricciones y condiciones conforme al cuaderno oficial de Zurich Seguros 2025.</p>", unsafe_allow_html=True)
