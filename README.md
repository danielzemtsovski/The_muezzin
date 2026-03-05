# The_muezzin

docker compose -p project_to_test up -d --build

docker build -t send_metadata .

docker run --rm --network project_to_test_default -v "${PWD}/podcasts:/app/podcasts" -e KAFKA_URI=kafka:9092 -e FOLDER_PATH=/app/podcasts send_metadata

docker build -t consumption_and_processing .

docker run --rm --network project_to_test_default -v "${PWD}/podcasts:/app/podcasts" -e ELASTIC_URI=http://elasticsearch:9200 -e KAFKA_URI=kafka:9092 -e MONGO_URI=mongodb://mongodb:27017 -e FOLDER_PATH=/app/podcasts consumption_and_processing