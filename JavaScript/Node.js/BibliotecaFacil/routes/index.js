
const express = require('express');
const router = express.Router();
const path = require('path');
const db = require('../db'); // Asegúrate de que la ruta sea correcta

// Definir las rutas

// Ruta para la página de inicio (login)
router.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, '../public/index.html'));
});

// Ruta para la vista del administrador
router.get('/gestor', (req, res) => {
  res.sendFile(path.join(__dirname, '../public/gestor.html'));
});

// Ruta para la vista del usuario
router.get('/user', (req, res) => {
  res.sendFile(path.join(__dirname, '../public/user.html'));
});

// Ruta para la vista de los libros disponibles 
router.get('/libros', (req, res) => {
  res.sendFile(path.join(__dirname, '../public/libros.html'));
});

// Ruta para la vista de los libros rentados
router.get('/librosRentados', (req, res) => {
  res.sendFile(path.join(__dirname, '../public/librosRentados.html'));
});

// Ruta para la vista de rentar libros
router.get('/rentar', (req, res) => {
  res.sendFile(path.join(__dirname, '../public/rentar.html'));
});

// Ruta para la vista de renovar renta
router.get('/renovar', (req, res) => {
  res.sendFile(path.join(__dirname, '../public/renovar.html'));
});

// Ruta para la vista de agregar libros
router.get('/agregarLibros', (req, res) => {
  res.sendFile(path.join(__dirname, '../public/agregarLibros.html'));
});

// Ruta para la vista de actualizar libros
router.get('/actualizarLibros', (req, res) => {
  res.sendFile(path.join(__dirname, '../public/actualizarLibros.html'));
});

// Ruta para la vista de elimnar libros
router.get('/eliminarLibros', (req, res) => {
  res.sendFile(path.join(__dirname, '../public/eliminarLibros.html'));
});


router.post('/register', (req, res) => {
  const { name, email, password } = req.body;
  
  // Lógica para registrar al usuario en la base de datos
  const query = 'INSERT INTO users (name, email, password) VALUES (?, ?, ?)';
  db.run(query, [name, email, password], (err) => {
      if (err) {
          console.error(err.message);
          res.status(500).json({ error: err.message });
      } else {
          res.redirect('/');
      }
  });
});

router.get('/register', (req, res) => {
  res.sendFile(path.join(__dirname, '../public/register.html'));
  res.redirect('/');
});

router.post('/login', (req, res) => {
  const { email, password } = req.body;
  const sql = 'SELECT * FROM users WHERE email = ? AND password = ?';
  db.get(sql, [email, password], (err, row) => {
    if (err) {
      return res.status(500).json({ error: err.message });
    }
    if (row) {
      res.redirect('/user');
    } else {
      res.redirect('/');
    }
  });
});

router.get('/books', (req, res) => {
  const { title, author, genre } = req.query;
  let sql = 'SELECT * FROM books WHERE 1=1';
  const params = [];

  if (title) {
    sql += ' AND title LIKE ?';
    params.push(`%${title}%`);
  }
  if (author) {
    sql += ' AND author LIKE ?';
    params.push(`%${author}%`);
  }
  if (genre) {
    sql += ' AND genre LIKE ?';
    params.push(`%${genre}%`);
  }

  db.all(sql, params, (err, rows) => {
    if (err) {
      return res.status(500).json({ error: err.message });
    }
    res.json({ books: rows });
  });
});

router.post('/borrow', (req, res) => {
  const { user_id, book_id } = req.body;
  const due_date = new Date();
  due_date.setDate(due_date.getDate() + 14); // Fecha de vencimiento a 2 semanas

  const sql = 'INSERT INTO loans (user_id, book_id, due_date) VALUES (?, ?, ?)';
  db.run(sql, [user_id, book_id, due_date.toISOString()], function(err) {
    if (err) {
      return res.status(500).json({ error: err.message });
    }
    res.json({ loanId: this.lastID });
  });
});

router.post('/renew', (req, res) => {
  const { loan_id } = req.body;
  const new_due_date = new Date();
  new_due_date.setDate(new_due_date.getDate() + 14);

  const sql = 'UPDATE loans SET due_date = ? WHERE id = ?';
  db.run(sql, [new_due_date.toISOString(), loan_id], function(err) {
    if (err) {
      return res.status(500).json({ error: err.message });
    }
    res.json({ message: 'Préstamo renovado con éxito' });
  });
});

router.post('/return', (req, res) => {
  const { loan_id } = req.body;

  const sql = 'DELETE FROM loans WHERE id = ?';
  db.run(sql, loan_id, function(err) {
    if (err) {
      return res.status(500).json({ error: err.message });
    }
    res.json({ message: 'Libro devuelto con éxito' });
  });
});

module.exports = router;

router.post('/books', (req, res) => {
  const { title, author, genre } = req.body;
  const sql = 'INSERT INTO books (title, author, genre) VALUES (?, ?, ?)';
  db.run(sql, [title, author, genre], function(err) {
    if (err) {
      return res.status(500).json({ error: err.message });
    }
    res.json({ bookId: this.lastID });
  });
});

router.get('/booksSearch', (req, res) => {
  const sql = 'SELECT * FROM books';
  db.all(sql, [], (err, rows) => {
    if (err) {
      return res.status(500).json({ error: err.message });
    }
    res.json({ books: rows });
  });
});

router.get('/books/:id', (req, res) => {
  const { id } = req.params;
  const sql = 'SELECT * FROM books WHERE id = ?';
  db.get(sql, [id], (err, row) => {
    if (err) {
      return res.status(500).json({ error: err.message });
    }
    res.json({ book: row });
  });
});

router.put('/books/:id', (req, res) => {
  const { id } = req.params;
  const { title, author, genre } = req.body;
  const sql = 'UPDATE books SET title = ?, author = ?, genre = ? WHERE id = ?';
  db.run(sql, [title, author, genre, id], function(err) {
    if (err) {
      return res.status(500).json({ error: err.message });
    }
    res.json({ message: 'Libro actualizado con éxito' });
  });
});

router.delete('/books/:id', (req, res) => {
  const { id } = req.params;
  const sql = 'DELETE FROM books WHERE id = ?';
  db.run(sql, [id], function(err) {
    if (err) {
      return res.status(500).json({ error: err.message });
    }
    res.json({ message: 'Libro eliminado con éxito' });
  });
});

// Esta ruta devolverá la información del usuario actual
router.get('/current-user', (req, res) => {
  // Supongamos que ya tienes la información del usuario en req.user
  // Si no, puedes almacenar esta información en la sesión y obtenerla de allí
  const user = req.session.user || null;
  if (user) {
    res.json(user);
  } else {
    res.status(401).json({ message: 'No hay usuario autenticado' });
  }
});
