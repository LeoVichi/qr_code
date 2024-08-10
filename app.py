"""
Author: L3nny_P34s4n7
Email: contact@leonardovichi.com
Date: 2024-08-10
License: MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

from flask import Flask, render_template, request, send_file
import qrcode
from io import BytesIO

# Cria uma instância do Flask para o aplicativo web
app = Flask(__name__)

@app.route('/')
def index():
    """
    Renderiza a página inicial.

    Returns:
        render_template: Renderiza o template HTML 'index.html'.
    """
    return render_template('index.html')

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    """
    Gera um código QR com base nos dados enviados via formulário.

    O tipo de código QR gerado depende dos dados fornecidos pelo usuário,
    como URL, vCard, texto, email, SMS, informações de WiFi, endereço de
    Bitcoin, etc.

    Returns:
        send_file: Envia a imagem do código QR gerado como um arquivo PNG.
    """
    # Coleta o tipo de QR e a resolução desejada a partir do formulário
    qr_type = request.form['type']
    resolution = int(request.form['resolution'])
    qr_data = ''

    # Coleta e organiza os dados conforme o tipo de QR especificado
    if qr_type == 'url':
        qr_data = request.form['url_input']
    elif qr_type == 'vcard':
        name = request.form['vcard_name']
        email = request.form['vcard_email']
        phone = request.form['vcard_phone']
        qr_data = f'BEGIN:VCARD\nFN:{name}\nEMAIL:{email}\nTEL:{phone}\nEND:VCARD'
    elif qr_type == 'text':
        qr_data = request.form['text_input']
    elif qr_type == 'email':
        address = request.form['email_address']
        subject = request.form['email_subject']
        body = request.form['email_body']
        qr_data = f'MAILTO:{address}?subject={subject}&body={body}'
    elif qr_type == 'sms':
        number = request.form['sms_number']
        message = request.form['sms_message']
        qr_data = f'SMSTO:{number}:{message}'
    elif qr_type == 'wifi':
        ssid = request.form['wifi_ssid']
        password = request.form['wifi_password']
        encryption = request.form['wifi_encryption']
        qr_data = f'WIFI:T:{encryption};S:{ssid};P:{password};;'
    elif qr_type == 'bitcoin':
        address = request.form['bitcoin_address']
        amount = request.form['bitcoin_amount']
        qr_data = f'bitcoin:{address}?amount={amount}'
    elif qr_type == 'twitter':
        username = request.form['twitter_username']
        tweet = request.form['twitter_tweet']
        qr_data = f'https://twitter.com/intent/tweet?text={tweet}&via={username}'
    elif qr_type == 'facebook':
        profile = request.form['facebook_profile']
        qr_data = f'https://www.facebook.com/{profile}'
    elif qr_type == 'pdf':
        pdf_url = request.form['pdf_url']
        qr_data = pdf_url
    elif qr_type == 'mp3':
        mp3_url = request.form['mp3_url']
        qr_data = mp3_url

    # Configura o QR code com a biblioteca qrcode
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_data)
    qr.make(fit=True)

    # Gera a imagem do QR code com as cores padrão (preto e branco)
    img = qr.make_image(fill='black', back_color='white')
    img = img.resize((resolution * 10, resolution * 10), resample=0)

    # Cria um buffer para armazenar a imagem em memória e retorná-la como arquivo
    buffer = BytesIO()
    img.save(buffer, format="PNG", dpi=(resolution, resolution))
    buffer.seek(0)
    return send_file(buffer, mimetype='image/png', as_attachment=True, download_name='qr_code.png')

if __name__ == '__main__':
    # Executa o aplicativo Flask no modo de depuração
    app.run(debug=True)