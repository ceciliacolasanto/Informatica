class Disco:

    def __init__(self, id, titulo, artista, precio, fecha, idioma, genero, n_canciones) -> None:
        self.id = id
        self.titulo = titulo
        self.artista = artista
        self.precio = precio
        self.fecha = fecha
        self.idioma = idioma
        self.genero = genero
        self._canciones = n_canciones
        

    def describe(self):
        return {
            'id': self.id,
            'título': self.titulo,
            'artista': self.artista,
            'precio': self.precio
        }

    def describe_details(self):
        return {
            'id': self.id,
            'título': self.titulo,
            'artista': self.artista,
            'precio': self.precio,
            'fecha_lanzamiento': self.fecha,
            'idioma': self.idioma,
            'número de canciones': self._canciones,
            'género': self.genero
        }