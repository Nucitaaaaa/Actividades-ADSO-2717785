
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
  