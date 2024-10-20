# Automação de Tagueamento com AWS Lambda

## Visão Geral

Este projeto demonstra uma solução automatizada para aplicar tags a todos os recursos recém-criados na AWS usando o AWS Lambda. Inclui um pipeline CI/CD para automatizar os processos de build, teste e deploy da função Lambda responsável por aplicar as tags em sua infraestrutura AWS.

A automação é disparada sempre que novos recursos são criados. A função Lambda aplicará as tags predefinidas a esses recursos, ajudando a manter o controle e gerenciamento de sua infraestrutura AWS.

## Funcionalidades

- **Função Lambda**: Aplica automaticamente tags a todos os recursos recém-criados na AWS.
- **Pipeline CI/CD**: Automatiza os processos de build, teste e deploy da função Lambda.
- **Template CloudFormation**: Implanta toda a infraestrutura, incluindo a função Lambda, roles do IAM e CodePipeline.
- **Integração com CodeBuild**: Os processos de build e teste são gerenciados pelo AWS CodeBuild.
- **S3 para Armazenamento de Artefatos**: Armazena o pacote de deploy da Lambda e artefatos de build em um bucket S3.

## Arquitetura

O projeto segue um fluxo CI/CD que consiste nas seguintes etapas:

1. **Source**: O código é armazenado em um repositório AWS CodeCommit ou qualquer sistema de controle de versão (como GitHub).
2. **Build**: O CodeBuild compila a função Lambda e a empacota em um arquivo zip para deploy.
3. **Test**: A função é testada utilizando um setup básico de pytest.
4. **Deploy**: O CodePipeline usa o CloudFormation para fazer o deploy ou atualizar a função Lambda.

A função Lambda escuta eventos relacionados à criação de recursos usando o AWS CloudTrail ou EventBridge, e automaticamente aplica as tags aos novos recursos criados.

## Pré-requisitos

Para executar este projeto, certifique-se de ter o seguinte:

- AWS CLI instalado e configurado
- Um bucket S3 para armazenar o pacote de deploy da Lambda e artefatos
- Repositório AWS CodeCommit (ou GitHub) para armazenar o código do projeto
- Conhecimento básico de serviços AWS como Lambda, CodePipeline, CloudFormation e CodeBuild

## Estrutura do Repositório

O projeto está organizado da seguinte forma:

```plaintext
.
├── lambda_function.py           # Código da função Lambda que aplica tags nos recursos AWS
├── buildspec.yml                # Arquivo de configuração do build para o AWS CodeBuild
├── pipeline.yaml                # Template CloudFormation para deploy do pipeline CI/CD
├── template.yaml                # Template CloudFormation para deploy da função Lambda
└── README.md                    # Documentação do projeto
