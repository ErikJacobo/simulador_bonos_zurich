# --- Simulador Zurich 2025 ---
import streamlit as st
from PIL import Image


def format_currency(value):
    return "$ {:,.2f}".format(value)


st.set_page_config(page_title="Simulador Bonos Zurich 2025", layout="centered")

# Logo en la parte superior derecha
col1, col2 = st.columns([5, 1])
with col2:
    logo = Image.open("link logo.jpg")
    st.image(logo, width=100)

st.markdown("<h1 style='text-align: center;'>Simulador de Bonos</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>Zurich 2025</h2>", unsafe_allow_html=True)

nombre_agente = st.text_input("Nombre del agente")
plan = st.selectbox("Selecciona el plan:", ["IMPULZA", "CIZ"])

ramos_impulza = ["Auto", "Flotillas", "Daños", "Vida + GMM", "Accidentes Personales", "Universal Assistance"]
ramos_ciz = ["Auto", "Flotillas", "Daños", "Vida", "GMM", "Conservación"]

ramo = st.selectbox("Selecciona el ramo a simular:", ramos_impulza if plan == "IMPULZA" else ramos_ciz)

resultados = []
datos_ingresados = []
total_bono = 0

# --- PLAN IMPULZA ---
if plan == "IMPULZA":
    if ramo == "Auto":
        pol = st.number_input("Pólizas pagadas mensuales (Auto)", min_value=0)
        if pol >= 5:
            porcentaje = 0.05
            comentario = f"✅ Emitiste {pol} pólizas. Superas el mínimo de 5 para el 5%."
        elif pol >= 3:
            porcentaje = 0.04
            comentario = f"✅ Emitiste {pol} pólizas. En el rango de 3-4, aplica bono del 4%."
        elif pol >= 1:
            porcentaje = 0.03
            comentario = f"✅ Emitiste al menos una póliza. Aplica bono del 3%."
        else:
            porcentaje = 0
            comentario = "❌ No emitiste pólizas. Se requiere mínimo una para aplicar bono."
        monto = pol * 1000 * porcentaje
        total_bono += monto
        datos_ingresados.append(f"Pólizas emitidas: {pol}")
        resultados.append(("🚗 Bono Auto", porcentaje, monto, comentario))

    elif ramo == "Flotillas":
        pol = st.number_input("Pólizas pagadas mensuales (Flotillas)", min_value=0)
        if pol >= 7:
            porcentaje = 0.035
            comentario = "✅ Emitiste 7 o más pólizas. Aplica bono del 3.5%."
        elif pol >= 5:
            porcentaje = 0.025
            comentario = "✅ Emitiste entre 5 y 6 pólizas. Aplica bono del 2.5%."
        elif pol >= 3:
            porcentaje = 0.015
            comentario = "✅ Emitiste entre 3 y 4 pólizas. Aplica bono del 1.5%."
        else:
            porcentaje = 0
            comentario = "❌ Emitiste menos de 3 pólizas. No aplica bono."
        monto = pol * 1000 * porcentaje
        total_bono += monto
        datos_ingresados.append(f"Pólizas Flotillas: {pol}")
        resultados.append(("🚛 Bono Flotillas", porcentaje, monto, comentario))

    elif ramo == "Daños":
        canal = st.radio("¿Por dónde emite?", ["Portal", "Mesa de trámites"])
        pol = st.number_input("Pólizas pagadas mensuales (Daños)", min_value=0)
        if canal == "Portal":
            if pol >= 5:
                porcentaje = 0.07
                comentario = "✅ Emitiste 5+ pólizas vía Portal. Aplica bono del 7%."
            elif pol >= 3:
                porcentaje = 0.06
                comentario = "✅ Emitiste 3-4 pólizas vía Portal. Aplica bono del 6%."
            elif pol >= 1:
                porcentaje = 0.03
                comentario = "✅ Emitiste al menos 1 póliza vía Portal. Aplica bono del 3%."
            else:
                porcentaje = 0
                comentario = "❌ No emitiste pólizas vía Portal."
        else:
            if pol >= 5:
                porcentaje = 0.06
                comentario = "✅ Emitiste 5+ pólizas vía Mesa. Aplica bono del 6%."
            elif pol >= 3:
                porcentaje = 0.05
                comentario = "✅ Emitiste 3-4 pólizas vía Mesa. Aplica bono del 5%."
            elif pol >= 1:
                porcentaje = 0.03
                comentario = "✅ Emitiste al menos 1 póliza vía Mesa. Aplica bono del 3%."
            else:
                porcentaje = 0
                comentario = "❌ No emitiste pólizas vía Mesa."
        monto = pol * 1000 * porcentaje
        total_bono += monto
        datos_ingresados.append(f"Pólizas Daños: {pol} / Canal: {canal}")
        resultados.append(("🏠 Bono Daños", porcentaje, monto, comentario))

    elif ramo == "Vida + GMM":
        pol = st.number_input("Pólizas acumuladas (Vida + GMM)", min_value=0)
        if pol >= 11:
            porcentaje = 0.08
            comentario = "✅ Emitiste 11 o más pólizas. Aplica bono combinado 3% GMM + 5% Vida (8%)."
        elif pol >= 4:
            porcentaje = 0.06
            comentario = "✅ Emitiste entre 4 y 10 pólizas. Aplica bono 2% GMM + 4% Vida (6%)."
        elif pol >= 1:
            porcentaje = 0.04
            comentario = "✅ Emitiste entre 1 y 3 pólizas. Aplica bono 1% GMM + 3% Vida (4%)."
        else:
            porcentaje = 0
            comentario = "❌ No emitiste ninguna póliza. Se requería al menos 1 póliza."
        monto = pol * 1000 * porcentaje
        total_bono += monto
        datos_ingresados.append(f"Pólizas Vida + GMM: {pol}")
        resultados.append(("❤️ Bono Vida + GMM", porcentaje, monto, comentario))

    elif ramo == "Accidentes Personales":
        prima = st.number_input("Prima mensual acumulada (Accidentes)", min_value=0.0)
        if prima >= 1_000_000:
            porcentaje = 0.12
            comentario = "✅ Prima ≥ $1,000,000. Aplica bono del 12%. Máximo permitido."
        elif prima >= 400_000:
            porcentaje = 0.08
            comentario = "✅ Prima entre $400,000 y $999,999. Aplica bono del 8%."
        elif prima >= 45_000:
            porcentaje = 0.04
            comentario = "✅ Prima entre $45,000 y $399,999. Aplica bono del 4%."
        else:
            porcentaje = 0
            comentario = "❌ Prima insuficiente. Mínimo requerido: $45,000."
        monto = prima * porcentaje
        total_bono += monto
        datos_ingresados.append(f"Prima mensual: {format_currency(prima)}")
        resultados.append(("🩺 Bono Accidentes Personales", porcentaje, monto, comentario))

    elif ramo == "Universal Assistance":
        prima = st.number_input("Prima mensual en USD (Universal Assistance)", min_value=0.0)
        if prima >= 8500:
            porcentaje = 0.10
            comentario = "✅ Prima ≥ $8,500 USD. Aplica bono del 10%. Máximo permitido."
        elif prima >= 4000:
            porcentaje = 0.07
            comentario = "✅ Prima entre $4,000 y $8,499 USD. Aplica bono del 7%."
        elif prima >= 2000:
            porcentaje = 0.05
            comentario = "✅ Prima entre $2,000 y $3,999 USD. Aplica bono del 5%."
        else:
            porcentaje = 0
            comentario = "❌ Prima insuficiente. Mínimo requerido: $2,000 USD."
        monto = prima * porcentaje
        total_bono += monto
        datos_ingresados.append(f"Prima mensual (USD): {format_currency(prima)}")
        resultados.append(("🌐 Bono Universal Assistance", porcentaje, monto, comentario))

