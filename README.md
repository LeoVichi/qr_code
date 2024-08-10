# QR Code Generator Web App

Este é um aplicativo web simples desenvolvido em Python utilizando Flask que permite a geração de códigos QR com base em diferentes tipos de entrada, como URLs, vCards, textos, emails, SMS, informações de WiFi, endereços de Bitcoin, perfis de Twitter e Facebook, links para PDFs e arquivos MP3.

## Funcionalidades

- **Geração de QR Codes** para diferentes tipos de dados.
- **Exportação de QR Codes** em formato PNG.
- **Interface web** intuitiva construída com Flask.

## Instalação

1. Clone o repositório para o seu ambiente local:
    ```bash
    git clone https://github.com/LeoVichi/qr_code.git
    cd qr-code-generator
    ```

2. Crie um ambiente virtual (recomendado) e instale as dependências:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. Execute o aplicativo:
    ```bash
    python3 app.py
    ```

4. Acesse a aplicação no seu navegador através do endereço:
    ```
    http://127.0.0.1:5000/
    ```

## Como Usar

1. Acesse a página inicial.
2. Escolha o tipo de QR code que deseja gerar (URL, vCard, texto, email, SMS, WiFi, Bitcoin, Twitter, Facebook, PDF, MP3).
3. Preencha os campos necessários.
4. Clique em "Gerar QR Code".
5. O QR code será gerado e baixado automaticamente como um arquivo PNG.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e enviar pull requests.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
