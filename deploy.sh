#!/bin/bash
echo "🚀 Iniciando el despliegue de la infraestructura en AWS..."

aws cloudformation deploy \
  --template-file infra.yml \
  --stack-name MiStackDePipeline \
  --parameter-overrides ConnectionArn="arn:aws:codeconnections:us-east-1:047719650114:connection/b86342db-e9e5-47e1-b08d-d7b255a072ce" GitHubRepo="Asdrubal82212/trabajofinal" \
  --capabilities CAPABILITY_IAM

echo "✅ ¡Despliegue completado con éxito!"