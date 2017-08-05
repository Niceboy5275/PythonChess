export PATH=/c/Users/Vincent/AppData/Local/Programs/Python/Python36:$PATH
for file in `ls -1 | egrep "^solution_[0-9]+.txt"`
do
    echo -n '.'
    python ../classes/chess_main.py < $file > output_simple_$file
    nbLines=`cat output_simple_$file | grep "Echec et mat !" | wc -l`
    if [ $nbLines -ne 1 ]
    then
        echo -n 'F1S'
    fi
    output_ref=`echo "output_simple_$file" | sed 's/txt/ref/g'`
    touch $output_ref
    dos2unix $output_ref 2> /dev/null
    dos2unix output_simple_$file 2> /dev/null
    nbLines=`diff  output_simple_$file $output_ref | wc -l`
    if [ $nbLines -ne 0 ]
    then
        mv output_simple_$file $output_ref
        echo -n 'F2S'
    else
        rm output_simple_$file
    fi
done
echo ""
for file in `ls -1 solution_*.txt | egrep -v "^solution_[0-9]+.txt"`
do
    echo -n '.'
    python ../classes/chess_main.py < $file > output_simple_$file
    output_ref=`echo "output_simple_$file" | sed 's/txt/ref/g'`
    touch $output_ref
    dos2unix $output_ref 2> /dev/null
    dos2unix output_simple_$file 2> /dev/null
    nbLines=`diff  output_simple_$file $output_ref | wc -l`
    if [ $nbLines -ne 0 ]
    then
        mv output_simple_$file $output_ref
        echo -n 'F2S'
    else
        rm output_simple_$file
    fi
done
echo ""
for file in `ls -1 | egrep "^solution_[0-9]+.txt"`
do
    echo -n '.'
    python ../classes/chess_main.py linux < $file > output_linux_$file
    nbLines=`cat output_linux_$file | grep "Echec et mat !" | wc -l`
    if [ $nbLines -ne 1 ]
    then
        echo -n 'F1L'
    fi
    output_ref=`echo "output_linux_$file" | sed 's/txt/ref/g'`
    touch $output_ref
    dos2unix $output_ref 2> /dev/null
    dos2unix output_linux_$file 2> /dev/null
    nbLines=`diff  output_linux_$file $output_ref | wc -l`
    if [ $nbLines -ne 0 ]
    then
        mv output_linux_$file $output_ref
        echo -n 'F2L'
    else
        rm output_linux_$file
    fi
done
echo ""
for file in `ls -1 solution_*.txt | egrep -v "^solution_[0-9]+.txt"`
do
    echo -n '.'
    python ../classes/chess_main.py < $file > output_linux_$file
    output_ref=`echo "output_linux_$file" | sed 's/txt/ref/g'`
    touch $output_ref
    dos2unix $output_ref 2> /dev/null
    dos2unix output_linux_$file 2> /dev/null
    nbLines=`diff  output_linux_$file $output_ref | wc -l`
    if [ $nbLines -ne 0 ]
    then
        mv output_linux_$file $output_ref
        echo -n 'F2L'
    else
        rm output_linux_$file
    fi
done
