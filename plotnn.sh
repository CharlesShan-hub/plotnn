#!/bin/bash
python "./models/$1.py"
pdflatex -output-directory="./models" "./tmp/$1.tex"

rm ./models/*.aux ./models/*.log ./models/*.vscodeLog
rm ./tmp/*

# if [[ "$OSTYPE" == "darwin"* ]]; then
#     open $1.pdf
# else
#     xdg-open $1.pdf
# fi
