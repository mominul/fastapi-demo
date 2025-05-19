FROM ghcr.io/astral-sh/uv:python3.12-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

RUN uv sync

# Make port 8000 available to the world outside this container
EXPOSE 8000

ENTRYPOINT ["./entrypoint.sh"]
