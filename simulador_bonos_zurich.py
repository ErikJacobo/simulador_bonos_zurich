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
        mensual = st.number_input("Prima Pagada Mensual (m.n.)", min_value=0.0)
        anual = st.number_input("Prima Pagada Anual (m.n.)", min_value=0.0)
        siniestralidad = st.number_input("% Siniestralidad Acumulada", min_value=0.0, max_value=100.0)

        datos_ingresados += [
            f"Prima Mensual: {format_currency(mensual)}",
            f"Prima Anual: {format_currency(anual)}",
            f"Siniestralidad: {siniestralidad:.2f}%"
        ]

        porcentaje = 0
        if mensual >= 100000:
            porcentaje = 0.055
        elif mensual >= 50000:
            porcentaje = 0.045
        elif mensual >= 20000:
            porcentaje = 0.035
        monto = mensual * porcentaje
        total_bono += monto
        resultados.append(("🚗 Bono Mensual Auto", porcentaje, monto, f"Bono mensual según prima: {format_currency(mensual)}"))

        porcentaje = 0
        if anual >= 1200000:
            porcentaje = 0.055
        elif anual >= 600000:
            porcentaje = 0.045
        elif anual >= 240000:
            porcentaje = 0.035
        monto = anual * porcentaje
        total_bono += monto
        resultados.append(("📅 Bono Recuperación Anual Auto", porcentaje, monto, f"Bono recuperación según prima anual: {format_currency(anual)}"))

        porcentaje = 0
        if siniestralidad <= 40:
            porcentaje = 0.03
        elif siniestralidad <= 50:
            porcentaje = 0.02
        elif siniestralidad <= 60:
            porcentaje = 0.01
        monto = anual * porcentaje
        total_bono += monto
        resultados.append(("📈 Bono Rentabilidad Auto", porcentaje, monto, f"Rentabilidad del {siniestralidad:.2f}%"))

    # --- FLOTILLAS ---
    elif ramo == "Flotillas":
        mensual = st.number_input("Prima Pagada Mensual Flotillas (m.n.)", min_value=0.0)
        anual = st.number_input("Prima Pagada Anual Flotillas (m.n.)", min_value=0.0)
        siniestralidad = st.number_input("% Siniestralidad Acumulada Flotillas", min_value=0.0, max_value=100.0)

        datos_ingresados += [
            f"Prima Mensual Flotillas: {format_currency(mensual)}",
            f"Prima Anual Flotillas: {format_currency(anual)}",
            f"Siniestralidad Flotillas: {siniestralidad:.2f}%"
        ]

        porcentaje = 0
        if mensual >= 150000:
            porcentaje = 0.045
        elif mensual >= 100000:
            porcentaje = 0.035
        elif mensual >= 30000:
            porcentaje = 0.025
        monto = mensual * porcentaje
        total_bono += monto
        resultados.append(("🚐 Bono Mensual Flotillas", porcentaje, monto, f"Bono mensual según prima flotillas: {format_currency(mensual)}"))

        porcentaje = 0
        if anual >= 1800000:
            porcentaje = 0.045
        elif anual >= 1200000:
            porcentaje = 0.035
        elif anual >= 360000:
            porcentaje = 0.025
        monto = anual * porcentaje
        total_bono += monto
        resultados.append(("📅 Bono Recuperación Anual Flotillas", porcentaje, monto, f"Bono recuperación según prima anual: {format_currency(anual)}"))

        porcentaje = 0
        if siniestralidad <= 45:
            porcentaje = 0.04
        elif siniestralidad <= 50:
            porcentaje = 0.025
        elif siniestralidad <= 55:
            porcentaje = 0.015
        monto = anual * porcentaje
        total_bono += monto
        resultados.append(("📈 Bono Rentabilidad Flotillas", porcentaje, monto, f"Rentabilidad del {siniestralidad:.2f}%"))

    # --- DAÑOS ---
    elif ramo == "Daños":
        canal = st.radio("Canal de contratación", ["Portal", "Mesa de trámites"])
        mensual = st.number_input("Prima Pagada Mensual Daños", min_value=0.0)
        anual = st.number_input("Prima Pagada Anual Daños", min_value=0.0)
        siniestralidad = st.number_input("% Siniestralidad Acumulada Daños", min_value=0.0, max_value=100.0)

        datos_ingresados += [
            f"Canal: {canal}",
            f"Prima Mensual Daños: {format_currency(mensual)}",
            f"Prima Anual Daños: {format_currency(anual)}",
            f"Siniestralidad Daños: {siniestralidad:.2f}%"
        ]

        porcentaje = 0
        if canal == "Portal":
            if mensual >= 80000:
                porcentaje = 0.07
            elif mensual >= 40000:
                porcentaje = 0.06
            elif mensual >= 15000:
                porcentaje = 0.05
        else:
            if mensual >= 200000:
                porcentaje = 0.07
            elif mensual >= 100000:
                porcentaje = 0.06
            elif mensual >= 50000:
                porcentaje = 0.05
        monto = mensual * porcentaje
        total_bono += monto
        resultados.append(("🏢 Bono Mensual Daños", porcentaje, monto, f"Canal: {canal} con prima mensual de {format_currency(mensual)}"))

        porcentaje = 0
        if canal == "Portal":
            if anual >= 960000:
                porcentaje = 0.07
            elif anual >= 480000:
                porcentaje = 0.06
            elif anual >= 180000:
                porcentaje = 0.05
        else:
            if anual >= 2400000:
                porcentaje = 0.07
            elif anual >= 1200000:
                porcentaje = 0.06
            elif anual >= 600000:
                porcentaje = 0.05
        monto = anual * porcentaje
        total_bono += monto
        resultados.append(("📅 Bono Recuperación Anual Daños", porcentaje, monto, f"Canal: {canal} con prima anual de {format_currency(anual)}"))

        porcentaje = 0
        if siniestralidad <= 30:
            porcentaje = 0.035
        elif siniestralidad <= 40:
            porcentaje = 0.025
        elif siniestralidad <= 50:
            porcentaje = 0.015
        monto = anual * porcentaje
        total_bono += monto
        resultados.append(("📈 Bono Rentabilidad Daños", porcentaje, monto, f"Rentabilidad del {siniestralidad:.2f}%"))

 # --- VIDA ---
    if ramo == "Vida":
        primas = st.number_input("Prima Pagada Acumulada Nuevo Negocio Vida (m.n.)", min_value=0.0)
        siniestralidad = st.number_input("Siniestralidad Vida (%)", min_value=0.0, max_value=100.0)

        datos_ingresados += [
            f"Prima Vida: {format_currency(primas)}",
            f"Siniestralidad Vida: {siniestralidad:.2f}%"
        ]

        porcentaje = 0
        if primas >= 50000:
            if siniestralidad <= 60:
                porcentaje = 0.06
        elif primas >= 30000:
            if siniestralidad <= 60:
                porcentaje = 0.04
        elif primas >= 10000:
            if siniestralidad <= 60:
                porcentaje = 0.02

        monto = primas * porcentaje
        total_bono += monto
        resultados.append(("❤️ Bono Vida CIZ", porcentaje, monto, f"Prima: {format_currency(primas)}, Siniestralidad: {siniestralidad:.2f}%"))

   # --- GMM ---
    if ramo == "GMM":
        primas = st.number_input("Prima Pagada Acumulada Nuevo Negocio GMM (m.n.)", min_value=0.0)
        siniestralidad = st.number_input("Siniestralidad GMM (%)", min_value=0.0, max_value=100.0)

        datos_ingresados += [
            f"Prima GMM: {format_currency(primas)}",
            f"Siniestralidad GMM: {siniestralidad:.2f}%"
        ]

        porcentaje = 0
        if primas >= 50000:
            if siniestralidad <= 65:
                porcentaje = 0.05
        elif primas >= 30000:
            if siniestralidad <= 65:
                porcentaje = 0.03
        elif primas >= 10000:
            if siniestralidad <= 65:
                porcentaje = 0.01

        monto = primas * porcentaje
        total_bono += monto
        resultados.append(("🩺 Bono GMM CIZ", porcentaje, monto, f"Prima: {format_currency(primas)}, Siniestralidad: {siniestralidad:.2f}%"))

