
const express = require('express');
const router = express.Router();
const path = require('path');
const db = require('../db'); 

//?Rutas Usuario

//*Ruta para la página de inicio (login)
router.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, '../public/index.html'));
});

//*Ruta para la vista del usuario
router.get('/user', (req, res) => {
  res.sendFile(path.join(__dirname, '../public/user.html'));
});

//*Ruta para la vista de los libros disponibles 
router.get('/libros', (req, res) => {
  res.sendFile(path.join(__dirname, '../public/libros.html'));
});

//*Ruta para la vista de todos libros 
router.get('/biblioteca', (req, res) => {
  res.sendFile(path.join(__dirname, '../public/librosA.html'));
});

//*Ruta para la vista de los libros rentados
router.get('/librosRentados', (req, res) => {
  res.sendFile(path.join(__dirname, '../public/librosRentados.html'));
});

//*Ruta para rentar un libro
router.get('/rentar', (req, res) => {
  res.sendFile(path.join(__dirname, '../public/rentar.html'));
});

//*Ruta para la vista de renovar renta
router.get('/renovar', (req, res) => {
  res.sendFile(path.join(__dirname, '../public/renovar.html'));
});

//*Ruta para la vista de agregar libros
router.get('/agregarLibro', (req, res) => {
  res.sendFile(path.join(__dirname, '../public/agregarLibro.html'));
});

//*Ruta para la vista de actualizar libros
router.get('/actualizarLibro', (req, res) => {
  res.sendFile(path.join(__dirname, '../public/actualizarLibro.html'));
});

//*Ruta para la vista de elimnar libros
router.get('/eliminarLibro', (req, res) => {
  res.sendFile(path.join(__dirname, '../public/eliminarLibro.html'));
});

//*Ruta para la vista de devolver libros
router.get('/devolver', (req, res) => {
  res.sendFile(path.join(__dirname, '../public/devolver.html'));
});

//*Ruta para la vista de buscar libros
router.get('/buscar', (req, res) => {
  res.sendFile(path.join(__dirname, '../public/buscar.html'));
});


//?Rutas Gestor 
router.get('/gestor', (req, res) => {
  res.sendFile(path.join(__dirname, '../public/gestor.html'));
});


router.post('/register', (req, res) => {
  const { name, email, password } = req.body;
  
  //*Lógica para registrar al usuario en la base de datos
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

  if (email === 'root' && password === 'toor') {
    return res.redirect('/gestor');
  }

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

router.get('/booksSearch', (req, res) => {
  const { title, author, genre } = req.query;
  let sql = 'SELECT * FROM books WHERE 1=1';
  const params = [];

  if (title && title.trim()) {
    sql += ' AND title LIKE ?';
    params.push(`%${title.trim()}%`);
  }
  if (author && author.trim()) {
    sql += ' AND author LIKE ?';
    params.push(`%${author.trim()}%`);
  }
  if (genre && genre.trim()) {
    sql += ' AND genre LIKE ?';
    params.push(`%${genre.trim()}%`);
  }

  // Ejecutar la consulta con los parámetros
  db.all(sql, params, (err, rows) => {
    if (err) {
      return res.status(500).json({ error: err.message });
    }
    res.json(rows);
  });
});

router.post('/borrow', (req, res) => {
  const { user_id, book_id } = req.body;
  const due_date = new Date();
  due_date.setDate(due_date.getDate() + 14); //*Fecha de vencimiento a 2 semanas

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

router.get('/book', (req, res) => {
  const sql = 'SELECT * FROM books';
  db.all(sql, [], (err, rows) => {
    if (err) {
      return res.status(500).json({ error: err.message });
    }
    res.json({ books: rows });
  });
});

router.get('/bookR', (req, res) => {
  const sql = 'SELECT * FROM BOOKS b WHERE EXISTS (SELECT * FROM LOANS l WHERE l.book_id = b.id);';
  db.all(sql, [], (err, rows) => {
    if (err) {
      return res.status(500).json({ error: err.message });
    }
    res.json({ books: rows });
  });
});

router.get('/bookD', (req, res) => {
  const sql = 'SELECT b.id, b.title, b.author, b.genre FROM BOOKS b LEFT JOIN LOANS l ON b.id = l.book_id WHERE l.id IS NULL;';
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
