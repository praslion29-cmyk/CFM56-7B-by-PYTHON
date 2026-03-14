# ==============================
# Script HTML dashboard dengan monitoring parameter tambahan
# ==============================

# Spec limit CFM56-7B (estimasi typical cruise / takeoff)
EGT_LIMIT = 920          # °C
OIL_PRESS_LOW = 30       # psi
OIL_PRESS_HIGH = 60      # psi
OIL_TEMP_LIMIT = 165     # °C
VIB_LIMIT = 3.5          # unit
FUEL_FLOW_LIMIT = 6000   # kg/h, asumsi typical max fuel flow per engine

# Sample data
aircraft = "B737-800"
egt = 650
oil_pressure = 45
oil_temp = 140
vibration = 1.5
fuel_flow = 4500

# ==============================
# Function status
# ==============================
def status(value, low_limit, high_limit=None):
    """Return status text with color"""
    if high_limit is None:
        # Only upper limit
        if value > low_limit*0.9 and value <= low_limit:
            return "Approaching Limit 🟡"
        elif value > low_limit:
            return "Warning 🔴"
        else:
            return "Normal 🟢"
    else:
        # Both lower & upper limit
        if value < low_limit or value > high_limit:
            return "Warning 🔴"
        elif (low_limit <= value <= low_limit*1.1) or (value >= high_limit*0.9):
            return "Approaching Limit 🟡"
        else:
            return "Normal 🟢"

# ==============================
# Buat HTML
# ==============================
html_content = f"""
<html>
<head>
<title>Aircraft Engine Monitoring</title>
<style>
body {{
    font-family: Arial, sans-serif;
    margin: 30px;
    background-color: #f4f4f4;
}}
h1 {{
    color: #003366;
}}
p {{
    font-size: 18px;
}}
.status-normal {{ color: green; }}
.status-approaching {{ color: orange; }}
.status-warning {{ color: red; }}
.box {{
    background-color: white;
    padding: 20px;
    border-radius: 10px;
    margin-bottom: 10px;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
}}
</style>
</head>
<body>
<h1>Aircraft Engine Health Monitoring</h1>

<div class="box">
<p>Aircraft : {aircraft}</p>
<p>EGT : {egt} °C - <span class="status-{status(egt, EGT_LIMIT).split()[0].lower()}">{status(egt, EGT_LIMIT)}</span></p>
<p>Oil Pressure : {oil_pressure} PSI - <span class="status-{status(oil_pressure, OIL_PRESS_LOW, OIL_PRESS_HIGH).split()[0].lower()}">{status(oil_pressure, OIL_PRESS_LOW, OIL_PRESS_HIGH)}</span></p>
<p>Oil Temperature : {oil_temp} °C - <span class="status-{status(oil_temp, OIL_TEMP_LIMIT).split()[0].lower()}">{status(oil_temp, OIL_TEMP_LIMIT)}</span></p>
<p>Vibration : {vibration} - <span class="status-{status(vibration, VIB_LIMIT).split()[0].lower()}">{status(vibration, VIB_LIMIT)}</span></p>
<p>Fuel Flow : {fuel_flow} kg/h - <span class="status-{status(fuel_flow, FUEL_FLOW_LIMIT).split()[0].lower()}">{status(fuel_flow, FUEL_FLOW_LIMIT)}</span></p>
</div>

</body>
</html>
"""

# ==============================
# Simpan file
# ==============================
with open("dashboard.html","w") as file:
    file.write(html_content)

print("HTML dashboard berhasil dibuat dengan Fuel Flow dan monitoring parameter tambahan")