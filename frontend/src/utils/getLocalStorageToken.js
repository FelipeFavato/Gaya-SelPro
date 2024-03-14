// getLocalStorageToken()
// Function that returns the token stored in the localStorage.
// Returns:
// The token stored in the localStorage, if it exists.

// Função que retorna o token armazenado no localStorage.
// Retorna:
// O token armazenado no localStorage, se existir.

export function getLocalStorageToken () {
  return localStorage.getItem('token');
}