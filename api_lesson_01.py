import json
data = '{"city" : "Hyderabad", "pollutant" :"PM2.5", "value":42.5, "unit" : "µg/m³"}'
python_data = json.loads(data)

print(python_data["city"])
print(python_data["pollutant"])
print(python_data["value"])
print(python_data["unit"])