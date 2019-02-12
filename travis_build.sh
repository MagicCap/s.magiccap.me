if [ "$TRAVIS_TAG" != "" ]
then
    zappa update
fi
