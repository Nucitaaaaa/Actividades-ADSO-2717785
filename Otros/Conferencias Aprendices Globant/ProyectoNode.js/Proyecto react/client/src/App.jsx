
import React, { useEffect, useState } from 'react';

const App = () => {
  const [estudiantes, setEstudiantes] = useState([]);

  useEffect(() => {
    fetch('/api/estudiantes')
      .then(response => response.json())
      .then(data => setEstudiantes(data))
      .catch(error => console.log(error));
  }, []);

  return (
    <div>
      <h1>Lista de Estudiantes</h1>
      <table>
        <thead>
          <tr>
            <th>Nombre</th>
            <th>Apellido</th>
            <th>Edad</th>
            <th>Semestre</th>
            <th>Estudia</th>
          </tr>
        </thead>
        <tbody>
          {estudiantes.map(estudiante => (
            <tr key={estudiante.id}>
              <td>{estudiante.nombre}</td>
              <td>{estudiante.apellido}</td>
              <td>{estudiante.edad}</td>
              <td>{estudiante.semestre}</td>
              <td>{estudiante.estudia ? 'Sí' : 'No'}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default App;


