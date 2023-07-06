import React, { useEffect, useState } from 'react';
import axios from 'axios';

function EmpleadoList() {
  const [empleados, setEmpleados] = useState([]);

  useEffect(() => {
    fetchEmpleados();
  }, []);

  const fetchEmpleados = async () => {
    try {
      const response = await axios.get('http://localhost:8000/empleados/');
      setEmpleados(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <h2>Listado de Empleados</h2>
      <ul>
        {empleados.map((empleado) => (
          <li key={empleado.id}>
            {empleado.nombre} - Salario: {empleado.salario_base}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default EmpleadoList;
