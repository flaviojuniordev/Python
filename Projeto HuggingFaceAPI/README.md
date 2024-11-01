# Gerador de Imagens com Hugging Face

Este projeto é um gerador de imagens que utiliza a API do Hugging Face para criar imagens a partir de descrições fornecidas pelo usuário. A interface é construída com Tkinter e permite a geração e salvamento das imagens geradas.

## Funcionalidades

- Geração de imagens a partir de um texto descritivo.
- Opção de salvar a imagem gerada no formato PNG.
- Interface amigável e intuitiva.

## Dependências

Para executar este projeto, você precisará das seguintes bibliotecas Python:

- `requests`: Para fazer requisições HTTP à API do Hugging Face.
- `Pillow`: Para manipulação de imagens.
- `tkinter`: Para a interface gráfica do usuário.

Você pode instalar as dependências necessárias utilizando o seguinte comando:

```bash
pip install requests Pillow
```

## Como Criar Seu Próprio Token no Hugging Face

Para usar a API do Hugging Face, você precisará criar um token de autenticação. Aqui estão os passos:

1. **Criar uma Conta**:
   - Acesse o site do Hugging Face: [Hugging Face](https://huggingface.co/).
   - Se você não tem uma conta, clique em **Sign Up** para criar uma.

2. **Fazer Login**:
   - Após criar sua conta, faça login clicando em **Login** no canto superior direito.

3. **Acessar Configurações de Token**:
   - Após o login, clique no seu nome de usuário no canto superior direito e selecione **Settings**.
   - Na página de configurações, encontre a seção **Access Tokens**.

4. **Criar um Novo Token**:
   - Clique em **New token**.
   - Dê um nome ao seu token e selecione as permissões necessárias. Para uso básico, as permissões padrão são suficientes.
   - Clique em **Generate** para criar o token.

5. **Copiar o Token**:
   - Uma vez gerado, copie o token que foi exibido. **Mantenha esse token em segredo**, pois ele concede acesso à sua conta.

## Integrar o Token ao Código

Depois de obter seu token, você precisa integrá-lo ao seu código no arquivo `app.py`. Encontre a linha:

Substitua pelo seu token copiado:

```python
headers = {"Authorization": "Bearer hf_coloqueseutokenaqui"}  # Coloque seu token aqui
```

## Considerações Finais

- **Segurança**: Nunca compartilhe seu token publicamente e evite incluí-lo diretamente no código que será versionado em sistemas de controle de versão como Git. Considere usar variáveis de ambiente para armazená-lo de forma mais segura.
- **Limites de Uso**: Fique atento ao uso da API, pois pode haver limites dependendo do seu plano na Hugging Face.

## Execução do Projeto

Para executar o projeto, basta rodar o arquivo `app.py`:

```bash
python app.py
```

Aproveite o seu gerador de imagens!
