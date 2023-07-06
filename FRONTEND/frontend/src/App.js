import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import logo from './logo.svg';
import './App.css';
import React from 'react';
import EmpleadoList from './components/EmpleadoList';
import EmpleadoForm from './components/EmpleadoForm';
function App() {
  return (
    <Router>
      <div>
        <Switch>
          <Route path="/" exact>
            <EmpleadoForm />
            <EmpleadoList />
          </Route>
          <Route path="/empleados/:id/editar" component={EmpleadoEdit} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;
