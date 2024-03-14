// removeElementClass(elementID, classe)
// Function that removes a class from an HTML element by its ID.
// Parameters:
// elementID: The ID of the HTML element.
// classe: The class to be removed from the element.

// Função que remove uma classe de um elemento HTML pelo seu ID.
// Parâmetros:
// elementID: O ID do elemento HTML.
// classe: A classe a ser removida do elemento.

export function removeElementClass (elementID, classe) {
  document.getElementById(elementID).classList.remove(classe)
}