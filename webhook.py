from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        # Adicione lógica de segurança aqui para validar o payload
        subprocess.run(["ansible-playbook", "/root/ansible-project/play6-app-web-deploy.yml"])
        return 'Webhook received!', 200
    else:
        return 'Invalid request!', 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
