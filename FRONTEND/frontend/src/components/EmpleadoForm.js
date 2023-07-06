import React, { useState } from 'react';
import axios from 'axios';

function EmpleadoForm() {
  const [nombre, setNombre] = useState('');
  const [salarioBase, setSalarioBase] = useState(0);

  const handleSubmit = async (e) => {
    e.preventDefault();

    const nuevoEmpleado = {
      nombre: nombre,
      salario_base: salarioBase,
    };

    try {
      await axios.post('http://localhost:8000/empleados/', nuevoEmpleado);
      setNombre('');
      setSalarioBase(0);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <h2>Agregar Empleado</h2>
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

        <button type="submit">Agregar</button>
      </form>
    </div>
  );
}

export default EmpleadoForm;
