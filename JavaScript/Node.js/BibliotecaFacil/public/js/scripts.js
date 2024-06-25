
document.addEventListener('DOMContentLoaded', function() {
  //? Register
  const registerForm = document.getElementById('registerForm');
  if (registerForm) {
    registerForm.addEventListener('submit', function(event) {
      event.preventDefault();
      const name = document.getElementById('registerName').value;
      const email = document.getElementById('registerEmail').value;
      const password = document.getElementById('registerPassword').value;

      fetch('/register', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name, email, password })
      })
      .then(response => response.json())
      .then(data => {
        document.getElementById('registerMessage').innerText = data.userId ? 'Registro exitoso' : 'Error en el registro';
      });
    });
  }

  //? Login
  const loginForm = document.getElementById('loginForm');
  if (loginForm) {
    loginForm.addEventListener('submit', function(event) {
      event.preventDefault();
      const email = document.getElementById('loginEmail').value;
      const password = document.getElementById('loginPassword').value;

      fetch('/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email, password })
      })
      .then(response => response.json())
      .then(data => {
        document.getElementById('loginMessage').innerText = data.message;

        if (data.redirectUrl) {
          window.location.href = data.redirectUrl;
        }
      })
      .catch(error => console.error('Error:', error));
    });
  }

  //? Libros (libros.html)
  if (document.getElementById('books')) {
    fetch('/book')
      .then(response => response.json())
      .then(data => {
        const resultsTable = document.getElementById('books').getElementsByTagName('tbody')[0];
        resultsTable.innerHTML = ''; // Limpiar resultados anteriores

        if (data.books && data.books.length > 0) {
          data.books.forEach(book => {
            const row = resultsTable.insertRow();
            const idCell = row.insertCell(0);
            const titleCell = row.insertCell(1);
            const authorCell = row.insertCell(2);
            const genreCell = row.insertCell(3);

            idCell.innerText = book.id;
            titleCell.innerText = book.title;
            authorCell.innerText = book.author;
            genreCell.innerText = book.genre;
          });
        } else {
          const row = resultsTable.insertRow();
          const cell = row.insertCell(0);
          cell.innerText = 'No se encontraron libros';
        }
      })
      .catch(error => {
        console.error('Error:', error);
        const resultsTable = document.getElementById('booksTable').getElementsByTagName('tbody')[0];
        resultsTable.innerHTML = '<tr><td>Ocurrió un error al buscar los libros</td></tr>';
      });
  }

  //? Libros rentados (libros.html)
  if (document.getElementById('booksBorrow')) {
    fetch('/bookR')
      .then(response => response.json())
      .then(data => {
        const resultsTable = document.getElementById('booksBorrow').getElementsByTagName('tbody')[0];
        resultsTable.innerHTML = ''; // Limpiar resultados anteriores

        if (data.books && data.books.length > 0) {
          data.books.forEach(book => {
            const row = resultsTable.insertRow();
            const idCell = row.insertCell(0);
            const titleCell = row.insertCell(1);
            const authorCell = row.insertCell(2);
            const genreCell = row.insertCell(3);

            idCell.innerText = book.id;
            titleCell.innerText = book.title;
            authorCell.innerText = book.author;
            genreCell.innerText = book.genre;
          });
        } else {
          const row = resultsTable.insertRow();
          const cell = row.insertCell(0);
          cell.innerText = 'No se encontraron libros';
        }
      })
      .catch(error => {
        console.error('Error:', error);
        const resultsTable = document.getElementById('booksTable').getElementsByTagName('tbody')[0];
        resultsTable.innerHTML = '<tr><td>Ocurrió un error al buscar los libros</td></tr>';
      });
  }

  //? Libros disponibles (libros.html)
  if (document.getElementById('booksFree')) {
    fetch('/bookD')
      .then(response => response.json())
      .then(data => {
        const resultsTable = document.getElementById('booksFree').getElementsByTagName('tbody')[0];
        resultsTable.innerHTML = ''; // Limpiar resultados anteriores

        if (data.books && data.books.length > 0) {
          data.books.forEach(book => {
            const row = resultsTable.insertRow();
            const idCell = row.insertCell(0);
            const titleCell = row.insertCell(1);
            const authorCell = row.insertCell(2);
            const genreCell = row.insertCell(3);

            idCell.innerText = book.id;
            titleCell.innerText = book.title;
            authorCell.innerText = book.author;
            genreCell.innerText = book.genre;
          });
        } else {
          const row = resultsTable.insertRow();
          const cell = row.insertCell(0);
          cell.innerText = 'No se encontraron libros';
        }
      })
      .catch(error => {
        console.error('Error:', error);
        const resultsTable = document.getElementById('booksTable').getElementsByTagName('tbody')[0];
        resultsTable.innerHTML = '<tr><td>Ocurrió un error al buscar los libros</td></tr>';
      });
  }

  
