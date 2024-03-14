import { toast} from 'vue3-toastify';
import 'vue3-toastify/dist/index.css';

// deleteSuccessToast(texto)
// Function that displays a success toast when deleting an item.
// Parameters:
// texto: The text to be displayed in the success toast.

// Função que exibe um toast de sucesso ao excluir um item.
// Parâmetros:
// texto: O texto a ser exibido no toast de sucesso.

export function deleteSuccessToast (texto) {
  toast.success(texto, {
    autoClose: 3000
  });
}