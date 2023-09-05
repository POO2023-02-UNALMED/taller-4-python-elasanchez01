from classroom.asignatura import Asignatura

class Grupo:
    grado = 'Grado 12'

    def __init__(self, grupo="grupo predeterminado", asignaturas=[], estudiantes = [], grado = grado):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes
        self.grado = grado

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=[]):
        self.listadoAlumnos = self.listadoAlumnos + lista
        self.listadoAlumnos.append(alumno)


    def __str__(self):
        return f'Grupo de estudiantes: {self._grupo}'

    @ classmethod
    def asignarNombre(cls, nombre="Grado 10"):
        cls.grado = nombre


    @ classmethod
    def asignarNombre(cls, nombre="Grado 4"):
        cls.grado = nombre


    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre