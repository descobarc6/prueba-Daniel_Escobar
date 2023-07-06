import React, { useState } from 'react';
import axios from 'axios';

function EmpleadoEdit({ empleado }) {
  const [nombre, setNombre] = useState(empleado.nombre);
  const [salarioBase, setSalarioBase] = useState(empleado.salario_base);

  const handleSubmit = async (e) => {
    e.preventDefault();

    const empleadoActualizado = {
      nombre: nombre,
      salario_base: salarioBase,
    };

    try {
      await axios.put(
        `http://localhost:8000/empleados/${empleado.id}/`,
        empleadoActualizado
      );
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <h2>Editar Empleado</h2>
      <form onSubmit={handleSubmit}>
        <label htmlFor="nombre">Nombre:</label>
        <input
          type="text"
          id="nombre"
          value={nombre}
          onChange={(e) => setNombre(e.target.value)}
        />

        <label htmlFor="salario">Salario Base:</label>
        <input
          type="number"
          id="salario"
          value={salarioBase}
          onChange={(e) => setSalarioBase(Number(e.target.value))}
        />

        <button type="submit">Actualizar</button>
      </form>
    </div>
  );
}

export default EmpleadoEdit;
