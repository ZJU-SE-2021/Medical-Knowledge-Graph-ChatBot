FROM neo4j:latest

COPY ./graph_data /data
ENV NEO4J_AUTH=none