
document.addEventListener('DOMContentLoaded', function() {
  document.getElementById('registerForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const name = document.getElementById('registerName').value;
    const email = document.getElementById('registerEmail').value;
    const password = document.getElementById('registerPassword').value;

    //?Register 

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
});


//?Login

document.addEventListener('DOMContentLoaded', function() {
  document.getElementById('loginForm').addEventListener('submit', function(event) {
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
  
      // Redirecciona si el login es exitoso
      if (data.redirectUrl) {
        window.location.href = data.redirectUrl;
      }
    })
    .catch(error => console.error('Error:', error));
  });
});


//?Libros (libros.html)

document.addEventListener('DOMContentLoaded', function() {
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


          idCell.innerText = book.id
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
});


document.addEventListener('DOMContentLoaded', function() {
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


          idCell.innerText = book.id
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
});

document.addEventListener('DOMContentLoaded', function() {
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


          idCell.innerText = book.id
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
});

//*Buscar libros (libros.html)

document.getElementById('searchForm').addEventListener('submit', function(event) {
  event.preventDefault();
  const title = document.getElementById('searchTitle').value;
  const author = document.getElementById('searchAuthor').value;
  const genre = document.getElementById('searchGenre').value;

  const query = new URLSearchParams({ title, author, genre });

  fetch(`/books?${query}`)
  .then(response => response.json())
  .then(data => {
    const resultsDiv = document.getElementById('searchResults');
    resultsDiv.innerHTML = '';
    data.books.forEach(book => {
      const bookDiv = document.createElement('div');
      bookDiv.innerText = `${book.title} by ${book.author} (Genre: ${book.genre})`;
      resultsDiv.appendChild(bookDiv);
    });
  });
});


//?Cliente para ver los libros rentados (rentar.html)

document.addEventListener('DOMContentLoaded', function() {
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
});


// //!rentar libro (libros.html) ?
  
document.getElementById('borrowForm').addEventListener('submit', function(event) {
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

//* Renovar prestamo (librosRentados.html)

document.getElementById('renewForm').addEventListener('submit', function(event) {
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
    document.getElementById('renewMessage').innerText = data.message ? 'Préstamo renovado con éxito' : 'Error en la renovación';
  });
});

//* Devolver libro (librosRentados.html)

document.getElementById('returnForm').addEventListener('submit', function(event) {
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
  });
});


//? Agregar libro 
document.addEventListener('DOMContentLoaded', function() {
  document.getElementById('addBookForm').addEventListener('submit', function(event) {
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
});

