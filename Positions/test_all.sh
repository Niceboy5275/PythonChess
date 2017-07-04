for file in `ls -1 solution*.txt`
do
    python ../classes/chess_simple.py < $file > output_$file
    nbLines=`cat output_$file | grep "Echec et mat !" | wc -l`
    if [ $nbLines -ne 1 ]
    then
        echo 'Error with file '$file
    fi
    output_ref=`echo "output_$file" | sed 's/txt/ref/g'`
    dos2unix output_$file
    dos2unix $output_ref
    nbLines=`diff  output_$file $output_ref | wc -l`
    if [ $nbLines -ne 0 ]
    then
        diff  output_$file $output_ref
        echo 'Error with file '$file
    else
        rm output_$file
    fi
done
