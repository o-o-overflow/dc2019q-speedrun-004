#!/bin/sh -e

RESULT=$(echo "adam" | nc "$1" "$2")
echo "$RESULT" | grep "i think i'm getting better at this coding thing."
echo "$RESULT" | grep "how much do you have to say?"
echo "$RESULT" | grep "That's not much to say."
echo "$RESULT" | grep "see ya later slowpoke."

RESULT=$(echo "3000" | nc "$1" "$2")
echo "$RESULT" | grep "That's too much to say!"

RESULT=$(python -c "print('2      ' + 'a'*2)" | nc "$1" "$2")
echo "$RESULT" | grep "Ok, what do you have to say for yourself?"
echo "$RESULT" | grep "Interesting thought"
echo "$RESULT" | grep "I'll take it into consideration."

