#!/bin/bash

# Check if any arguments are passed
if [ "$#" -lt 1 ]; then
    docker-compose up
else
    # Change directory to math_module
    cd ./math_module

    # Get view, layout, and IP from config_getter.py
    view=$(python config_getter.py -v | tr -d '\r')
    layout=$(python config_getter.py -l | tr -d '\r')
    ip=$(python config_getter.py -h | tr -d '\r')

    # Copy layout to specific locations
    cp -f "$layout" ./data/layout.json
    echo "Layout Copied into math_module/data"
    cp -f "$layout" ../backend/data/layout.json
    cp -f "$view" ../backend/data/view.svg
    echo "View and Layout copied to backend/data"

    # Change directory to front/map
    cd ../front/map

    # Run Python setup script with IP
    python ./setup.py --ip "$ip"
    
    # Install npm dependencies and build project
    npm install
    npm run build

    # Create directories if they don't exist and copy files
    mkdir -p ../../backend/data/dist/
    cp -f ./dist/* ../../backend/data/dist

    mkdir -p ../../backend/data/dist/assets/
    cp -f ./dist/assets/* ../../backend/data/dist/assets

    echo "All compiled frontend files moved to backend/data"

    # Change directory to backend
    cd ../../backend/

    echo "All composer modules installed"

    # Go back to the original directory
    cd ..

    # Build and start the Docker containers
    docker-compose build
    docker-compose up
fi