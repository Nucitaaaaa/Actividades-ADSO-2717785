
document.getElementById('registerForm').addEventListener('submit', function(event) {
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

  document.addEventListener('DOMContentLoaded', function() {
    fetch('/books')
      .then(response => response.json())
      .then(data => {
        const resultsDiv = document.getElementById('searchResult');
        resultsDiv.innerHTML = ''; // Limpiar resultados anteriores
  
        if (data.books && data.books.length > 0) {
          data.books.forEach(book => {
            const bookDiv = document.createElement('div');
            bookDiv.innerText = `Título: ${book.title}, Autor: ${book.author}, Género: ${book.genre}`;
            resultsDiv.appendChild(bookDiv);
          });
        } else {
          resultsDiv.innerText = 'No se encontraron libros';
        }
      })
      .catch(error => {
        console.error('Error:', error);
        const resultsDiv = document.getElementById('searchResult');
        resultsDiv.innerText = 'Ocurrió un error al buscar los libros';
      });
  });
  
  

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
  

  document.addEventListener('DOMContentLoaded', () => {
    const userInfoDiv = document.getElementById('user-info');

// Obtener y mostrar la información del usuario
function fetchCurrentUser() {
  fetch('/current-user')
    .then(response => response.json())
    .then(user => {
      if (user && user.id) {
        userInfoDiv.innerHTML = `<p>ID: ${user.id}</p><p>// Usuario: ${user.name}</p>`;
      } else {
        userInfoDiv.innerHTML = '<p>No hay usuario autenticado</p>';
      }
    })
    .catch(error => {
      userInfoDiv.innerHTML = '<p>Error al obtener la información del usuario</p>';
    });
}

fetchCurrentUser();


});
