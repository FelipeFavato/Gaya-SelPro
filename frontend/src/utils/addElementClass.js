
// addElementClass(elementID, classe)
// Function that adds a class to an HTML element by its ID.
// Parameters:
// elementID: The ID of the HTML element.
// classe: The class to be added to the element.

// Função que adiciona uma classe a um elemento HTML pelo seu ID.
// Parâmetros:
// elementID: O ID do elemento HTML.
// classe: A classe a ser adicionada ao elemento.


export function addElementClass (elementID, classe) {
  document.getElementById(elementID).classList.add(classe);
}