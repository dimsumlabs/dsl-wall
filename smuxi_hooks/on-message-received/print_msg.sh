#!/bin/bash

# A Smuxi hook script. This hooks flashes the ceiling light when a new message
# on the #dimsumlabs channel was received.
#
# Usage: put this script in
# ~/.local/share/smuxi/hooks/engine/protocol-manager/on-message-received/
# and chmod +x it

if [ "$SMUXI_CHAT_ID" != "#dimsumlabs" ]; then
    exit 0
fi

# Sends ESC/P command
send_esc() {
	echo -en "\x1b$1" | lpr
}

echo -n "$SMUXI_MSG_TIMESTAMP_ISO_LOCAL " | lpr
send_esc 4 # Select italic
echo -n "$SMUXI_SENDER " | lpr
send_esc 5 # Cancel italic
echo $SMUXI_MSG \
	| iconv -f utf-8 -t 437 -c \
        | lpr
