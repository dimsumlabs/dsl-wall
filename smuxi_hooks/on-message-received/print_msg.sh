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

ESC="\x1b"
ITALIC_ON="${ESC}4"
ITALIC_OFF="${ESC}5"
(
	echo -n "$SMUXI_MSG_TIMESTAMP_ISO_LOCAL "
	echo -ne "$ITALIC_ON"
	echo -n "$SMUXI_SENDER"
	echo -ne "$ITALIC_OFF"
	echo " $SMUXI_MSG"
) | iconv -f utf-8 -t 437 -c \
  | lpr &
