import { addElementClass } from "./addElementClass";
import { removeElementClass } from "./removeElementClass";



// clickSavecheckRequiredInsertField(inputValue, inputID, labelID)
// Function that checks if an input field is empty on save click and adds or removes classes based on that value.
// Parameters:
// inputValue: The value of the input field to be checked.
// inputID: The ID of the input element to be modified.
// labelID: The ID of the label associated with the input element.

// Função que verifica se um campo de entrada está vazio ao clicar em salvar e adiciona ou remove classes com base nesse valor.
// Parâmetros:
// inputValue: O valor do campo de entrada a ser verificado.
// inputID: O ID do elemento de entrada a ser modificado.
// labelID: O ID do rótulo associado ao elemento de entrada.

export function  clickSavecheckRequiredInsertField (inputValue, inputID, labelID) {
  if (inputValue === '') {
    addElementClass(inputID, 'required-red-border');
    addElementClass(labelID, 'campo-obrigatorio-warning');
  } else {
    removeElementClass(inputID, 'required-red-border');
    removeElementClass(labelID, 'campo-obrigatorio-warning');
  }
}