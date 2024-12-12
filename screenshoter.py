import pyautogui
from tkinter import Tk, Button, Label, filedialog

# Criar uma janela tkinter
win = Tk()
win.title("LoopGlitch Screenshoter")

# Função de callback para tirar uma captura de tela
def tirar_screenshot():
    try:
        # Abrir um diálogo de arquivos para permitir que o usuário escolha onde salvar a captura de tela
        caminho_arquivo = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("Arquivos PNG", "*.png")])
        
        if caminho_arquivo:  # Se o usuário escolheu um caminho válido
            screenshot = pyautogui.screenshot()
            screenshot.save(caminho_arquivo)  # Salvar a captura de tela no caminho escolhido
            status_label.config(text=f"Captura de tela salva como '{caminho_arquivo.split('/')[-1]}'", fg="green")
        else:
            status_label.config(text="Captura de tela não salva. Nenhum caminho de arquivo selecionado.", fg="red")
    except Exception as e:
        status_label.config(text=f"Erro: {str(e)}", fg="red")

# Criar um rótulo de instruções
instrucoes_label = Label(win, text="Clique no botão para tirar uma captura de tela.")
instrucoes_label.pack(pady=10)

# Criar um botão para acionar a captura de tela
screenshot_button = Button(win, text="Tirar Captura de Tela", command=tirar_screenshot)
screenshot_button.pack(pady=5)

# Criar um rótulo para exibir o status
status_label = Label(win, text="", fg="green")
status_label.pack(pady=5)

# Iniciar o loop de eventos do tkinter
win.mainloop()
