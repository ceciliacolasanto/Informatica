from db_discos import get_db
from clase_disco import Disco


def insert_disco(id, titulo, artista, precio, fecha, idioma, n_canciones, genero):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO discos (id, titulo, artista, precio, fecha, idioma, n_canciones, genero) \
    VALUES ( ?, ?, ?, ? ,?, ?, ?, ?)"
    cursor.execute(statement, [id, titulo, artista, precio, fecha, idioma, n_canciones, genero])
    db.commit()
    return True

def update_disco(id, titulo, artista, precio, fecha, idioma, n_canciones, genero):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE discos SET titulo = ?, artista = ?, precio= ?, fecha= ?, idioma= ?, n_canciones= ?, genero= ?, \
    WHERE ISBN = ?"
    cursor.execute(statement, [titulo, artista, precio, fecha, idioma, n_canciones, genero, id])
    db.commit()
    return True


def delete_disco(id):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM discos WHERE id = ?"
    cursor.execute(statement, [id])
    db.commit()
    return True


def get_by_id(id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT id, titulo, artista, precio, fecha, idioma, n_canciones, genero FROM discos WHERE id = ?"
    cursor.execute(statement, [id])
    single_disco = cursor.fetchone()
    id = single_disco[0]
    titulo = single_disco[1]
    artista = single_disco[2]
    precio = single_disco[3]
    fecha = single_disco[4]
    idioma = single_disco[5]
    n_canciones = single_disco[6]
    genero = single_disco[7]
    disco = Disco(id, titulo, artista, precio, fecha, idioma, n_canciones, genero) 
    return disco.describe_details()


def get_discos():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id, titulo, artista, precio, fecha, idioma, n_canciones, genero FROM discos"
    cursor.execute(query)
    discos_list = cursor.fetchall()
    list_of_discos=[]
    for disco in discos_list:
        id = disco[0]
        titulo = disco[1]
        artista = disco[2]
        precio = disco[3]
        fecha = disco[4]
        idioma = disco[5]
        n_canciones = disco[6]
        genero = disco[7]
        disco_to_add = Disco(id, titulo, artista, precio, fecha, idioma, n_canciones, genero)
        list_of_discos.append(disco_to_add)
    return list_of_discos