# --- PLAN CIZ ---
 if plan == "CIZ" and ramo == "Auto":
        prima_mensual = st.number_input("Prima pagada mensual (Auto CIZ)", min_value=0.0)
        prima_anual = st.number_input("Prima pagada anual acumulada (Auto CIZ)", min_value=0.0)
        siniestralidad = st.number_input("Siniestralidad acumulada (%)", min_value=0.0, max_value=100.0)

        datos_ingresados.append(f"Prima mensual: {format_currency(prima_mensual)}")
        datos_ingresados.append(f"Prima anual: {format_currency(prima_anual)}")
        datos_ingresados.append(f"Siniestralidad: {siniestralidad:.2f}%")

        # Bono mensual
        porcentaje_mensual = 0
        comentario_mensual = "❌ No aplica bono mensual."
        if prima_mensual >= 100_000:
            porcentaje_mensual = 0.055
            comentario_mensual = "✅ Prima mensual ≥ $100,000. Aplica bono del 5.5%."
        elif prima_mensual >= 50_000:
            porcentaje_mensual = 0.045
            comentario_mensual = "✅ Prima mensual entre $50,000 y $99,999. Aplica bono del 4.5%."
        elif prima_mensual >= 20_000:
            porcentaje_mensual = 0.035
            comentario_mensual = "✅ Prima mensual entre $20,000 y $49,999. Aplica bono del 3.5%."
        monto_mensual = prima_mensual * porcentaje_mensual
        total_bono += monto_mensual
        resultados.append(("💠 Bono Mensual", porcentaje_mensual, monto_mensual, comentario_mensual))

        # Bono recuperación anual
        porcentaje_recuperacion = 0
        comentario_recuperacion = "❌ No aplica bono recuperación anual."
        if prima_anual >= 1_200_000:
            porcentaje_recuperacion = 0.055
            comentario_recuperacion = "✅ Prima anual ≥ $1,200,000. Aplica bono del 5.5%."
        elif prima_anual >= 600_000:
            porcentaje_recuperacion = 0.045
            comentario_recuperacion = "✅ Prima anual entre $600,000 y $1,199,999. Aplica bono del 4.5%."
        elif prima_anual >= 240_000:
            porcentaje_recuperacion = 0.035
            comentario_recuperacion = "✅ Prima anual entre $240,000 y $599,999. Aplica bono del 3.5%."
        monto_recuperacion = prima_anual * porcentaje_recuperacion
        total_bono += monto_recuperacion
        resultados.append(("💠 Bono Recuperación Anual", porcentaje_recuperacion, monto_recuperacion, comentario_recuperacion))

        # Bono rentabilidad
        porcentaje_rentabilidad = 0
        comentario_rentabilidad = "❌ No aplica bono rentabilidad."
        if siniestralidad <= 40:
            porcentaje_rentabilidad = 0.03
            comentario_rentabilidad = "✅ Siniestralidad ≤ 40%. Aplica bono del 3%."
        elif siniestralidad <= 50:
            porcentaje_rentabilidad = 0.02
            comentario_rentabilidad = "✅ Siniestralidad entre 40.1% y 50%. Aplica bono del 2%."
        elif siniestralidad <= 60:
            porcentaje_rentabilidad = 0.01
            comentario_rentabilidad = "✅ Siniestralidad entre 50.1% y 60%. Aplica bono del 1%."
        monto_rentabilidad = prima_anual * porcentaje_rentabilidad
        total_bono += monto_rentabilidad
        resultados.append(("💠 Bono Rentabilidad Anual", porcentaje_rentabilidad, monto_rentabilidad, comentario_rentabilidad))

       # --- CIZ: Flotillas ---
    if plan == "CIZ" and ramo == "Flotillas":
        prima_mensual = st.number_input("Prima pagada mensual (Flotillas CIZ)", min_value=0.0)
        prima_anual = st.number_input("Prima pagada anual acumulada (Flotillas CIZ)", min_value=0.0)
        siniestralidad = st.number_input("Siniestralidad acumulada (%)", min_value=0.0, max_value=100.0)

        datos_ingresados.append(f"Prima mensual Flotillas: {format_currency(prima_mensual)}")
        datos_ingresados.append(f"Prima anual Flotillas: {format_currency(prima_anual)}")
        datos_ingresados.append(f"Siniestralidad: {siniestralidad:.2f}%")

        # Bono mensual
        porcentaje_mensual = 0
        comentario_mensual = "❌ No aplica bono mensual."
        if prima_mensual >= 150_000:
            porcentaje_mensual = 0.045
            comentario_mensual = "✅ Prima mensual ≥ $150,000. Aplica bono del 4.5%."
        elif prima_mensual >= 100_000:
            porcentaje_mensual = 0.035
            comentario_mensual = "✅ Prima mensual entre $100,000 y $149,999. Aplica bono del 3.5%."
        elif prima_mensual >= 30_000:
            porcentaje_mensual = 0.025
            comentario_mensual = "✅ Prima mensual entre $30,000 y $99,999. Aplica bono del 2.5%."
        monto_mensual = prima_mensual * porcentaje_mensual
        total_bono += monto_mensual
        resultados.append(("🚌 Bono Mensual Flotillas", porcentaje_mensual, monto_mensual, comentario_mensual))

        # Bono recuperación anual
        porcentaje_recuperacion = 0
        comentario_recuperacion = "❌ No aplica bono recuperación anual."
        if prima_anual >= 1_800_000:
            porcentaje_recuperacion = 0.045
            comentario_recuperacion = "✅ Prima anual ≥ $1,800,000. Aplica bono del 4.5%."
        elif prima_anual >= 1_200_000:
            porcentaje_recuperacion = 0.035
            comentario_recuperacion = "✅ Prima anual entre $1,200,000 y $1,799,999. Aplica bono del 3.5%."
        elif prima_anual >= 360_000:
            porcentaje_recuperacion = 0.025
            comentario_recuperacion = "✅ Prima anual entre $360,000 y $1,199,999. Aplica bono del 2.5%."
        monto_recuperacion = prima_anual * porcentaje_recuperacion
        total_bono += monto_recuperacion
        resultados.append(("🚌 Bono Recuperación Anual Flotillas", porcentaje_recuperacion, monto_recuperacion, comentario_recuperacion))

        # Bono rentabilidad
        porcentaje_rentabilidad = 0
        comentario_rentabilidad = "❌ No aplica bono rentabilidad."
        if siniestralidad <= 45:
            porcentaje_rentabilidad = 0.04
            comentario_rentabilidad = "✅ Siniestralidad ≤ 45%. Aplica bono del 4%."
        elif siniestralidad <= 50:
            porcentaje_rentabilidad = 0.025
            comentario_rentabilidad = "✅ Siniestralidad entre 45.1% y 50%. Aplica bono del 2.5%."
        elif siniestralidad <= 55:
            porcentaje_rentabilidad = 0.015
            comentario_rentabilidad = "✅ Siniestralidad entre 50.1% y 55%. Aplica bono del 1.5%."
        monto_rentabilidad = prima_anual * porcentaje_rentabilidad
        total_bono += monto_rentabilidad
        resultados.append(("🚌 Bono Rentabilidad Anual Flotillas", porcentaje_rentabilidad, monto_rentabilidad, comentario_rentabilidad))


    elif ramo == "Daños":
        prod_2024 = st.number_input("Producción 2024 (Daños)", min_value=0.0)
        prod_2025 = st.number_input("Producción 2025 (Daños)", min_value=0.0)
        sin = st.number_input("Siniestralidad Daños (%)", min_value=0.0, max_value=100.0)
        crecimiento = ((prod_2025 - prod_2024) / prod_2024) * 100 if prod_2024 > 0 else 0

        datos_ingresados.extend([
            f"Producción 2024: {format_currency(prod_2024)}",
            f"Producción 2025: {format_currency(prod_2025)}",
            f"Crecimiento Real: {crecimiento:.2f}%",
            f"Siniestralidad: {sin:.2f}%"
        ])

        if sin <= 60:
            if prod_2025 >= 100_000:
                porcentaje = 0.06
                comentario = "✅ Producción ≥ $100,000 y siniestralidad ≤ 60%. Aplica bono del 6%."
            elif prod_2025 >= 50_000:
                porcentaje = 0.04
                comentario = "✅ Producción entre $50,000 y $99,999. Aplica bono del 4%."
            elif prod_2025 >= 20_000:
                porcentaje = 0.02
                comentario = "✅ Producción entre $20,000 y $49,999. Aplica bono del 2%."
            else:
                porcentaje = 0
                comentario = "❌ Producción menor a $20,000. No aplica bono."
        else:
            porcentaje = 0
            comentario = f"❌ Siniestralidad de {sin:.2f}% excede el máximo permitido de 60%."

        monto = prod_2025 * porcentaje
        total_bono += monto
        resultados.append(("🏠 Bono Daños CIZ", porcentaje, monto, comentario))

    elif ramo == "Vida":
        primas = st.number_input("Primas pagadas mensuales (Vida)", min_value=0.0)
        datos_ingresados.append(f"Primas Vida: {format_currency(primas)}")
        if primas >= 50_000:
            porcentaje = 0.06
            comentario = "✅ Primas ≥ $50,000. Aplica bono del 6%."
        elif primas >= 30_000:
            porcentaje = 0.04
            comentario = "✅ Primas entre $30,000 y $49,999. Aplica bono del 4%."
        elif primas >= 10_000:
            porcentaje = 0.02
            comentario = "✅ Primas entre $10,000 y $29,999. Aplica bono del 2%."
        else:
            porcentaje = 0
            comentario = "❌ Primas insuficientes. Mínimo requerido: $10,000."
        monto = primas * porcentaje
        total_bono += monto
        resultados.append(("❤️ Bono Vida CIZ", porcentaje, monto, comentario))

    elif ramo == "GMM":
        primas = st.number_input("Primas pagadas mensuales (GMM)", min_value=0.0)
        datos_ingresados.append(f"Primas GMM: {format_currency(primas)}")
        if primas >= 50_000:
            porcentaje = 0.05
            comentario = "✅ Primas ≥ $50,000. Aplica bono del 5%."
        elif primas >= 30_000:
            porcentaje = 0.03
            comentario = "✅ Primas entre $30,000 y $49,999. Aplica bono del 3%."
        elif primas >= 10_000:
            porcentaje = 0.01
            comentario = "✅ Primas entre $10,000 y $29,999. Aplica bono del 1%."
        else:
            porcentaje = 0
            comentario = "❌ Primas insuficientes. Mínimo requerido: $10,000."
        monto = primas * porcentaje
        total_bono += monto
        resultados.append(("🩹 Bono GMM CIZ", porcentaje, monto, comentario))

    elif ramo == "Conservación":
        cartera = st.number_input("Cartera conservada anual (CIZ)", min_value=0.0)
        datos_ingresados.append(f"Cartera conservada: {format_currency(cartera)}")
        if cartera >= 200_000:
            porcentaje = 0.04
            comentario = "✅ Conservación ≥ $200,000. Aplica bono del 4%."
        elif cartera >= 100_000:
            porcentaje = 0.03
            comentario = "✅ Conservación entre $100,000 y $199,999. Aplica bono del 3%."
        elif cartera >= 50_000:
            porcentaje = 0.02
            comentario = "✅ Conservación entre $50,000 y $99,999. Aplica bono del 2%."
        else:
            porcentaje = 0
            comentario = "❌ Conservación insuficiente. Mínimo requerido: $50,000."
        monto = cartera * porcentaje
        total_bono += monto
        resultados.append(("💼 Bono Conservación CIZ", porcentaje, monto, comentario))


    # --- Resultados Finales ---
    if resultados:
        if st.button("Calcular Bonos", key=f"calcular_bonos_zurich_{plan}_{ramo}"):
            st.markdown(f"""
                <h3>🧾 Resultado para {nombre_agente}:</h3>
                <h4>📊 Datos Ingresados:</h4>
                <ul>
            """, unsafe_allow_html=True)

            for dato in datos_ingresados:
                st.markdown(f"<li>{dato}</li>", unsafe_allow_html=True)

            st.markdown("</ul>", unsafe_allow_html=True)
            st.markdown("<h4>💵 Resultados de Bono:</h4>", unsafe_allow_html=True)

            for nombre_bono, porcentaje, monto, comentario in resultados:
                st.markdown(f'''
                    <div style='margin-bottom: 10px;'>
                        <strong>{nombre_bono}:</strong> {format_currency(monto)}<br>
                        <span style='color: gray;'>Bono de {nombre_bono}: {porcentaje*100:.2f}% → {format_currency(monto)}</span> ✅ {comentario}
                    </div>
                ''', unsafe_allow_html=True)

            st.markdown("<h4>🧮 Total del Bono:</h4>", unsafe_allow_html=True)
            st.markdown(f"<strong style='font-size: 24px;'>{format_currency(total_bono)}</strong>", unsafe_allow_html=True)

    st.markdown(
        "<p style='text-align: center; color: gray;'>Aplican restricciones y condiciones conforme al cuaderno oficial de Zurich Seguros 2025.</p>",
        unsafe_allow_html=True
    )

