"""
molecule.py
A python package

Handles the primary functions
"""
import numpy as np
from geometry_analysis.measure import calculate_distance, calculate_angle

class Molecule:
    def __init__(self, name, symbols, coordinates):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError("Name is not a string.")

        self.symbols = symbols
        self._coordinates = coordinates
        self.bonds = self.build_bond_list()

    @property
    def num_atoms(self):
        return len(self.coordinates)

    @property
    def coordinates(self):
        return self._coordinates

    @coordinates.setter
    def coordinates(self, new_coordinates):
        self._coordinates = new_coordinates
        self.bonds = self.build_bond_list()

    def build_bond_list(self, max_bond=2.93, min_bond=0):
        """
        Build a list of bonds based on a distance criteria.
        Atoms within a specified distance of one another will be considered bonded.
        Parameters
        ----------
        max_bond : float, optional
        min_bond : float, optional
        Returns
        -------
        bond_list : list
            List of bonded atoms. Returned as list of tuples where the values are the atom indices.
        """

        bonds = {}

        for atom1 in range(self.num_atoms):
            for atom2 in range(atom1, self.num_atoms):
                distance = calculate_distance(self.coordinates[atom1], self.coordinates[atom2])

                if distance > min_bond and distance < max_bond:
                    bonds[(atom1, atom2)] = distance

        return bonds


if __name__ == "__main__":
    # Do something if this file is invoked on its own
    random_coordinates = np.random.random([3, 3])
    name = "my molecule"
    symbols = ["H", "O", "H"]

    my_molecule = Molecule(name, symbols, random_coordinates)

    print(F'There are {len(my_molecule.bonds)} bonds')
    print(F'The coordinates are {my_molecule.coordinates}')

    #random_coordinates = np.random.random([3,3])
    random_coordinates[0] += 100

    my_molecule.coordinates = random_coordinates

    print(F'\n\nThere are {len(my_molecule.bonds)} bonds')
    print(F'The coordinates are {my_molecule.coordinates}')


def canvas(with_attribution=True):
    """
    Placeholder function to show example docstring (NumPy format)

    Replace this function and doc string for your own project

    Parameters
    ----------
    with_attribution : bool, Optional, default: True
        Set whether or not to display who the quote is from

    Returns
    -------
    quote : str
        Compiled string including quote and optional attribution
    """

    quote = "The code is but a canvas to our imagination."
    if with_attribution:
        quote += "\n\t- Adapted from Henry David Thoreau"
    return quote


if __name__ == "__main__":
    # Do something if this file is invoked on its own
    print(canvas(False))
