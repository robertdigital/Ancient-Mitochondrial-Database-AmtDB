for fa in *.fa; do \
    python3 fastaFileReader.py "$fa"
done 

cat AH1.csv | head -n1 > merged.csv #you can choose a random csv file. we just need one random csv file for taking a header
for f in *.csv; do cat "`pwd`/$f" | tail -n +2 >> merged.csv; done 