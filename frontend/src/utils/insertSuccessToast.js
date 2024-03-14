import { toast} from 'vue3-toastify';
import 'vue3-toastify/dist/index.css';

// insertSuccessToast(texto)
// Function that displays a success toast after inserting an item.
// Parameters:
// texto: The text to be displayed in the success toast.

// Função que exibe um toast de sucesso após a inserção de um item.
// Parâmetros:
// texto: O texto a ser exibido no toast de sucesso.

export function insertSuccessToast (texto) {
  toast.success(texto + ' INSERIDO com sucesso!', {
    autoClose: 3000
  });
}