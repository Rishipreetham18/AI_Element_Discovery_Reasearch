import csv

class Element:
    def __init__(self, AtomicNumber, Element, Symbol, AtomicMass, NumberOfNeutrons, NumberOfProtons, NumberOfElectrons,
                 Period, Group, Phase, Radioactive, Natural, Metal, Nonmetal, Metalloid, Type,
                 AtomicRadius, Electronegativity, ionizationEnergy, Density, MeltingPoint, BoilingPoint,
                 stableIsotopes, Discoverer, Year, SpecificHeat, NumberOfShells, NumberOfValence):
        self.AtomicNumber = AtomicNumber
        self.Element = Element
        self.symbol = Symbol
        self.AtomicMass = AtomicMass
        self.NumberOfNeutrons = NumberOfNeutrons
        self.NumberOfProtons = NumberOfProtons
        self.NumberOfElectrons = NumberOfElectrons
        self.Period = Period
        self.Group = Group
        self.Phase = Phase
        self.Radioactive = Radioactive
        self.Natural = Natural
        self.Metal = Metal
        self.Nonmetal = Nonmetal
        self.Metalloid = Metalloid
        self.Type = Type
        self.AtomicRadius = AtomicRadius
        self.Electronegativity = Electronegativity
        self.ionizationEnergy = ionizationEnergy
        self.Density = Density
        self.MeltingPoint = MeltingPoint
        self.BoilingPoint = BoilingPoint
        self.stableIsotopes = stableIsotopes
        self.Discoverer = Discoverer
        self.Year = Year
        self.SpecificHeat = SpecificHeat
        self.NumberOfShells = NumberOfShells
        self.NumberOfValence = NumberOfValence

    def to_dict(self):
        return vars(self)

class ElementList:
    def __init__(self):
        self.elements = []

    def add_element(self, element):
        self.elements.append(element)

    def generate_csv(self, filename, selected_attributes):
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=selected_attributes)
            writer.writeheader()
            for element in self.elements:
                element_dict = element.to_dict()
                selected_data = {k: element_dict[k] for k in selected_attributes}
                writer.writerow(selected_data)

    def read_csv(self, filename):
        with open(filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                element_data = {}
                for k, v in row.items():
                    element_data[k] = v
                element = Element(**element_data)
                self.add_element(element)

    def display_data(self):
        print("Attribute Names:")
        print(", ".join(vars(self.elements[0]).keys()))

        for element in self.elements:
            print(", ".join(str(value) for value in vars(element).values()))

        print("Attribute Names:")
        print(", ".join(vars(self.elements[0]).keys()))

def get_user_input(prompt):
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                raise ValueError("Input cannot be empty.")
            return user_input
        except ValueError as e:
            print(f"Error: {e}")

element_list = ElementList()
element_list.read_csv('Elements_data.csv')
element_list.display_data()

selected_attributes_str = get_user_input("Enter attribute names (comma-separated) to include in the output CSV: ")
selected_attributes = [attr.strip() for attr in selected_attributes_str.split(',')]

element_list.generate_csv('output_elements.csv', selected_attributes)
