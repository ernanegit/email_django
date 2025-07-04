# 🔐 Sistema de Autenticação Django com Email

![Django](https://img.shields.io/badge/Django-5.2.4-green.svg)
![Python](https://img.shields.io/badge/Python-3.13-blue.svg)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.1.3-purple.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Produção_Ready-brightgreen.svg)

Sistema completo de autenticação desenvolvido em Django que utiliza email como campo principal de login, incluindo verificação de email com tokens seguros e interface responsiva moderna.

## 📸 Screenshots

### 🔑 Tela de Login
![Login](https://github.com/ernanegit/email_django/blob/main/docs/images/login-preview.png)
*Interface de login responsiva com validação em tempo real*

### 📊 Dashboard do Usuário
![Dashboard](https://github.com/ernanegit/email_django/blob/main/docs/images/dashboard-preview.png)
*Dashboard personalizado com informações do usuário e status de verificação*

### 📧 Verificação de Email
![Email Verification](https://github.com/ernanegit/email_django/blob/main/docs/images/email-verification-preview.png)
*Sistema de verificação de email com mensagens claras*

## 🚀 Funcionalidades

### 🔑 Sistema de Autenticação
- ✅ **Login via email** (não username tradicional)
- ✅ **Registro de usuários** com validação completa
- ✅ **Verificação de email obrigatória** com tokens seguros
- ✅ **Logout** com redirecionamento automático
- ✅ **Sessões seguras** com controle de tempo
- ✅ **Redirecionamentos inteligentes** após login

### 👤 Gestão de Usuários
- ✅ **Modelo CustomUser** estendendo AbstractUser
- ✅ **Campos personalizados** (first_name, last_name, is_email_verified)
- ✅ **Manager customizado** para criação de usuários e superusuários
- ✅ **Interface admin** personalizada e otimizada
- ✅ **Validação robusta** de dados de entrada

### 🎨 Interface e Experiência do Usuário
- ✅ **Design responsivo** com Bootstrap 5
- ✅ **Templates organizados** com sistema de herança
- ✅ **Mensagens de feedback** visuais e contextuais
- ✅ **Navegação intuitiva** e moderna
- ✅ **Dashboard personalizado** com informações relevantes
- ✅ **Formulários estilizados** com validação frontend

### 🛡️ Segurança e Boas Práticas
- ✅ **Proteção CSRF** em todos os formulários
- ✅ **Tokens seguros** para verificação de email com expiração
- ✅ **Configuração segura** com variáveis de ambiente
- ✅ **Validação de dados** robusta no backend
- ✅ **Prevenção de exposição** de credenciais sensíveis
- ✅ **Senhas hasheadas** com algoritmos seguros

### 📧 Sistema de Email Profissional
- ✅ **Templates HTML** responsivos e profissionais
- ✅ **Console backend** para desenvolvimento local
- ✅ **Configuração SMTP** flexível para produção
- ✅ **Links de verificação** com tokens únicos e seguros
- ✅ **Prevenção de spam** e rate limiting

## 🛠️ Tecnologias Utilizadas

| Categoria | Tecnologia | Versão | Propósito |
|-----------|------------|--------|-----------|
| **Backend** | Django | 5.2.4 | Framework web principal |
| **Language** | Python | 3.13+ | Linguagem de programação |
| **Frontend** | Bootstrap | 5.1.3 | Framework CSS responsivo |
| **Database** | SQLite | - | Banco de dados (desenvolvimento) |
| **Email** | SMTP | - | Envio de emails |
| **Security** | Django Auth | - | Sistema de autenticação |

## 📦 Instalação e Configuração

### ⚙️ Pré-requisitos
- Python 3.9 ou superior
- Git
- Navegador moderno
- Conta de email (Gmail recomendado para testes)

### 🚀 Instalação Rápida

```bash
# 1. Clone o repositório
git clone https://github.com/ernanegit/email_django.git
cd email_django

# 2. Crie e ative o ambiente virtual
python -m venv venv

# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Configure as variáveis de ambiente
cp .env.example .env
# Edite o arquivo .env com suas configurações

# 5. Execute as migrações
python manage.py makemigrations
python manage.py migrate

# 6. Crie um superusuário
python manage.py createsuperuser

# 7. Execute o servidor
python manage.py runserver
```

### 🔧 Configuração Detalhada

#### 📧 Configuração de Email

**Para Desenvolvimento (Console):**
```python
# Já configurado por padrão
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

**Para Produção (Gmail):**
1. **Ative a verificação em 2 etapas** no Gmail
2. **Gere uma senha de aplicativo:**
   - Acesse: https://myaccount.google.com/apppasswords
   - Crie nova senha para "Django App"
3. **Configure no arquivo .env:**
   ```env
   EMAIL_USER=seu_email@gmail.com
   EMAIL_PASSWORD=senha_de_aplicativo_gerada
   ```

#### 🔐 Configuração de Segurança

**Arquivo .env completo:**
```env
# Configurações do Django
SECRET_KEY=sua_chave_secreta_django_muito_longa_e_segura_aqui
DEBUG=True

# Configurações de Email
EMAIL_USER=seu_email@gmail.com
EMAIL_PASSWORD=sua_senha_de_aplicativo_gmail

# Configurações de Database (Produção)
DB_NAME=nome_do_banco
DB_USER=usuario_banco
DB_PASSWORD=senha_banco
DB_HOST=localhost
DB_PORT=5432
```

## 📁 Estrutura do Projeto

```
email_django/
├── 📁 accounts/                    # App principal de autenticação
│   ├── 📄 models.py               # CustomUser e modelos relacionados
│   ├── 📄 views.py                # Views de autenticação e dashboard
│   ├── 📄 forms.py                # Formulários customizados
│   ├── 📄 managers.py             # Manager do CustomUser
│   ├── 📄 tokens.py               # Gerador de tokens de verificação
│   ├── 📄 utils.py                # Utilitários (envio de email)
│   ├── 📄 urls.py                 # URLs do app accounts
│   ├── 📄 admin.py                # Configuração da interface admin
│   └── 📁 migrations/             # Migrações do banco de dados
├── 📁 auth_project/               # Configurações do projeto Django
│   ├── 📄 settings.py             # Configurações principais
│   ├── 📄 urls.py                 # URLs principais do projeto
│   ├── 📄 wsgi.py                 # Configuração WSGI
│   └── 📄 asgi.py                 # Configuração ASGI
├── 📁 templates/                  # Templates HTML organizados
│   ├── 📄 base.html               # Template base com Bootstrap
│   └── 📁 accounts/               # Templates específicos do accounts
│       ├── 📄 login.html          # Página de login
│       ├── 📄 register.html       # Página de registro
│       ├── 📄 dashboard.html      # Dashboard do usuário
│       ├── 📄 verify_email_sent.html        # Confirmação de envio
│       └── 📄 verification_email.html       # Template do email
├── 📁 static/                     # Arquivos estáticos
│   ├── 📁 css/                    # Estilos customizados
│   ├── 📁 js/                     # JavaScript customizado
│   └── 📁 img/                    # Imagens do projeto
├── 📁 docs/                       # Documentação e screenshots
│   ├── 📁 images/                 # Screenshots do sistema
│   │   ├── 🖼️ login-preview.png           # Screenshot do login
│   │   ├── 🖼️ dashboard-preview.png       # Screenshot do dashboard
│   │   └── 🖼️ email-verification-preview.png # Screenshot verificação
│   └── 📄 CHANGELOG.md            # Histórico de mudanças
├── 📄 .env.example               # Template de configuração
├── 📄 .gitignore                 # Arquivos ignorados pelo Git
├── 📄 requirements.txt           # Dependências Python
├── 📄 manage.py                  # Utilitário de linha de comando Django
└── 📄 README.md                  # Este arquivo
```

## 🎯 Como Usar o Sistema

### 1️⃣ Registro de Novo Usuário
1. **Acesse:** `http://127.0.0.1:8000/accounts/register/`
2. **Preencha:** Email, nome, sobrenome e senha
3. **Clique:** "Registrar"
4. **Aguarde:** Redirecionamento para página de confirmação

### 2️⃣ Verificação de Email
1. **Verifique:** Console do Django (desenvolvimento) ou email (produção)
2. **Copie:** Link de verificação
3. **Acesse:** Link no navegador
4. **Confirme:** Ativação da conta

### 3️⃣ Login no Sistema
1. **Acesse:** `http://127.0.0.1:8000/accounts/login/`
2. **Digite:** Email e senha cadastrados
3. **Clique:** "Entrar"
4. **Redirecionamento:** Automático para dashboard

### 4️⃣ Usando o Dashboard
- **Visualize:** Informações pessoais
- **Confirme:** Status de verificação de email
- **Acesse:** Funcionalidades disponíveis
- **Gerencie:** Perfil do usuário

## 🚀 Deploy para Produção

### 🌐 Configurações para Produção

```python
# settings.py - Configurações de produção
DEBUG = False
ALLOWED_HOSTS = ['seudominio.com', 'www.seudominio.com']

# Database para produção (PostgreSQL recomendado)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}
```

### ☁️ Deploy com Heroku
```bash
# 1. Instalar Heroku CLI e fazer login
heroku login

# 2. Criar aplicação
heroku create nome-do-seu-app

# 3. Configurar variáveis de ambiente
heroku config:set SECRET_KEY=sua_chave_secreta_produção
heroku config:set DEBUG=False
heroku config:set EMAIL_USER=seu_email@gmail.com
heroku config:set EMAIL_PASSWORD=sua_senha_aplicativo

# 4. Deploy
git push heroku main

# 5. Executar migrações
heroku run python manage.py migrate

# 6. Criar superusuário
heroku run python manage.py createsuperuser

# 7. Coletar arquivos estáticos
heroku run python manage.py collectstatic --noinput
```

## 🧪 Testes e Qualidade

### 🔍 Executar Testes
```bash
# Executar todos os testes
python manage.py test

# Testes específicos do app accounts
python manage.py test accounts

# Testes com cobertura
pip install coverage
coverage run --source='.' manage.py test
coverage report
coverage html  # Gerar relatório HTML
```

### ✅ Checklist de Qualidade
- [ ] Todos os testes passando
- [ ] Cobertura de testes > 80%
- [ ] Sem vulnerabilidades de segurança
- [ ] Performance otimizada
- [ ] Documentação atualizada

## 📈 Roadmap e Melhorias Futuras

### 🎯 Próximas Funcionalidades
- [ ] **Reset de senha** via email com tokens seguros
- [ ] **Perfil de usuário** editável com campos adicionais
- [ ] **Upload de foto** de perfil com redimensionamento
- [ ] **Autenticação de dois fatores** (2FA) via SMS/App
- [ ] **Login social** (Google, GitHub, Facebook, LinkedIn)
- [ ] **API REST** com Django REST Framework
- [ ] **Notificações** em tempo real com WebSockets
- [ ] **Histórico de logins** e atividades do usuário
- [ ] **Sistema de roles** e permissões granulares

### 🔧 Melhorias Técnicas
- [ ] **Testes automatizados** com 100% cobertura
- [ ] **CI/CD** com GitHub Actions
- [ ] **Containerização** com Docker
- [ ] **Cache** com Redis para performance
- [ ] **Monitoramento** com Sentry
- [ ] **Logs estruturados** com ELK Stack
- [ ] **Rate limiting** para APIs
- [ ] **Backup automatizado** do banco de dados

### 🎨 Melhorias de Interface
- [ ] **Tema escuro/claro** com toggle
- [ ] **PWA** (Progressive Web App)
- [ ] **Animações** e micro-interações
- [ ] **Dashboard** mais elaborado com gráficos
- [ ] **Internacionalização** (i18n) multi-idiomas

## 🤝 Contribuição

### 📋 Como Contribuir
1. **Fork** o repositório
2. **Crie uma branch** para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. **Implemente** a funcionalidade seguindo os padrões do projeto
4. **Escreva testes** para a nova funcionalidade
5. **Execute** os testes para garantir que não quebrou nada
6. **Commit** suas mudanças (`git commit -m 'feat: adiciona nova funcionalidade'`)
7. **Push** para sua branch (`git push origin feature/nova-funcionalidade`)
8. **Abra um Pull Request** detalhado

### 🎯 Diretrizes de Contribuição
- Siga as convenções de código PEP 8
- Escreva testes para novas funcionalidades
- Mantenha a cobertura de testes alta
- Atualize a documentação quando necessário
- Use commits semânticos (feat, fix, docs, style, refactor, test, chore)
- Seja descritivo nos Pull Requests

### 🐛 Reportar Bugs
- Use os [GitHub Issues](https://github.com/ernanegit/email_django/issues)
- Inclua passos para reproduzir o bug
- Adicione screenshots se relevante
- Especifique versão do Python e Django

## 📊 Estatísticas do Projeto

| Métrica | Valor |
|---------|-------|
| **Linhas de código** | ~2000+ |
| **Arquivos Python** | 15+ |
| **Templates HTML** | 6 |
| **Funcionalidades** | 20+ |
| **Testes** | Em desenvolvimento |
| **Documentação** | Completa |

## 🏆 Reconhecimentos

### 🙏 Agradecimentos
- **Django Framework** pela excelente documentação e flexibilidade
- **Bootstrap Team** pela framework CSS responsiva
- **Python Community** pelo suporte e recursos
- **GitHub** pela plataforma de desenvolvimento colaborativo

### 📚 Recursos Utilizados
- [Django Documentation](https://docs.djangoproject.com/)
- [Bootstrap Documentation](https://getbootstrap.com/docs/)
- [Python.org](https://www.python.org/)
- [Real Python Tutorials](https://realpython.com/)

## 📞 Suporte e Contato

### 🆘 Onde Buscar Ajuda
- **Issues:** [GitHub Issues](https://github.com/ernanegit/email_django/issues)
- **Discussões:** [GitHub Discussions](https://github.com/ernanegit/email_django/discussions)
- **Email:** ernane1974@outlook.com

### 👨‍💻 Sobre o Autor
**Ernane Silva**
- 🐙 **GitHub:** [@ernanegit](https://github.com/ernanegit)
- 📧 **Email:** ernane1974@outlook.com
- 💼 **LinkedIn:** [Perfil do Ernane](https://linkedin.com/in/ernanegit)
- 🌐 **Portfólio:** Em desenvolvimento

## 📄 Licença

Este projeto está licenciado sob a **Licença MIT** - veja o arquivo [LICENSE](LICENSE) para detalhes completos.

### 📋 Resumo da Licença
- ✅ Uso comercial permitido
- ✅ Modificação permitida
- ✅ Distribuição permitida
- ✅ Uso privado permitido
- ❌ Responsabilidade limitada
- ❌ Garantia não fornecida

---

<div align="center">

**⭐ Se este projeto foi útil para você, considere dar uma estrela no repositório! ⭐**

**🚀 Desenvolvido com ❤️ por [Ernane Silva](https://github.com/ernanegit) 🚀**

**📅 Última atualização: Julho 2025**

