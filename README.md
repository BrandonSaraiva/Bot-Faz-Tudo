# Apresentação

Bom esse bot eu criei para uso pessoal por isso tem funcionalidades e configurações tão específicas, caso alguem queira usa-lo precisará adaptar bastante para o seu própio pc.

# Instalações:

Instalações necessárias no python:

**pyautogui** : *py -m pip install pyautogui*

**telebot**   : *python -m pip install --user pyTelegramBotAPI*

# Configurações:

Voce irá criar um bot no telegram: 

![image](https://user-images.githubusercontent.com/90096835/212699272-24838609-8d93-4730-a549-7ef5b6059902.png)


- *Com o TOKEN da API pego irá substituir a CHAVE_API em todos os arquivos pelo o seu*

- *Caso queira utilizar a funcionalidade /tokin terá que ter esse BOT, link do Tokin: https://github.com/BrandonSaraiva/Projeto-bot-telegram-Lotof-cil*

- **O pyautogui utiliza batante os pixels da tela para se movimentar, por isso falei sobre esse BOT ser bem especifico para meu uso pessoal, meu monitor é 1920 X 1080 (23.5) polegadas, caso seu monitor também seja esse irá funcionar bem.**

- **Você irá ter que configurar algumas funções para o seu pc, por exemplo na função /email ele abre o link através da minha barra de favoritos no OPERA em uma posição especifica do favorito, você terá que mudar a localização do pyautogui.moveTo(). Na funçao /drive ele abre o bot em uma posição especifica dentro da pasta. Lembre-se também de deixar todos os aplicativos maximizados, se algum tiver em um tamanho menor doq full-scream (navegador por exemplo) ele irá clicar em outro local.**

- *Meu sistema operacional é o windows 10 pro*

- Caso não tenha familiaridade com o pyautogui para fazer essas configurações, veja esse vídeo: **https://youtu.be/MeOUl7ZjJRM**

# Comandos:

- Para ativar o bot digite /oi

/boleto   -  (Para receber o boleto do iesb ) #ainda estou configurando essa parte

/drive    -  (Para subir algum arquivo do seu desktop para o drive)

/diario   -  (Comandos para se usar diariamente) {

    /tokinho  -  (Ative o bot tokinho)
    
    /email    -  (Ver os ultimos 5 emails na caixa de email)
    
    /teamViewer - (Conectar um pc ao seu)

    /suspender - (Suspender o pc) {
    
      /tempo  -   Colocar um temporizador para o pc suspender
    
      /agora  -   Suspender imediatamente
      
      /cancelar -  Irá reiniciar o bot fazendo assim cancelar o shutdown
      
    }
    
    /clima     - (Previsão de hoje)

    /minimiza  - (Minimiza todas as abas)
    
}


/discord  -  (Conectar ao discord da empresa)

/limpar   -  (Feche todas as abas no servidor)

# Funcionalidades extras

**Eu também fiz umas funcionalidades para controlar o pc quando estiver vendo video no youtub, pode ser que vc esteja longe do PC  e queira digitar e ontrolar o som por exemplo, então fiz essas funções:**

- Caso você queira carregar um vídeo para assistir é só mandar o link do vídeo para o seu Bot, ele irá abrir em uma nova aba já com tudo pronto para você assistir.

- Digite **'Q'** para poder dar zoom no browse e 'P' para diminuir o zoom 

- Digite **'Qq'** para o zoom ser ainda maior e 'Pp' para ser ainda menor

- Digite **'A'** para pressionar a seta esquerda do pc (volta o vídeo em 5 segundos)

- Digite **'L'** para pressionar a seta direita do pc (adianta o vídeo em 5 segundos)

- Digite **','** para diminuir o som do pc

- Digite **'.'** para aumentar o som do pc

-Digite **'G'** para pressionar a barra de espaço do pc (pausa o vídeo)

- Digite **'F'** para sair da tela cheia do vídeo

- Use o comando **/escrever** para poder escrever no input que você clicar no seu pc

# Vídeo mostrando funcionando
