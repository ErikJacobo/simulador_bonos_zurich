# --- Simulador Zurich 2025 - Plan CIZ (Completo) ---
import streamlit as st
from PIL import Image

def format_currency(value):
    return "$ {:,.2f}".format(value)

st.set_page_config(page_title="Simulador Bonos Zurich 2025 - CIZ", layout="centered")

# Logo
col1, col2 = st.columns([5, 1])
with col2:
    logo = Image.open("link logo.jpg")
    st.image(logo, width=100)

st.markdown("<h1 style='text-align: center;'>Simulador de Bonos</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>Zurich 2025 - Plan CIZ</h2>", unsafe_allow_html=True)

nombre_agente = st.text_input("Nombre del agente")

if nombre_agente:
    ramo = st.selectbox("Selecciona el ramo a simular:", ["Auto", "Flotillas", "Daños", "Vida", "GMM", "Conservación"])

    resultados = []
    datos_ingresados = []
    total_bono = 0

  # --- AUTO ---
    if ramo == "Auto":
        prima_mensual = st.number_input("Prima mensual pagada (Auto)", min_value=0.0)
        prima_anual = st.number_input("Prima anual pagada (Auto)", min_value=0.0)
        siniestralidad = st.number_input("Siniestralidad acumulada (%)", min_value=0.0, max_value=100.0)

        datos_ingresados += [
            f"Prima mensual: {format_currency(prima_mensual)}",
            f"Prima anual: {format_currency(prima_anual)}",
            f"Siniestralidad: {siniestralidad:.2f}%"
        ]

        # Bono mensual
        porcentaje_mensual = 0
        if prima_mensual >= 100000:
            porcentaje_mensual = 0.055
        elif prima_mensual >= 50000:
            porcentaje_mensual = 0.045
        elif prima_mensual >= 20000:
            porcentaje_mensual = 0.035

        monto_mensual = prima_mensual * porcentaje_mensual
        total_bono += monto_mensual
        comentario_mensual = f"{'✅' if porcentaje_mensual else '❌'} Bono mensual según prima: {format_currency(prima_mensual)}."
        resultados.append(("🚗 Bono Mensual Auto", porcentaje_mensual, monto_mensual, comentario_mensual))

        # Bono recuperación
        porcentaje_rec = 0
        if prima_anual >= 1200000:
            porcentaje_rec = 0.055
        elif prima_anual >= 600000:
            porcentaje_rec = 0.045
        elif prima_anual >= 240000:
            porcentaje_rec = 0.035

        monto_rec = prima_anual * porcentaje_rec
        total_bono += monto_rec
        comentario_rec = f"{'✅' if porcentaje_rec else '❌'} Bono recuperación según prima anual: {format_currency(prima_anual)}."
        resultados.append(("📅 Bono Recuperación Anual Auto", porcentaje_rec, monto_rec, comentario_rec))

        # Bono rentabilidad
        porcentaje_rent = 0
        if siniestralidad <= 40:
            porcentaje_rent = 0.03
        elif siniestralidad <= 50:
            porcentaje_rent = 0.02
        elif siniestralidad <= 60:
            porcentaje_rent = 0.01

        monto_rent = prima_anual * porcentaje_rent
        total_bono += monto_rent
        comentario_rent = f"{'✅' if porcentaje_rent else '❌'} Rentabilidad del {siniestralidad:.2f}%."
        resultados.append(("🧾 Bono Rentabilidad Auto", porcentaje_rent, monto_rent, comentario_rent))


   # --- FLOTILLAS ---
    if ramo == "Flotillas":
        prima_mensual = st.number_input("Prima mensual pagada (Flotillas)", min_value=0.0)
        prima_anual = st.number_input("Prima anual pagada (Flotillas)", min_value=0.0)
        siniestralidad = st.number_input("Siniestralidad acumulada (%)", min_value=0.0, max_value=100.0)

        datos_ingresados += [
            f"Prima mensual: {format_currency(prima_mensual)}",
            f"Prima anual: {format_currency(prima_anual)}",
            f"Siniestralidad: {siniestralidad:.2f}%"
        ]

        # Bono mensual
        porcentaje_mensual = 0
        if prima_mensual >= 150000:
            porcentaje_mensual = 0.045
        elif prima_mensual >= 100000:
            porcentaje_mensual = 0.035
        elif prima_mensual >= 30000:
            porcentaje_mensual = 0.025

        monto_mensual = prima_mensual * porcentaje_mensual
        total_bono += monto_mensual
        comentario_mensual = f"{'✅' if porcentaje_mensual else '❌'} Bono mensual según prima: {format_currency(prima_mensual)}."
        resultados.append(("🚛 Bono Mensual Flotillas", porcentaje_mensual, monto_mensual, comentario_mensual))

        # Bono recuperación
        porcentaje_rec = 0
        if prima_anual >= 1800000:
            porcentaje_rec = 0.045
        elif prima_anual >= 1200000:
            porcentaje_rec = 0.035
        elif prima_anual >= 360000:
            porcentaje_rec = 0.025

        monto_rec = prima_anual * porcentaje_rec
        total_bono += monto_rec
        comentario_rec = f"{'✅' if porcentaje_rec else '❌'} Bono recuperación según prima anual: {format_currency(prima_anual)}."
        resultados.append(("📆 Bono Recuperación Anual Flotillas", porcentaje_rec, monto_rec, comentario_rec))

        # Bono rentabilidad
        porcentaje_rent = 0
        if siniestralidad <= 45:
            porcentaje_rent = 0.04
        elif siniestralidad <= 50:
            porcentaje_rent = 0.025
        elif siniestralidad <= 55:
            porcentaje_rent = 0.015

        monto_rent = prima_anual * porcentaje_rent
        total_bono += monto_rent
        comentario_rent = f"{'✅' if porcentaje_rent else '❌'} Rentabilidad del {siniestralidad:.2f}%."
        resultados.append(("📊 Bono Rentabilidad Flotillas", porcentaje_rent, monto_rent, comentario_rent))

 # --- DAÑOS ---
    if ramo == "Daños":
        portal = st.radio("¿Por qué medio se realizó la emisión?", ["Portal", "Mesa de trámites"])
        transportes = st.checkbox("¿Incluye línea de Transportes?")
        prima_mensual = st.number_input("Prima mensual pagada (Daños)", min_value=0.0)
        prima_anual = st.number_input("Prima anual pagada (Daños)", min_value=0.0)
        siniestralidad = st.number_input("Siniestralidad acumulada (%)", min_value=0.0, max_value=100.0)

        datos_ingresados += [
            f"Medio de emisión: {portal}",
            f"Incluye transportes: {'Sí' if transportes else 'No'}",
            f"Prima mensual: {format_currency(prima_mensual)}",
            f"Prima anual: {format_currency(prima_anual)}",
            f"Siniestralidad: {siniestralidad:.2f}%"
        ]

        porcentaje_mensual = 0
        comentario_mensual = ""

        if portal == "Portal":
            if prima_mensual >= 80000:
                porcentaje_mensual = 0.05 if transportes else 0.07
            elif prima_mensual >= 40000:
                porcentaje_mensual = 0.04 if transportes else 0.06
            elif prima_mensual >= 15000:
                porcentaje_mensual = 0.03 if transportes else 0.05
        else:
            if siniestralidad <= 40:
                if prima_mensual >= 200000:
                    porcentaje_mensual = 0.04 if transportes else 0.07
                elif prima_mensual >= 100000:
                    porcentaje_mensual = 0.03 if transportes else 0.06
                elif prima_mensual >= 50000:
                    porcentaje_mensual = 0.02 if transportes else 0.05
            else:
                comentario_mensual = "❌ No aplica bono mensual por siniestralidad > 40% en Mesa de trámites."

        monto_mensual = prima_mensual * porcentaje_mensual
        total_bono += monto_mensual
        if not comentario_mensual:
            comentario_mensual = f"{'✅' if porcentaje_mensual else '❌'} Bono mensual por medio {portal} con prima de {format_currency(prima_mensual)}."
        resultados.append(("📅 Bono Mensual Daños", porcentaje_mensual, monto_mensual, comentario_mensual))

        porcentaje_rec = 0
        comentario_rec = ""

        if portal == "Portal":
            if prima_anual >= 960000:
                porcentaje_rec = 0.05 if transportes else 0.07
            elif prima_anual >= 480000:
                porcentaje_rec = 0.04 if transportes else 0.06
            elif prima_anual >= 180000:
                porcentaje_rec = 0.03 if transportes else 0.05
        else:
            if siniestralidad <= 40:
                if prima_anual >= 2400000:
                    porcentaje_rec = 0.04 if transportes else 0.07
                elif prima_anual >= 1200000:
                    porcentaje_rec = 0.03 if transportes else 0.06
                elif prima_anual >= 600000:
                    porcentaje_rec = 0.02 if transportes else 0.05
            else:
                comentario_rec = "❌ No aplica bono recuperación anual por siniestralidad > 40% en Mesa de trámites."

        monto_rec = prima_anual * porcentaje_rec
        total_bono += monto_rec
        if not comentario_rec:
            comentario_rec = f"{'✅' if porcentaje_rec else '❌'} Bono recuperación anual por medio {portal} con prima de {format_currency(prima_anual)}."
        resultados.append(("📆 Bono Recuperación Anual Daños", porcentaje_rec, monto_rec, comentario_rec))

        porcentaje_rent = 0
        if siniestralidad <= 30:
            porcentaje_rent = 0.035
        elif siniestralidad <= 40:
            porcentaje_rent = 0.025
        elif siniestralidad <= 50:
            porcentaje_rent = 0.015

        monto_rent = prima_anual * porcentaje_rent
        total_bono += monto_rent
        comentario_rent = f"{'✅' if porcentaje_rent else '❌'} Bono rentabilidad con siniestralidad del {siniestralidad:.2f}%."
        resultados.append(("🏠 Bono Rentabilidad Daños", porcentaje_rent, monto_rent, comentario_rent))

   # --- VIDA ---
    if ramo == "Vida":
        primas = st.number_input("Prima Pagada Acumulada Nuevo Negocio Vida (m.n.)", min_value=0.0)
        siniestralidad = st.number_input("Siniestralidad Vida (%)", min_value=0.0, max_value=100.0)

        datos_ingresados += [
            f"Prima Vida: {format_currency(primas)}",
            f"Siniestralidad Vida: {siniestralidad:.2f}%"
        ]

        porcentaje = 0
        if primas >= 6000000 and siniestralidad <= 60:
            porcentaje = 0.06
        elif primas >= 2500000 and siniestralidad <= 60:
            porcentaje = 0.05
        elif primas >= 500000 and siniestralidad <= 60:
            porcentaje = 0.04
        elif primas >= 50000:
            porcentaje = 0.03

        monto = primas * porcentaje
        total_bono += monto
        comentario = f"{'✅' if porcentaje else '❌'} Prima: {format_currency(primas)}, Siniestralidad: {siniestralidad:.2f}%"
        resultados.append(("❤️ Bono Vida CIZ", porcentaje, monto, comentario))

    # --- GMM ---
    if ramo == "GMM":
        primas = st.number_input("Prima Pagada Acumulada Nuevo Negocio GMM (m.n.)", min_value=0.0)
        siniestralidad = st.number_input("Siniestralidad GMM (%)", min_value=0.0, max_value=100.0)

        datos_ingresados += [
            f"Prima GMM: {format_currency(primas)}",
            f"Siniestralidad GMM: {siniestralidad:.2f}%"
        ]

        porcentaje = 0
        if primas >= 6000000 and siniestralidad <= 65:
            porcentaje = 0.03
        elif primas >= 2500000 and siniestralidad <= 65:
            porcentaje = 0.02
        elif primas >= 500000 and siniestralidad <= 65:
            porcentaje = 0.01

        monto = primas * porcentaje
        total_bono += monto
        comentario = f"{'✅' if porcentaje else '❌'} Prima: {format_currency(primas)}, Siniestralidad: {siniestralidad:.2f}%"
        resultados.append(("🩺 Bono GMM CIZ", porcentaje, monto, comentario))

    # --- CONSERVACIÓN ---
    if ramo == "Conservación":
        cartera_vida = st.number_input("Cartera Vida (monto asegurado)", min_value=0.0)
        cartera_gmm = st.number_input("Cartera GMM (monto asegurado)", min_value=0.0)
        conservacion_vida = st.number_input("% Conservación Vida", min_value=0.0, max_value=100.0)
        conservacion_gmm = st.number_input("% Conservación GMM", min_value=0.0, max_value=100.0)
        siniestralidad_vida = st.number_input("Siniestralidad Vida Conservación (%)", min_value=0.0, max_value=100.0)
        siniestralidad_gmm = st.number_input("Siniestralidad GMM Conservación (%)", min_value=0.0, max_value=100.0)

        datos_ingresados += [
            f"Cartera Vida: {format_currency(cartera_vida)}",
            f"Cartera GMM: {format_currency(cartera_gmm)}",
            f"Conservación Vida: {conservacion_vida:.2f}%",
            f"Conservación GMM: {conservacion_gmm:.2f}%",
            f"Siniestralidad Vida Conservación: {siniestralidad_vida:.2f}%",
            f"Siniestralidad GMM Conservación: {siniestralidad_gmm:.2f}%"
        ]

        porcentaje_vida = 0
        if siniestralidad_vida <= 65:
            if conservacion_vida >= 90:
                porcentaje_vida = 0.025
            elif conservacion_vida >= 80:
                porcentaje_vida = 0.015

        monto_vida = cartera_vida * porcentaje_vida
        total_bono += monto_vida
        comentario_vida = f"{'✅' if porcentaje_vida else '❌'} Conservación Vida de {conservacion_vida:.2f}% con siniestralidad {siniestralidad_vida:.2f}%"
        resultados.append(("📘 Bono Conservación Vida", porcentaje_vida, monto_vida, comentario_vida))

        porcentaje_gmm = 0
        if siniestralidad_gmm <= 65:
            if conservacion_gmm >= 90:
                porcentaje_gmm = 0.025
            elif conservacion_gmm >= 80:
                porcentaje_gmm = 0.015

        monto_gmm = cartera_gmm * porcentaje_gmm
        total_bono += monto_gmm
        comentario_gmm = f"{'✅' if porcentaje_gmm else '❌'} Conservación GMM de {conservacion_gmm:.2f}% con siniestralidad {siniestralidad_gmm:.2f}%"
        resultados.append(("📗 Bono Conservación GMM", porcentaje_gmm, monto_gmm, comentario_gmm))

  # --- Mostrar Resultados Finales ---
    if resultados:
        if st.button("Calcular Bonos", key="calcular_bonos_zurich"):
            st.markdown(f"### 🧾 Resultado para {nombre_agente}:")

            st.markdown("#### 📊 Datos Ingresados:")
            for dato in datos_ingresados:
                st.markdown(f"- {dato}")

            st.markdown("#### 💵 Resultados de Bono:")
            for nombre_bono, porcentaje, monto, comentario in resultados:
                st.markdown(f"- **{nombre_bono}:** {format_currency(monto)}")
                st.markdown(f"  - Porcentaje aplicado: **{porcentaje*100:.2f}%**")
                st.markdown(f"  - Explicación: {comentario}")

            st.markdown("#### 🧮 Total del Bono:")
            st.markdown(f"**{format_currency(total_bono)}**")

            st.markdown(
                "<p style='text-align: center; color: gray;'>Aplican restricciones y condiciones conforme al cuaderno oficial de Zurich Seguros 2025.</p>",
                unsafe_allow_html=True
            )
