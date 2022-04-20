# app-postgres

Passo 1: Clonar o repositório: 
  git clone https://github.com/jasonthiago/app-postgres.git

Passo 2: Entrar no diretório app-postgres
  cd app-postgress
 
Passo 3: Rodar o Compose ou rodar via swarm 
  via docker-compose: docker-compose up
  via swarm: docker stack deploy -c docker-compose.yaml stackGalaticos
  
Passo 4: Testar a API
  curl localhost:5000
  curl localhost:5000:/teste
