"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def newController():
    """
    Crea una instancia del modelo
    """
    control = {
        'model': None
    }
    control['model'] = model.newCatalog()
    return control


# Funciones para la carga de datos


def loadData(control):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadBooks(control)
    loadTags(control)
    loadBooksTags(control)


def loadBooks(control):
    # TODO lab 6, incluir el indice de libros por titulo con ADT Map
    """
    Carga los libros del archivo. Por cada libro se indica al
    modelo que debe adicionarlo al catalogo.
    """
    booksfile = cf.data_dir + 'GoodReads/books-small.csv'
    input_file = csv.DictReader(open(booksfile, encoding='utf-8'))
    for book in input_file:
        model.addBook(control['model'], book)


def loadTags(control):
    """
    Carga todos los tags del archivo e indica al modelo
    que los adicione al catalogo
    """
    tagsfile = cf.data_dir + 'GoodReads/tags.csv'
    input_file = csv.DictReader(open(tagsfile, encoding='utf-8'))
    for tag in input_file:
        model.addTag(control['model'], tag)


def loadBooksTags(control):
    """
    Carga la información que asocia tags con libros en el catalogo
    """
    booktagsfile = cf.data_dir + 'GoodReads/book_tags-small.csv'
    input_file = csv.DictReader(open(booktagsfile, encoding='utf-8'))
    for booktag in input_file:
        model.addBookTag(control['model'], booktag)


# Funciones de consulta sobre el catálogo


def getBestBooks(control, number):
    """
    Retorna los mejores libros según su promedio
    """
    bestbooks = model.getBestBooks(control['model'], number)
    return bestbooks


def countBooksByTag(control, tag):
    """
    Retorna los libros que fueron etiquetados con el tag
    """
    return model.countBooksByTag(control['model'], tag)


def booksSize(control):
    """
    Numero de libros cargados al catalogo
    """
    return model.booksSize(control['model'])


def authorsSize(control):
    """
    Numero de autores cargados al catalogo
    """
    return model.authorsSize(control['model'])


def tagsSize(control):
    """
    Numero de tags cargados al catalogo
    """
    return model.tagsSize(control['model'])


def getBooksByAuthor(control, authorname):
    """
    Retorna los libros de un autor
    """
    authorinfo = model.getBooksByAuthor(control['model'], authorname)
    return authorinfo


def getBooksByTag(control, tagname):
    """
    Retorna los libros que han sido marcados con
    una etiqueta
    """
    books = model.getBooksByTag(control['model'], tagname)
    return books


def getBooksYear(control, year):
    """
    Retorna los libros que fueron publicados
    en un año
    """
    books = model.getBooksByYear(control['model'], year)
    return books


def getBooksByTitle(control, title):
    # TODO lab 6, conectar con la funcion model.getBooksByTitle()
    """
    Completar la descripcion de getBooksByTittle
    """
    books = model.getBooksByTitle(control['model'], title)
    return books


def titlesSize(control):
    # TODO lab 6, conectar con la funcion model.titlesSize()
    """
    Completar la descripcion de titlesSize
    """
    return model.titlesSize(control['model'])
