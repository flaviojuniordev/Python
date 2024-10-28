# Internet Velocity Test

Este aplicativo, desenvolvido com [Streamlit](https://streamlit.io/) e [speedtest-cli](https://pypi.org/project/speedtest-cli/), realiza um teste de velocidade da internet, medindo as velocidades de download, upload e o ping.

## Requisitos

Antes de iniciar, certifique-se de ter Python e as bibliotecas necessárias instaladas:

- **Streamlit**: Interface para o aplicativo web.
- **speedtest-cli**: Realiza o teste de velocidade.

### Instalando as Dependências

Execute o comando abaixo para instalar as bibliotecas:

```bash
pip install streamlit speedtest-cli
```

## Estrutura do Código

O código possui três funções principais:

1. `run_speedtest()`: Executa o teste de velocidade e retorna as velocidades de download e upload (em Mbps) e o ping.
2. `display_results(download_speed, upload_speed, ping)`: Exibe os resultados no aplicativo, incluindo as barras de progresso para download e upload.
3. `main()`: Interface principal do Streamlit, com um botão para iniciar o teste.

## Executando o Aplicativo

Para iniciar o aplicativo, execute o seguinte comando no terminal:

```bash
streamlit run internetvelocity.py
```

## Exemplo de Uso

1. Clique no botão **Iniciar** para começar o teste.
2. Aguarde o cálculo da velocidade.
3. Veja os resultados:
   - **Velocidade de Download**: Em Mbps com uma barra de progresso (máximo de 100 Mbps).
   - **Velocidade de Upload**: Em Mbps com uma barra de progresso (máximo de 100 Mbps).
   - **Ping**: Tempo de resposta em milissegundos.

---

**Autor**: [Flávio Júnior]

