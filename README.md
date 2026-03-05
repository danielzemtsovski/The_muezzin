# The_muezzin

docker compose -p project_to_test up -d --build

docker build -t send_metadata .

docker run --rm --network project_to_test_default -v "${PWD}/../podcasts:/app/podcasts" --env-file ../.env send_metadata

docker build -t consumption_and_processing .

docker run --rm --network project_to_test_default -v "${PWD}/../podcasts:/app/podcasts" --env-file ../.env consumption_and_processing