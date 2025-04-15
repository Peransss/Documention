# Superclass
class Hewan:
    def suara(self):
        print("Hewan bersuara")

# Subclass
class Kucing(Hewan):
    def suara(self):
        print("Meong...")

    def garuk(self):
        print("Kucing menggaruk")

# Upcasting (Objek Kucing diperlakukan sebagai Hewan)
hewan1: Hewan = Kucing()  # Upcasting secara implisit
hewan1.suara()  # Output: Meong...

# Downcasting (Mengubah kembali ke Kucing)
if isinstance(hewan1, Kucing):
    hewan2: Kucing = hewan1  # Downcasting secara eksplisit
    hewan2.suara()  # Output: Kucing menggaruk
