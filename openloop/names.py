"""
Generates device names used by the API
"""

from random import randint

flowers = """Achillea
Agapanthus
Ageratum
Alpina
Alstroemeria
Amaryllis
Anconitum
Anemone
Anigozanthus
Anthurium
Asparagus
Aster
Astilbe
Banksia
Bellflower
Boronia
Bouvardia
Broom
Buddleia
Bupleurum
Campanula
Candytuft
Carnation
Carthamus
Caspia
Cattleya
Celosia
Chamelaucium
Chrysanthemum
Clarkia
Convallaria
Cordyline
Cosmos
Cornflower
Craspedia
Cymbidium
Daffodil
Dahlia
Dendrobium
Drumstick
Enthusiasm
Feverfew
Freesia
Gardenia
Gerbera
Ginger
Gladiolus
Godetia
Gyp
Heath
Heather
Hippeastrum
Hydrangea
Iris
Jonquil
Knapweed
Larkspur
Lavandula
Lavender
Liatris
Lilac
Lily
Limonium
Lisianthus
Melaleuca
Memosa
Mimosa
Monkshood
Montbretia
Musa
Myrsine
Myrtle
Myrtus
Narcissus
Nephrolepis
Nerine
Nigella
Ornithogalum
Paeonia
Peony
Phalaenopsis
Philodendron
Phlox
Pitt
Pittosporum
Porium
Ranunculus
Rattlesnake
Rose
Safflower
Salix
Sansevieria
Saponaria
Saxicola
Scabiosa
Schinus
Snapdragon
Solidago
Speedwell
Statice
Stenamezon
Stephanotis
Stock
Strawflower
Sunflower
Tailflowers
Thouroughwax
Throatwort
Tracelium
Tuberose
Tulip
Tulipa
Veronica
Wattle
Waxflower
Windflower
Wolfsbane
Zantedeschia
Zinna""".splitlines()

elements = """Actinium
Americium
Argon
Arsenic
Astatine
Barium
Berkelium
Beryllium
Bismuth
Bohrium
Boron
Bromine
Cadmium
Calcium
Californium
Carbon
Cerium
Chlorine
Chromium
Cobalt
Curium
Darmstadtium
Dubnium
Dysprosium
Einsteinium
Erbium
Europium
Fermium
Fluorine
Francium
Gadolinium
Gallium
Germanium
Hafnium
Hassium
Helium
Holmium
Hydrogen
Indium
Iodine
Iridium
Krypton
Lanthanum
Lawrencium
Lithium
Lutetium
Magnesium
Manganese
Meitnerium
Mendelevium
Molybdenum
Neodymium
Neon
Neptunium
Nickel
Niobium
Nitrogen
Nobelium
Osmium
Oxygen
Palladium
Phosphorus
Platinum
Plutonium
Polonium
Praseodymium
Promethium
Protactinium
Radium
Radon
Rhenium
Rhodium
Roentgenium
Rubidium
Ruthenium
Rutherfordium
Samarium
Scandium
Seaborgium
Selenium
Silicon
Strontium
Tantalum
Technetium
Tellurium
Terbium
Thallium
Thorium
Thulium
Titanium
Ununbium
Ununhexium
Ununoctium
Ununpentium
Ununquadium
Ununseptium
Ununtrium
Uranium
Vanadium
Xenon
Ytterbium
Yttrium
Zinc
Zirconium""".splitlines()

def sel_random(arr):
    l = len(arr)-1
    r = randint(0, l)
    return arr[r]

def generate():
    el = sel_random(elements)
    fl = sel_random(flowers)
    return f"{el} {fl}"

if __name__ == "__main__":
    from time import sleep

    while True:
        x = generate()
        print(x)
        sleep(.5)