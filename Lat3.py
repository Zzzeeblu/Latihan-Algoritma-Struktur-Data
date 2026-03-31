class Kendaraan:
    def __init__(self, merek, model):
        self.merek = merek
        self.model = model

    def __str__(self):
        return f"Kendaraan: {self.merek} {self.model}"
    
class Mobil(Kendaraan):
    def __init__(self, merek, model, jumlah_pintu):
        super().__init__(merek, model) 
        self.jumlah_pintu = jumlah_pintu 
    def __str__(self):
        return f"Mobil: {self.merek} {self.model} (Jumlah Pintu: {self.jumlah_pintu})"

class SepedaMotor(Kendaraan):
    def __init__(self, merek, model, jenis_transmisi):
        super().__init__(merek, model)
        self.jenis_transmisi = jenis_transmisi

    def __str__(self):
        return f"Sepeda Motor: {self.merek} {self.model} (Transmisi: {self.jenis_transmisi})"


print("Informasi Kendaraan")
mobil1 = Mobil("Toyota", "Hilux", 4)
print(mobil1)
motor1 = SepedaMotor("Honda", "Vario", "Matic")
print(motor1)
