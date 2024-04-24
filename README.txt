This Python fragment starts by initializing a list called "peliculas" containing movie titles. Then, it does nothing with the list.
After defining the list, there is a function named "instrucciones" defined. This function takes no input. It prints three smart sentences in the standard output about the essentials of Python modules and packages. It prints one sentence each second.
Actually this is a dummy package, it has only test purpouses.
In the new 0.0.2 and 0.0.2.1 versions, there is an additional sentence that says: "¡Has difrutado de la segunda versión de este paquete!"
In the new version 0.0.3, you can add tabs to the “instructions” output when you call it with the optional “tabs” parameter set to True. This is an example of how to add functionality in a safe way in a library (without messing up the old one).
You can build this package while running:
$ python -m build
(in the root of the repository: https://github.com/p4bloOS/paquete-cib-pablopy)
