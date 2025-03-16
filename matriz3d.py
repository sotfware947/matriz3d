# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Días de la semana (7 días)
# Tercera dimensión: Semanas (3 semanas)
temperaturas = [
    [   # Guayaquil
        [   # Semana 1
            {"day": "Lunes", "temp": 75},
            {"day": "Martes", "temp": 84},
            {"day": "Miércoles", "temp": 85},
            {"day": "Jueves", "temp": 73},
            {"day": "Viernes", "temp": 84},
            {"day": "Sábado", "temp": 88},
            {"day": "Domingo", "temp": 93}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 72},
            {"day": "Martes", "temp": 75},
            {"day": "Miércoles", "temp": 82},
            {"day": "Jueves", "temp": 80},
            {"day": "Viernes", "temp": 85},
            {"day": "Sábado", "temp": 89},
            {"day": "Domingo", "temp": 92}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 70},
            {"day": "Martes", "temp": 82},
            {"day": "Miércoles", "temp": 85},
            {"day": "Jueves", "temp": 80},
            {"day": "Viernes", "temp": 86},
            {"day": "Sábado", "temp": 90},
            {"day": "Domingo", "temp": 94}
        ]
    ],
    [   # Manabi
        [   # Semana 1
            {"day": "Lunes", "temp": 64},
            {"day": "Martes", "temp": 66},
            {"day": "Miércoles", "temp": 68},
            {"day": "Jueves", "temp": 70},
            {"day": "Viernes", "temp": 72},
            {"day": "Sábado", "temp": 75},
            {"day": "Domingo", "temp": 78}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 61},
            {"day": "Martes", "temp": 64},
            {"day": "Miércoles", "temp": 78},
            {"day": "Jueves", "temp": 72},
            {"day": "Viernes", "temp": 75},
            {"day": "Sábado", "temp": 78},
            {"day": "Domingo", "temp": 80}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 60},
            {"day": "Martes", "temp": 64},
            {"day": "Miércoles", "temp": 68},
            {"day": "Jueves", "temp": 72},
            {"day": "Viernes", "temp": 74},
            {"day": "Sábado", "temp": 78},
            {"day": "Domingo", "temp": 82}
        ]
    ],
    [   # Quito
        [   # Semana 1
            {"day": "Lunes", "temp": 90},
            {"day": "Martes", "temp": 94},
            {"day": "Miércoles", "temp": 95},
            {"day": "Jueves", "temp": 93},
            {"day": "Viernes", "temp": 89},
            {"day": "Sábado", "temp": 87},
            {"day": "Domingo", "temp": 85}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 89},
            {"day": "Martes", "temp": 92},
            {"day": "Miércoles", "temp": 95},
            {"day": "Jueves", "temp": 92},
            {"day": "Viernes", "temp": 87},
            {"day": "Sábado", "temp": 82},
            {"day": "Domingo", "temp": 80}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 90},
            {"day": "Martes", "temp": 92},
            {"day": "Miércoles", "temp": 95},
            {"day": "Jueves", "temp": 91},
            {"day": "Viernes", "temp": 89},
            {"day": "Sábado", "temp": 85},
            {"day": "Domingo", "temp": 82}
        ]
    ]
]

def calcular_promedio_temperatura(temperaturas, ciudad_idx):
    ciudades = ["Guayaquil", "Manabi", "Quito"]
    # escoger que cuidad se quiere calcular el promedio de temperaturas 0 guayaquil , 1 manabi , 2 quito
    ciudad = temperaturas[ciudad_idx]
    for semana_idx, semana in enumerate(ciudad):
        suma_temperaturas = sum([dia["temp"] for dia in semana])
        promedio = suma_temperaturas / len(semana)
        print(f"Promedio de temperaturas en {ciudades[ciudad_idx]}, Semana {semana_idx + 1}: {promedio:.2f} grados")


calcular_promedio_temperatura(temperaturas, 2)