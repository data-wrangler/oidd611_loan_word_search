IMAGES=./*.png
for f in $IMAGES
do
    echo "Processing $f..."
    gocr -p ../../gocr/ -i $f -C ABCDEFGHIJKLMNOPQRSTUVWXYZ -m 167 -o $f.txt
done

echo "" > consolidated_list.out
TEXTFILES=./*.txt
for f in $TEXTFILES
do
    cat $f | tr "\n" " " >> consolidated_list.out
    echo "" >> consolidated_list.out
done
