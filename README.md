# 🔐 Sistema de Autenticação Django com Email

![Django](https://img.shields.io/badge/Django-5.2.4-green.svg)
![Python](https://img.shields.io/badge/Python-3.13-blue.svg)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.1.3-purple.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

Sistema completo de autenticação desenvolvido em Django que utiliza email como campo principal de login, incluindo verificação de email com tokens seguros e interface responsiva moderna.

## 📸 Screenshots

### Tela de Login
![Login](docs/images/login-preview.png)

### Dashboard do Usuário
![Dashboard](docs/images/dashboard-preview.png)

### Verificação de Email
![Email Verification](docs/images/email-verification-preview.png)

## 🚀 Funcionalidades

### 🔑 Autenticação
- ✅ **Login via email** (não username)
- ✅ **Registro de usuários** com validação completa
- ✅ **Verificação de email** obrigatória com tokens seguros
- ✅ **Logout** com redirecionamento automático
- ✅ **Validação de formulários** robusta

### 👤 Gestão de Usuários
- ✅ **Modelo CustomUser** estendendo AbstractUser
- ✅ **Campos personalizados** (first_name, last_name, is_email_verified)
- ✅ **Manager customizado** para criação de usuários
- ✅ **Admin interface** personalizada

### 🎨 Interface e UX
- ✅ **Design responsivo** com Bootstrap 5
- ✅ **Templates organizados** com sistema de herança
- ✅ **Mensagens de feedback** visuais
- ✅ **Navegação intuitiva** e moderna
- ✅ **Dashboard personalizado** para usuários

### 🛡️ Segurança
- ✅ **Proteção CSRF** em todos os formulários
- ✅ **Tokens seguros** para verificação de email
- ✅ **Configuração segura** com variáveis de ambiente
- ✅ **Validação de dados** no backend
- ✅ **Prevenção de exposição** de credenciais

### 📧 Sistema de Email
- ✅ **Templates HTML** profissionais para emails
- ✅ **Console backend** para desenvolvimento
- ✅ **Configuração SMTP** pronta para produção
- ✅ **Links de verificação** com expiração

## 🛠️ Tecnologias Utilizadas

- **Backend:** Django 5.2.4
- **Frontend:** HTML5, CSS3, Bootstrap 5.1.3
- **Database:** SQLite (desenvolvimento) / PostgreSQL (produção)
- **Python:** 3.13+
- **Email:** SMTP (Gmail, SendGrid, etc.)

## 📦 Instalação e Configuração

### Pré-requisitos
- Python 3.9+
- Git

### 1. Clone o Repositório
```bash
git clone https://github.com/ernanegit/email_django.git
cd email_django
```

### 2. Ambiente Virtual
```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### 3. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 4. Configurar Variáveis de Ambiente
```bash
# Copiar template de configuração
cp .env.example .env

# Editar arquivo .env com suas configurações
```

**Conteúdo do arquivo .env:**
```env
SECRET_KEY=sua_chave_secreta_django_muito_longa_e_segura
DEBUG=True
EMAIL_USER=seu_email@gmail.com
EMAIL_PASSWORD=sua_senha_de_aplicativo_gmail
```

### 5. Configurar Banco de Dados
```bash
# Aplicar migrações
python manage.py makemigrations
python manage.py migrate
```

### 6. Criar Superusuário
```bash
python manage.py createsuperuser
```

### 7. Executar Servidor
```bash
python manage.py runserver
```

Acesse: **http://127.0.0.1:8000**

## 🔧 Configuração de Email

### Para Desenvolvimento (Console)
O projeto já vem configurado para mostrar emails no console durante o desenvolvimento.

### Para Produção (Gmail)
1. **Ative a verificação em 2 etapas** no Gmail
2. **Gere uma senha de aplicativo:**
   - Acesse: https://myaccount.google.com/apppasswords
   - Crie nova senha para "Django App"
3. **Configure no .env:**
   ```env
   EMAIL_USER=seu_email@gmail.com
   EMAIL_PASSWORD=senha_de_aplicativo_gerada
   ```

### Outros Provedores SMTP
```python
# Para SendGrid
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = 'sua_api_key_sendgrid'

# Para Mailgun
EMAIL_HOST = 'smtp.mailgun.org'
EMAIL_HOST_USER = 'seu_usuario_mailgun'
EMAIL_HOST_PASSWORD = 'sua_senha_mailgun'
```

## 📁 Estrutura do Projeto

```
email_django/
├── accounts/                   # App principal de autenticação
│   ├── models.py              # CustomUser model
│   ├── views.py               # Views de autenticação
│   ├── forms.py               # Formulários customizados
│   ├── managers.py            # Manager do CustomUser
│   ├── tokens.py              # Gerador de tokens
│   ├── utils.py               # Utilitários (envio de email)
│   ├── urls.py                # URLs do app
│   └── admin.py               # Interface admin
├── auth_project/              # Configurações do projeto
│   ├── settings.py            # Configurações principais
│   ├── urls.py                # URLs principais
│   └── wsgi.py                # WSGI config
├── templates/                 # Templates HTML
│   ├── base.html              # Template base
│   └── accounts/              # Templates do app accounts
│       ├── login.html
│       ├── register.html
│       ├── dashboard.html
│       ├── verify_email_sent.html
│       └── verification_email.html
├── static/                    # Arquivos estáticos
│   ├── css/
│   ├── js/
│   └── img/
├── .env.example              # Template de configuração
├── .gitignore               # Arquivos ignorados pelo Git
├── requirements.txt         # Dependências Python
└── README.md               # Este arquivo
```

## 🎯 Como Usar

### 1. Registro de Usuário
1. Acesse `/accounts/register/`
2. Preencha o formulário com email, nome e senha
3. Clique em "Registrar"
4. Verifique o email no console (desenvolvimento)

### 2. Verificação de Email
1. Copie o link de verificação do console
2. Cole no navegador para ativar a conta
3. Será redirecionado para o login

### 3. Login
1. Acesse `/accounts/login/`
2. Use seu email e senha
3. Será redirecionado para o dashboard

### 4. Dashboard
- Visualize informações da conta
- Status de verificação de email
- Data de cadastro
- Opções de logout

## 🚀 Deploy para Produção

### Configurações Necessárias

1. **Configurar DEBUG=False**
2. **Configurar ALLOWED_HOSTS**
3. **Usar banco PostgreSQL**
4. **Configurar servidor SMTP real**
5. **Configurar servidor web (nginx + gunicorn)**

### Exemplo com Heroku
```bash
# Instalar Heroku CLI
# Fazer login: heroku login

# Criar app
heroku create nome-do-seu-app

# Configurar variáveis de ambiente
heroku config:set SECRET_KEY=sua_chave_secreta
heroku config:set DEBUG=False
heroku config:set EMAIL_USER=seu_email@gmail.com
heroku config:set EMAIL_PASSWORD=sua_senha_app

# Deploy
git push heroku main

# Aplicar migrações
heroku run python manage.py migrate

# Criar superusuário
heroku run python manage.py createsuperuser
```

## 🧪 Testes

```bash
# Executar todos os testes
python manage.py test

# Testes específicos do app accounts
python manage.py test accounts

# Com coverage
pip install coverage
coverage run --source='.' manage.py test
coverage report
```

## 📈 Melhorias Futuras

### Funcionalidades Planejadas
- [ ] **Reset de senha** via email
- [ ] **Perfil de usuário** editável
- [ ] **Upload de foto** de perfil
- [ ] **Autenticação de dois fatores** (2FA)
- [ ] **Login social** (Google, GitHub, Facebook)
- [ ] **API REST** com Django REST Framework
- [ ] **Notificações** em tempo real
- [ ] **Histórico de logins**

### Melhorias Técnicas
- [ ] **Testes automatizados** completos
- [ ] **CI/CD** com GitHub Actions
- [ ] **Docker** containerization
- [ ] **Cache** com Redis
- [ ] **Monitoramento** com Sentry
- [ ] **Logs** estruturados

## 🤝 Contribuição

1. **Fork** o projeto
2. **Crie uma branch** para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. **Commit** suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. **Push** para a branch (`git push origin feature/nova-funcionalidade`)
5. **Abra um Pull Request**

### Diretrizes de Contribuição
- Siga as convenções de código do projeto
- Escreva testes para novas funcionalidades
- Atualize a documentação quando necessário
- Use commits semânticos

## 📝 Changelog

### [1.0.0] - 2025-07-04
- ✅ Sistema de autenticação via email
- ✅ Verificação de email com tokens
- ✅ Dashboard personalizado
- ✅ Interface responsiva
- ✅ Configuração de desenvolvimento e produção

## 🐛 Problemas Conhecidos

- Nenhum problema conhecido no momento

## 📞 Suporte

- **Issues:** [GitHub Issues](https://github.com/ernanegit/email_django/issues)
- **Email:** ernane1974@outlook.com
- **LinkedIn:** [Perfil do Ernane](https://linkedin.com/in/ernanegit)

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👨‍💻 Autor

**Ernane**
- GitHub: [@ernanegit](https://github.com/ernanegit)
- Email: ernane1974@outlook.com

## 🙏 Agradecimentos

- Django Framework pela excelente documentação
- Bootstrap pela interface responsiva
- Comunidade Python pelo suporte

---

**⭐ Se este projeto foi útil para você, considere dar uma estrela no repositório!**