# --- CONSERVACIÓN ---
    if ramo == "Conservación":
        vida_conservacion = st.number_input("% Conservación Vida", min_value=0.0, max_value=100.0)
        gmm_conservacion = st.number_input("% Conservación GMM", min_value=0.0, max_value=100.0)
        sin_v = st.number_input("Siniestralidad Vida (%)", min_value=0.0, max_value=100.0)
        sin_gmm = st.number_input("Siniestralidad GMM (%)", min_value=0.0, max_value=100.0)

        datos_ingresados.append(f"Conservación Vida: {vida_conservacion:.2f}%")
        datos_ingresados.append(f"Conservación GMM: {gmm_conservacion:.2f}%")
        datos_ingresados.append(f"Siniestralidad Vida: {sin_v:.2f}%")
        datos_ingresados.append(f"Siniestralidad GMM: {sin_gmm:.2f}%")

        porcentaje_vida = 0
        if sin_v <= 65:
            if vida_conservacion >= 90:
                porcentaje_vida = 0.025
            elif vida_conservacion >= 80:
                porcentaje_vida = 0.015

        monto_vida = 100000 * porcentaje_vida
        total_bono += monto_vida
        comentario_vida = f"{'✅' if porcentaje_vida else '❌'} Conservación Vida de {vida_conservacion:.2f}% → bono del {porcentaje_vida*100:.2f}%."
        resultados.append(("📘 Bono Conservación Vida", porcentaje_vida, monto_vida, comentario_vida))

        porcentaje_gmm = 0
        if sin_gmm <= 65:
            if gmm_conservacion >= 90:
                porcentaje_gmm = 0.025
            elif gmm_conservacion >= 80:
                porcentaje_gmm = 0.015

        monto_gmm = 100000 * porcentaje_gmm
        total_bono += monto_gmm
        comentario_gmm = f"{'✅' if porcentaje_gmm else '❌'} Conservación GMM de {gmm_conservacion:.2f}% → bono del {porcentaje_gmm*100:.2f}%."
        resultados.append(("📗 Bono Conservación GMM", porcentaje_gmm, monto_gmm, comentario_gmm))

    if resultados and st.button("Calcular Bonos", key="calcular_bonos_zurich"):
        st.markdown(f"### 🧾 Resultado para {nombre_agente}")

        if datos_ingresados:
            st.markdown("#### 📊 Datos Ingresados:")
            for dato in datos_ingresados:
                st.markdown(f"- {dato}")

        if resultados:
            st.markdown("#### 💵 Resultados de Bono:")
            for nombre_bono, porcentaje, monto, comentario in resultados:
                st.markdown(f'''
                    <div style='margin-bottom: 10px;'>
                        <strong>{nombre_bono}:</strong><br>
                        Porcentaje aplicado: <code>{porcentaje*100:.2f}%</code><br>
                        Monto ganado: <code>{format_currency(monto)}</code><br>
                        Explicación: {comentario}
                    </div>
                ''', unsafe_allow_html=True)

            st.markdown("#### 🧮 Total del Bono:")
            st.markdown(f"<code>{format_currency(total_bono)}</code>", unsafe_allow_html=True)
        else:
            st.warning("No se generó ningún bono con los datos ingresados.")

        st.markdown(
            "<p style='text-align: center; color: gray;'>Aplican restricciones y condiciones conforme al cuaderno oficial de Zurich Seguros 2025.</p>",
            unsafe_allow_html=True
        )
