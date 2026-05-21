import time

class UMASystem:
    def __init__(self, owner_name, preferred_title):
        self.owner = owner_name
        self.title = preferred_title
        self.security_lock = True
        
    def boot_system(self):
        print(f"[{time.strftime('%H:%M:%S')}] Iniciando UMA OS v1 (Estructura Base)...")
        time.sleep(1)
        print(f"UMA: Bienvenido de vuelta, {self.title}. Sistema operativo activo y listo en España.")
        
    def verify_security(self, has_ring, pulse_bpm):
        print(f"\n[{time.strftime('%H:%M:%S')}] Escaneando protocolo simbiótico...")
        time.sleep(1.5)
        
        if not has_ring:
            print("CRÍTICO: Anillo de seguridad no detectado. Bloqueo total del núcleo.")
            self.security_lock = True
            return "SISTEMA_BLOQUEADO"
            
        elif has_ring and pulse_bpm > 120:
            print("ALERTA: Pulsaciones elevadas detectadas bajo validación.")
            print("UMA: Activando Interfaz Espejo de Respaldo por Seguridad.")
            self.security_lock = False
            return "INTERFAZ_ESPEJO_FALSA"
            
        else:
            print("UMA: Autenticación exitosa. Desbloqueando Núcleo Principal.")
            self.security_lock = False
            return "ACCESO_CONCEDIDO_CORE"

# --- EJECUCIÓN DE PRUEBA ---
if __name__ == "__main__":
    uma = UMASystem(owner_name="Creador", preferred_title="Señor")
    uma.boot_system()
    
    # Probamos el modo bajo presión simulando pulso alterado
    estado = uma.verify_security(has_ring=True, pulse_bpm=135)
    print(f"Estado de la pantalla: {estado}")