//? Buscar libro

  const searchForm = document.getElementById('searchForm');
  if (searchForm) {
    searchForm.addEventListener('submit', function(event) {
      event.preventDefault();
      const title = document.getElementById('searchTitle').value;
      const author = document.getElementById('searchAuthor').value;
      const genre = document.getElementById('searchGenre').value;

      const query = new URLSearchParams({ title, author, genre });

      fetch(`/book?${query}`)
      .then(response => response.json())
      .then(data => {
        const resultsDiv = document.getElementById('search');
        resultsDiv.innerHTML = '';

        const thead = resultsDiv.createTHead();
        const headerRow = thead.insertRow();
        const headers = ['ID', 'Título', 'Autor', 'Género'];
        headers.forEach(headerText => {
          const th = document.createElement('th');
          th.innerText = headerText;
          headerRow.appendChild(th);
        });

        const tbody = resultsDiv.createTBody();
        if (data.books && data.books.length > 0) {
          data.books.forEach(book => {
            const row = tbody.insertRow();
            row.style.display = 'table-row'; // Asegurarse de que la fila de tabla es visible
            const idCell = row.insertCell(0);
            const titleCell = row.insertCell(1);
            const authorCell = row.insertCell(2);
            const genreCell = row.insertCell(3);

            idCell.innerText = book.id;
            titleCell.innerText = book.title;
            authorCell.innerText = book.author;
            genreCell.innerText = book.genre;
          });

        } else {
          const row = resultsTable.insertRow();
          const cell = row.insertCell(0);
          cell.innerText = 'No se encontraron libros';
        }
      });
    });
  }


  //? Cliente para ver los libros rentados (rentar.html)
  if (document.getElementById('librosRentados')) {
    fetch('/books')
      .then(response => response.json())
      .then(data => {
        const resultsTable = document.getElementById('librosRentados').getElementsByTagName('tbody')[0];
        resultsTable.innerHTML = ''; // Limpiar resultados anteriores

        if (data.books && data.books.length > 0) {
          data.books.forEach(book => {
            const row = resultsTable.insertRow();
            const idCell = row.insertCell(0);
            const titleCell = row.insertCell(1);

            idCell.innerText = book.id; // Asegúrate de que el objeto libro tenga una propiedad id
            titleCell.innerText = book.title;
          });
        } else {
          const row = resultsTable.insertRow();
          const cell = row.insertCell(0);
          cell.innerText = 'No se encontraron libros';
        }
      })
      .catch(error => {
        console.error('Error:', error);
        const resultsTable = document.getElementById('librosRentados').getElementsByTagName('tbody')[0];
        resultsTable.innerHTML = '<tr><td>Ocurrió un error al buscar los libros</td></tr>';
      });
  }

  //? Rentar libro (libros.html)
  const borrowForm = document.getElementById('borrowForm');
  if (borrowForm) {
    borrowForm.addEventListener('submit', function(event) {
      event.preventDefault();
      const user_id = document.getElementById('borrowUserId').value;
      const book_id = document.getElementById('borrowBookId').value;

      fetch('/borrow', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ user_id, book_id })
      })
      .then(response => response.json())
      .then(data => {
        document.getElementById('borrowMessage').innerText = data.loanId ? 'Préstamo solicitado con éxito' : 'Error en el préstamo';
      });
    });
  }

  //? Renovar préstamo (librosRentados.html)
  const renewForm = document.getElementById('renewForm');
  if (renewForm) {
    renewForm.addEventListener('submit', function(event) {
      event.preventDefault();
      const loan_id = document.getElementById('renewLoanId').value;

      fetch('/renew', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ loan_id })
      })
      .then(response => response.json())
      .then(data => {
        document.getElementById('renewMessage').innerText = data.success ? 'Préstamo renovado con éxito' : 'Error al renovar el préstamo';
      });
    });
  }
});


