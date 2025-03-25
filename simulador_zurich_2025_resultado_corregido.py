
import streamlit as st

def format_currency(value):
    return "${:,.2f}".format(value)

st.set_page_config(page_title="Simulador Bonos Zurich 2025", layout="centered")

st.markdown("<h1 style='text-align: center;'>Simulador de Bonos</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>Zurich 2025</h2>", unsafe_allow_html=True)

nombre_agente = st.text_input("Nombre del agente")

if nombre_agente:
    plan = st.selectbox("Selecciona el plan:", ["IMPULZA", "CIZ"])
    if plan == "IMPULZA":
        ramo = st.selectbox("Selecciona el ramo:", ["Auto"])
    else:
        ramo = st.selectbox("Selecciona el ramo:", ["Auto (con siniestralidad)", "Crecimiento"])

    total_bono = 0
    resultados = []
    datos_ingresados = []

    if plan == "CIZ" and ramo == "Auto (con siniestralidad)":
        produccion = st.number_input("Producción Autos 2025", min_value=0.0)
        siniestralidad = st.number_input("Siniestralidad Autos (%)", min_value=0.0, max_value=100.0)
        if siniestralidad <= 65:
            if produccion >= 100000:
                porcentaje = 0.055
            elif produccion >= 50000:
                porcentaje = 0.045
            elif produccion >= 20000:
                porcentaje = 0.035
            else:
                porcentaje = 0.0
        else:
            porcentaje = 0.0
        bono = produccion * porcentaje
        total_bono += bono
        datos_ingresados.append(f"Producción 2025: {format_currency(produccion)}")
        datos_ingresados.append(f"Siniestralidad: {siniestralidad:.2f}%")
        resultados.append(f"Bono de Producción: {porcentaje*100:.2f}% → {format_currency(bono)} → {'✅ Aplica bono del ' + str(int(porcentaje*100)) + '%' if porcentaje > 0 else '❌ No aplica bono.'}")

    elif plan == "CIZ" and ramo == "Crecimiento":
        prod_2024 = st.number_input("Producción 2024", min_value=0.0)
        prod_2025 = st.number_input("Producción 2025", min_value=0.0)
        siniestralidad = st.number_input("Siniestralidad (%)", min_value=0.0, max_value=100.0)
        crecimiento = ((prod_2025 - prod_2024) / prod_2024 * 100) if prod_2024 > 0 else 0.0
        if crecimiento >= 30 and siniestralidad <= 50:
            porcentaje = 0.05
        elif crecimiento >= 10 and siniestralidad <= 50:
            porcentaje = 0.03
        else:
            porcentaje = 0.0
        bono = (prod_2025 - prod_2024) * porcentaje if porcentaje > 0 else 0.0
        total_bono += bono
        datos_ingresados.append(f"Producción 2024: {format_currency(prod_2024)}")
        datos_ingresados.append(f"Producción 2025: {format_currency(prod_2025)}")
        datos_ingresados.append(f"Crecimiento Real: {crecimiento:.2f}%")
        datos_ingresados.append(f"Siniestralidad: {siniestralidad:.2f}%")
        resultados.append(f"Bono de Crecimiento: {porcentaje*100:.2f}% → {format_currency(bono)} → {'✅ Aplica bono del ' + str(int(porcentaje*100)) + '%' if porcentaje > 0 else '❌ No aplica bono.'}")

    if resultados and st.button("Calcular Bonos"):
        st.markdown(f"### 🧾 Resultado para {nombre_agente}")
        st.markdown("#### 📊 Datos Ingresados:")
        for dato in datos_ingresados:
            st.markdown(f"- {dato}")
        st.markdown("#### 💵 Resultados de Bono:")
        for r in resultados:
            st.markdown(f"- {r}")
        st.markdown(f"#### 🧮 Total del Bono:
- {format_currency(total_bono)}")
        st.markdown("<p style='text-align: center; color: gray;'>Aplican restricciones y condiciones conforme al cuaderno oficial de Zurich Seguros 2025.</p>", unsafe_allow_html=True)
