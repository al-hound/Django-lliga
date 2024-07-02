from django.core.management.base import BaseCommand
from faker import Faker
from datetime import timedelta
from random import randint

from League.models import Lliga, Equip, Jugador, Partit

faker = Faker(["es_CA", "es_ES"])

class Command(BaseCommand):
    help = 'Crea una lliga amb equips i jugadors'
    
    def add_arguments(self, parser):
        parser.add_argument('titol_lliga', nargs=1, type=str)
    
    def handle(self, *args, **options):
        titol_lliga = options['titol_lliga'][0]
        lliga = Lliga.objects.filter(nom=titol_lliga)
        if lliga.exists():
            self.stdout.write(self.style.ERROR("Aquesta lliga ja està creada. Posa un altre nom."))
            return
    
        self.stdout.write("Creem la nova lliga: {}".format(titol_lliga))
        lliga = Lliga(nom=titol_lliga, temporada="2023-2024")  # Ejemplo de temporada
        lliga.save()
    
        prefixos = ["RCD", "Athletic", "", "Deportivo", "Unión Deportiva"]
        for i in range(20):
            ciutat = faker.city()
            prefix = prefixos[randint(0, len(prefixos)-1)]
            if prefix:
                prefix += " "
            nom_equip = prefix + ciutat
            equip = Equip(ciutat=ciutat, nom=nom_equip, lliga=lliga)
            equip.save()
    
            self.stdout.write("Creem jugadors de l'equip " + nom_equip)
            for j in range(25):
                nom_jugador = faker.name()
                posicio = "Delantero"  # ejemplo de posición
                data_naixement = faker.date_of_birth(minimum_age=18, maximum_age=40)
                jugador = Jugador(nom=nom_jugador, posicio=posicio, data_naixement=data_naixement, equip=equip)
                jugador.save()
    
        self.stdout.write("Creem partits de la lliga")
        equips = list(lliga.equip_set.all())
        for local in equips:
            for visitant in equips:
                if local != visitant:
                    partit = Partit(local=local, visitant=visitant, lliga=lliga)
                    partit.save()
