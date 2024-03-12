import json
import requests

empleadoNuevo = {
    "codigo": 433,
    "nombres": "sergio",
    "apellidos": "gomez"
}

obtener = requests.post("http://172.16.100.115:3000", data=json.dumps(empleadoNuevo))
print(obtener)
