# QuGIT_v2: Quantum Gaussian Information Toolbox version 2

QuGIT is an open-sourced object-oriented Python library aimed at simulating multimode quantum gaussian states developed
by I. Brandão, D. Tandeitnik, T. Guerreiro (https://github.com/IgorBrandao42/Quantum-Gaussian-Information-Toolbox).

QuGIT_v2 (https://github.com/Setnom6/Quantum-Gaussian-Information-Toolbox-v2) makes use of QuGIT but is more focused in the computation of correlations between modes, primarily using the Logarithmic Negativity. In addition, a bigger flexibility in the definition of elementary states with arbitrary number
of modes is made. A list of the concrete additions made in QuGIT_v2 vs QuGIT can be found later.

The other significant difference is the change in some of the conventions and formal definitions of Gaussian States. This election is made following [Phys. Rev. D 106, 105021]. They are:

* $\hbar = 1$
* $[q_{i},p_{i}] = i \cdot \Omega$ (where $q_{i}$, $p_{i}$ are the quadratures and $\Omega$ is the symplectic matrix) 
* $\{A,B\}=AB+BA$ (anticonmutator)
* The covariance matrix is defined as $V = < {x_{i}-R_{i},x_{j}-R_{j}}>$ (where $R$ is the mean vector and $x$ is the quadratures vector).

In this package only one class is used, Gaussian_state and some auxiliary methods have been defined.

## Main features and changes from QuGIT

### Gaussian_state class

The fundamental building block of the toolbox is its ability to emulate an arbitrary multimode gaussian state, perform gaussian operations, and retrieve information from it. This is achieved through the custom Python class ```python Gaussian_state```, whose constructor arguments are

* R, V --- numpy.ndarray mean quadrature vector and covariance matrix for the desired gaussian states;

Elementary gaussian states can be created adding "vacuum", "thermal", "coherent" or "squeezed" to the arguments. The main improve from the original QuGIT is that it allows to produce those kind of predefined states with an arbitrary number of modes.

### Logarithmic_negativity method

This method has been improved from QuGIT allowing to compute the Logarithmic Negativity for a Gaussian State with an arbitrary number of modes. You can specify the subsystems on consideration and compute the LN only for those subsystems. Also, if the subsystem A is not a single mode, the tool will compute the LN but will also raise a warning because, as said in the literature, LN cannot provide the entanglement univocally if that is not the case.

Example of use is in the Log_Neg.py file

### Transformations

The definition of the beam splitter and the two mode squeezer have been changed to match the new conventions. Also, an attenuation transformation, which add some noise to the final covariance matrix after the symplectic transformation is implemented. The attenuation appears in the context of analogue gravity, see [Phys. Rev. D 106, 105021] for more details.

### Elementary states

Elementary_states() is a constructor of Gaussian states of the four type specified above but it allows to give different parameters for each mode.

### LN_generalized method

This method provides the Log Negativity of subsystems A and B for a Gaussian State after a symplectic transformation.
It takes as arguments:

* Scattering matrix in terms of the Bogoluibov coefficients (in annhilation/creation basis (S) if 1 is introduced as args)
* A Gaussian State to apply transformation on it (InState)  
* An array telling which are the modes from the subsystem A (subsA)
* An array telling which are the modes from the subsystem B (subsB)
* Can accept also an atenuation term eta

With that it computes the Logarithmic Negativity of the modes specified.

### Is_Symplectic

Is_Symplectic() is a method which allows to check if a given transformation matrix is symplectic or not. In addition, if the matrix is given in the annihilation and creation basis instead of the quadratures basis it checks the equivalent condition known as Bogoliubov relations.



## Dependencies

The toolbox makes use of the Numpy (version 1.26.4) and Scipy (version 1.11.4) packages.

## Installation

You can download the file "qgt.py" from this repository and use it as a module. In that case you have to call it from your script as

``` import qgt ```

Note that the location of the file is important and this syntax only work if "qgt.py" is in the same directory as the script from where you are calling it.

Another option is to pip install the latest library version from Pypi (not recommended since the version could be outdated compared to this repository), in that case, in a Linux terminal write (for non Linux OS use the equivalent command to pip install):

``` python3 -m pip install QuGIT_v2```

And then import it in your scripts as

``` import QuGIT_v2.qgt as qgt ```

No matter where is your script located this will work and you can call the functions from qgt as ``` qgt.Gaussian_state()```, for example.

## Running example

In the folder **Examples** there are some scripts with basic examples of implementation and calculations. These scripts import the toolbox as it were installed with pip. If is not the case, change the import line for the one showed in Installation. 

## Author

Jose Manuel Montes Armenteros

## Formalism

* Gerardo Adesso and Fabrizio Illuminati 2007 J. Phys. A: Math. Theor. 40 7821
* Anthony J. Brady, Ivan Agullo, and Dimitrios Kranas 2022 Phys. Rev. D 106, 105021
* I. Brandão, D. Tandeitnik, T. Guerreiro, " QuGIT: a numerical toolbox for Gaussian quantum states", arXiv:2201.06368

## License

This code is made available under the Creative Commons Attribution - Non Commercial 4.0 License. For full details see LICENSE.md.
