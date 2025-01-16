# Gerenciamento de Resíduos Perigosos

Este é um projeto desenvolvido em **Python** utilizando a biblioteca **Streamlit** para criar uma interface interativa para o gerenciamento de resíduos perigosos. O aplicativo permite o cadastro de resíduos, visualização de gráficos sobre os dados e consulta de informações climáticas para auxiliar na gestão.

## Funcionalidades

- **Cadastro de Resíduos:** O usuário pode cadastrar resíduos perigosos, informando tipo, volume, local, nível de perigo, responsável, status e data de coleta.
- **Dashboard:** O painel exibe gráficos interativos sobre o volume de resíduos por local, nível de perigo, responsáveis e status dos resíduos.
- **Clima e Alertas:** O aplicativo permite consultar as condições climáticas de um local e exibir alertas sobre temperatura extrema, além de visualizar dados sobre a umidade e vento.

## Tecnologias Utilizadas

- **Streamlit:** Para criar a interface interativa.
- **Pandas:** Para manipulação de dados em tabelas.
- **Plotly:** Para visualização de gráficos interativos.
- **Requests:** Para fazer requisições à API de clima.
- **OpenWeatherAPI:** Usada para obter dados climáticos.

## Pré-Requisitos

Antes de rodar o aplicativo, você precisa instalar as bibliotecas necessárias. Você pode fazer isso executando o seguinte comando:

```bash
pip install streamlit pandas plotly requests
