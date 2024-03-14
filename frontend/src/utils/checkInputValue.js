import { removeElementClass } from "./removeElementClass";
import { addElementClass } from "./addElementClass";

// checkInputValue(inputValue, inputID)
// Function that checks the value of an input field and adds or removes a class based on that value.
// Parameters:
// inputValue: The value of the input field to be checked.
// inputID: The ID of the input element to be modified.

// Função que verifica o valor de um campo de entrada e adiciona ou remove uma classe com base nesse valor.
// Parâmetros:
// inputValue: O valor do campo de entrada a ser verificado.
// inputID: O ID do elemento de entrada a ser modificado.

export function checkInputValue (inputValue, inputID) {
  if (inputValue === '') {
    addElementClass(inputID, 'required-red-border');
  } else {
    removeElementClass(inputID, 'required-red-border');
  }
}