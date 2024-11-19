import streamlit as st
from datetime import datetime
import pytz

# Ciudades y sus zonas horarias
cities = {
    "Madrid": "Europe/Madrid",
    "San Francisco": "America/Los_Angeles",
    "New York": "America/New_York",
    "Lima": "America/Lima",
    "Dubai": "Asia/Dubai",
    "Bali": "Asia/Makassar",
}

# Función para determinar la actividad basada en la hora
def get_activity(hour):
    if 8 <= hour < 9:
        return "Se están preparando para trabajar."
    elif 9 <= hour < 13:
        return "Están trabajando."
    elif 13 <= hour < 14:
        return "Están comiendo."
    elif 14 <= hour < 18:
        return "Están trabajando."
    else:
        return "Están descansando."

# Interfaz de la app
st.title("Horario Global")

if st.button("Calcular Hora"):
    for city, tz in cities.items():
        local_time = datetime.now(pytz.timezone(tz))
        hour = local_time.hour
        activity = get_activity(hour)
        
        st.subheader(city)
        st.write(f"Hora local: {local_time.strftime('%H:%M')}")
        st.write(f"Actividad: {activity}")
