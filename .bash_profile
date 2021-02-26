if [[ -z $DISPLAY ]] && [[ $(tty) = /dev/tty1 ]]; then exec startx; fi

REPO=dsl-wall
cd ~/"$REPO"
UNCOMMITTED_CHANGES=$(git status --porcelain 2>/dev/null | wc -l)
if [ "$UNCOMMITTED_CHANGES" -gt 0 ]
then
        echo "WARNING: The repo $REPO has uncommitted changes!"
fi
