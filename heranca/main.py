class Animal:

    # ===== VARIÁVEIS =====
    vivo = True
    # ===== VARIÁVEIS =====

    # ===== MÉTODOS =====

    # ======================================
    def comer(self):
        print ('Este animal está comendo' )
    # ======================================
    def dormir(self):
        print ('Este animal está dormindo')
    # ======================================

    # ===== MÉTODOS =====

# ===== SUB CLASSES =====

# ======================================
class Cachorro (Animal):
    # ===== MÉTODOS =====
    def correr(self):
        print ('Este cachorro está correndo')
    def comer(self):
        print ('Este cachorro está comendo ração')
    # ===== MÉTODOS =====
# ======================================
class Peixe (Animal):
    # ===== MÉTODOS =====
    def nadar(self):
        print ('Este peixe está nadando')
    # ===== MÉTODOS =====
# ======================================
class Gaviao (Animal):
    # ===== MÉTODOS =====
    def voar(self):
        print ('Este gavião está voando')
    # ===== MÉTODOS =====
# ======================================

# ===== SUB CLASSES =====

cachorro = Cachorro()
peixe    = Peixe()
gaviao   = Gaviao()

cachorro.correr()
cachorro.comer()
peixe.nadar()
gaviao.voar()