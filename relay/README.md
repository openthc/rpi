# Relay Control

These scripts are for controlling relay devices.

## Configuration

Update the relay.tab file for your own configuration.
Each line is one relay definition: `[relay-name]:[physical-pin]`


## Usage

    ./set.sh [RELAY_ID] [open|shut]

## GPIO Pin Selection

When selecting pins for the relay connections be sure to select pins that are 
configured for default HIGH or LOW as needed.