//*?Devolver libro (librosRentados.html)

document.addEventListener('DOMContentLoaded', function() {
  const returnForm = document.getElementById('returnForm');
  if (returnForm) {
    returnForm.addEventListener('submit', function(event) {
      event.preventDefault();
      const loan_id = document.getElementById('returnLoanId').value;
      const book_id = document.getElementById('returnBookId').value;

      fetch('/return', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ loan_id, book_id })
      })
      .then(response => response.json())
      .then(data => {
        document.getElementById('returnMessage').innerText = data.message ? 'Libro devuelto con éxito' : 'Error en la devolución';
      })
      .catch(error => {
        console.error('Error:', error);
        document.getElementById('returnMessage').innerText = 'Error en la devolución';
      });
    });
  }
});


//? Agregar libro 
document.addEventListener('DOMContentLoaded', function() {
  const addBookForm = document.getElementById('addBookForm');
  if (addBookForm) {
    addBookForm.addEventListener('submit', function(event) {
      event.preventDefault();
      const title = document.getElementById('title').value;
      const author = document.getElementById('author').value;
      const genre = document.getElementById('genre').value;

      fetch('/books', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ title, author, genre })
      })
      .then(response => response.json())
      .then(data => {
        const messageElement = document.getElementById('message');
        if (data.bookId) {
          messageElement.innerText = 'Libro agregado exitosamente. ID: ' + data.bookId;
        } else {
          messageElement.innerText = 'Error al agregar el libro';
        }
      })
      .catch(error => {
        console.error('Error:', error);
        document.getElementById('message').innerText = 'Error al agregar el libro';
      });
    });
  }
});


//? Modificar libro 

document.addEventListener('DOMContentLoaded', function() {
  const updateBookForm = document.getElementById('updateBookForm');
  if (updateBookForm) {
    updateBookForm.addEventListener('submit', function(event) {
      event.preventDefault();
      const bookId = document.getElementById('bookId').value;
      const title = document.getElementById('title').value;
      const author = document.getElementById('author').value;
      const genre = document.getElementById('genre').value;

      fetch(`/books/${bookId}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ title, author, genre })
      })
      .then(response => response.json())
      .then(data => {
        const messageElement = document.getElementById('message');
        if (data.message) {
          messageElement.innerText = 'Libro actualizado con éxito';
        } else {
          messageElement.innerText = 'Error al actualizar el libro';
        }
      })
      .catch(error => {
        console.error('Error:', error);
        document.getElementById('message').innerText = 'Error al actualizar el libro';
      });
    });
  }
});


//? Eliminar libro 

document.addEventListener('DOMContentLoaded', function() {
  const deleteBookForm = document.getElementById('deleteBookForm');
  if (deleteBookForm) {
    deleteBookForm.addEventListener('submit', function(event) {
      event.preventDefault();
      const bookId = document.getElementById('bookId').value;

      fetch(`/books/${bookId}`, {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json'
        }
      })
      .then(response => response.json())
      .then(data => {
        const messageElement = document.getElementById('message');
        if (data.message) {
          messageElement.innerText = 'Libro eliminado con éxito';
        } else {
          messageElement.innerText = 'Error al eliminar el libro';
        }
      })
      .catch(error => {
        console.error('Error:', error);
        document.getElementById('message').innerText = 'Error al eliminar el libro';
      });
    });
  }
});
