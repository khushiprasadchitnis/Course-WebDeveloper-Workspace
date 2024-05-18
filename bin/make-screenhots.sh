find . -name *.html 				|\
grep -v node_modules 				|\
while read FILE
do
	SHOT=${FILE/.html/.png};
	SHOT=${SHOT/solution/exercise};

	echo "$FILE -> $SHOT"

	node screenshot.js  $FILE $SHOT
done

