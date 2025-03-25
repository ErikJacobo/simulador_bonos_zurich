
import streamlit as st

def format_currency(value):
    return "${:,.2f}".format(value)

st.set_page_config(page_title="Simulador Bonos Zurich 2025", layout="centered")

st.markdown("<h1 style='text-align: center;'>Simulador de Bonos</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>Zurich 2025</h2>", unsafe_allow_html=True)

nombre_agente = st.text_input("Nombre del agente")

if nombre_agente:
    plan = st.selectbox("Selecciona el plan:", ["IMPULZA", "CIZ"])

    ramos_impulza = ["Auto", "Flotillas", "Daños", "Vida + GMM", "Accidentes Personales", "Universal Assistance"]
    ramos_ciz = ["Auto", "Flotillas", "Daños", "Vida", "GMM", "Conservación"]

    if plan == "IMPULZA":
        ramo = st.selectbox("Selecciona el ramo:", ramos_impulza)
    else:
        ramo = st.selectbox("Selecciona el ramo:", ramos_ciz)

    total_bono = 0
    resultados = []
    datos_ingresados = []

    if plan == "IMPULZA":
        if ramo == "Auto":
            pol = st.number_input("Pólizas pagadas mensuales (Auto)", min_value=0)
            if pol >= 5:
                porcentaje = 0.05
                comentario = "✅ Aplica bono del 5%"
            elif pol >= 3:
                porcentaje = 0.04
                comentario = "✅ Aplica bono del 4%"
            elif pol >= 1:
                porcentaje = 0.03
                comentario = "✅ Aplica bono del 3%"
            else:
                porcentaje = 0
                comentario = "❌ No aplica bono"
            monto = pol * 1000 * porcentaje
            total_bono += monto
            datos_ingresados.append(f"Pólizas pagadas: {pol}")
            resultados.append(f"Bono de Producción: {porcentaje*100:.2f}% → {format_currency(monto)} → {comentario}")

        elif ramo == "Flotillas":
            pol = st.number_input("Pólizas pagadas mensuales (Flotillas)", min_value=0)
            if pol >= 7:
                porcentaje = 0.035
                comentario = "✅ Aplica bono del 3.5%"
            elif pol >= 5:
                porcentaje = 0.025
                comentario = "✅ Aplica bono del 2.5%"
            elif pol >= 3:
                porcentaje = 0.015
                comentario = "✅ Aplica bono del 1.5%"
            else:
                porcentaje = 0
                comentario = "❌ No aplica bono"
            monto = pol * 1000 * porcentaje
            total_bono += monto
            datos_ingresados.append(f"Pólizas pagadas: {pol}")
            resultados.append(f"Bono de Producción: {porcentaje*100:.2f}% → {format_currency(monto)} → {comentario}")

        elif ramo == "Daños":
            canal = st.radio("¿Por dónde emite?", ["Portal", "Mesa de trámites"])
            pol = st.number_input("Pólizas pagadas mensuales (Daños)", min_value=0)
            if pol >= 5:
                porcentaje = 0.07
            elif pol >= 3:
                porcentaje = 0.06
            elif pol >= 1:
                porcentaje = 0.03
            else:
                porcentaje = 0
            comentario = f"{'✅ Aplica' if porcentaje > 0 else '❌ No aplica'} bono del {int(porcentaje*100)}%"
            monto = pol * 1000 * porcentaje
            total_bono += monto
            datos_ingresados.append(f"Pólizas: {pol} / Canal: {canal}")
            resultados.append(f"Bono de Daños: {porcentaje*100:.2f}% → {format_currency(monto)} → {comentario}")

        elif ramo == "Vida + GMM":
            pol = st.number_input("Pólizas acumulables (Vida + GMM)", min_value=0)
            if pol >= 11:
                porcentaje = 0.08
                comentario = "✅ Aplica bono 3% GMM + 5% Vida"
            elif pol >= 4:
                porcentaje = 0.06
                comentario = "✅ Aplica bono 2% GMM + 4% Vida"
            elif pol >= 1:
                porcentaje = 0.04
                comentario = "✅ Aplica bono 1% GMM + 3% Vida"
            else:
                porcentaje = 0
                comentario = "❌ No aplica bono"
            monto = pol * 1000 * porcentaje
            total_bono += monto
            datos_ingresados.append(f"Pólizas acumuladas: {pol}")
            resultados.append(f"Bono Vida + GMM: {porcentaje*100:.2f}% → {format_currency(monto)} → {comentario}")

        elif ramo == "Accidentes Personales":
            prima = st.number_input("Prima mensual acumulada (Accidentes)", min_value=0.0)
            if prima >= 1_000_000:
                porcentaje = 0.12
            elif prima >= 400_000:
                porcentaje = 0.08
            elif prima >= 45_000:
                porcentaje = 0.04
            else:
                porcentaje = 0.0
            comentario = f"{'✅ Aplica bono del ' + str(int(porcentaje*100)) + '%' if porcentaje > 0 else '❌ No aplica bono'}"
            monto = prima * porcentaje
            total_bono += monto
            datos_ingresados.append(f"Prima mensual: {format_currency(prima)}")
            resultados.append(f"Bono Accidentes: {porcentaje*100:.2f}% → {format_currency(monto)} → {comentario}")

        elif ramo == "Universal Assistance":
            prima = st.number_input("Prima mensual en USD", min_value=0.0)
            if prima >= 8500:
                porcentaje = 0.10
            elif prima >= 4000:
                porcentaje = 0.07
            elif prima >= 2000:
                porcentaje = 0.05
            else:
                porcentaje = 0
            comentario = f"{'✅ Aplica bono del ' + str(int(porcentaje*100)) + '%' if porcentaje > 0 else '❌ No aplica bono'}"
            monto = prima * porcentaje
            total_bono += monto
            datos_ingresados.append(f"Prima mensual (USD): {format_currency(prima)}")
            resultados.append(f"Bono Universal Assistance: {porcentaje*100:.2f}% → {format_currency(monto)} → {comentario}")

    elif plan == "CIZ":
        if ramo == "Auto":
            prima = st.number_input("Prima mensual Auto", min_value=0.0)
            sin = st.number_input("Siniestralidad (%)", min_value=0.0, max_value=100.0)
            if sin <= 65:
                if prima >= 100_000:
                    porcentaje = 0.055
                elif prima >= 50_000:
                    porcentaje = 0.045
                elif prima >= 20_000:
                    porcentaje = 0.035
                else:
                    porcentaje = 0
            else:
                porcentaje = 0
            comentario = f"{'✅ Aplica bono del ' + str(int(porcentaje*1000)/10) + '%' if porcentaje > 0 else '❌ No aplica bono'}"
            monto = prima * porcentaje
            total_bono += monto
            datos_ingresados.append(f"Prima: {format_currency(prima)} / Siniestralidad: {sin:.2f}%")
            resultados.append(f"Bono Auto: {porcentaje*100:.2f}% → {format_currency(monto)} → {comentario}")

    if resultados and st.button("Calcular Bonos"):
        st.markdown(f"### 🧾 Resultado para {nombre_agente}")
        st.markdown("#### 📊 Datos Ingresados:")
        for dato in datos_ingresados:
            st.markdown(f"- {dato}")
        st.markdown("#### 💵 Resultados de Bono:")
        for r in resultados:
            st.markdown(f"- {r}")
        st.markdown("#### 🧮 Total del Bono:")
        st.markdown(f"- {format_currency(total_bono)}")
        st.markdown("<p style='text-align: center; color: gray;'>Aplican restricciones y condiciones conforme al cuaderno oficial de Zurich Seguros 2025.</p>", unsafe_allow_html=True)
