# Ancient-Mitochondrial-Database-AmtDB

1.  Understanding the role of dinucleotides, especially CpG dinucleotides in the evolution of human mitochondrial DNA             sequences

2.  Download all the fasta files available on the AmtDB website(https://amtdb.org/records/)
    
3.  Keep them all in a common folder. Name the folder as AmtDB
    
4.  Paste the fastaFileReader.py, bashScript.sh in that same folder.
    
5.  To run the bashScript.sh, paste the command below in the terminal
    
    ```bash
    sh bashScript.sh
    ```
    
    *bashScript is a script in bash that will run the fastaFileReader.py on all the fasta files and will merge all the output files to give a single output file.*
    
6.  You'll get a merged.csv in that same folder along with the other csv files created
    
7.  Create a new folder named Data and paste the merged.csv in that folder.
    
8.  Now return to the folder in which all the analysis was done
    
9.  To remove all the csv files in that folder, paste the command below in the terminal
    
    ```bash
    rm *.csv
    ```
    
10.  If you want to delete all the fasta files in that folder too, paste the command below in the terminal
    
    ```bash
    rm *.fa
    ```
    
11.  Now copy the reference table from the website([https://amtdb.org/records/](https://amtdb.org/records/)) and paste it into an excel sheet. Save it as a .csv file(with separator as tab). Name the file as ReferenceTable.csv
    
12.  Rename the second column of ReferenceTable.csv as info(instead of Name). Now, sort the files according to the column named 'info'.
    
13.  After the sorting is done, check for some entries manually and then merge them both into a same datafile and name that datafile as *[mergedData.csv]()*
    
    [*mergedData.csv*]() is the file needed to analyse now.
    

#### Checking if all the needds for the code are satisfied on your system or not. We've used Python3 for this purpose along with bash scripting. You'll need to have Python3(3.5.x or higher) installed on your system along with some of its modules (pandas, openpyxl)

*How to check if you've python3 installed on your system or not:*

-   Either paste the command below in your terminal
    
    ```bash
    python3 --version
    ```
    

-   You should get some output like Python 3.x.x (e.g Python 3.6.5) if it's installed or you can go to the directory of the script python3Checker.sh and run it by pasting the command below in the terminal
    
    ```bash
    sh python3Checker.sh
    ```
    

It'll print out a statement based on if it's installed or not

*How to install python3:*

Two methods are generally followed

-   Method 1: normal installation (for ubuntu(linux) users)
    
    ```bash
    sudo apt-get install python3
    ```
    

-   Method 2: installing python3 using package managers(Homebrew/Linuxbrew, Macport, etc)
    
    if you've brew(Homebrew/Linuxbrew) installed on your system, then paste the command below in the terminal(to check for brew, just type brew in terminal, if it gives any error then it's not installed but if it gives some options, then it's installed)
    
    ```bash
    brew install python3
    ```
    

Similar can be done for other package managers too but you've to read their documentation online.

*How to know if the modules required are installed in your python environment or not:*

Paste the command below in your terminal

```bash
python -c "import module_name"
```

It'll print out a statement based on if it's installed or not

-   If a module exists in the system, then you won't get any error and run the command below to verify it
    
    ```bash
    echo $?
    ```
    

If you get a '0' as an output, then that means that the module we looked for exists in system

-   If a module doesn't exists in the system, then you'll get an error like this
    
    ```bash
    Traceback (most recent call last):
     File "", line 1, in 
     ImportError: No module named numpy
    to further verify it, paste the command below
    echo $?
    ```
    

If you get a '1' as an output, then that means that the module we looked for does not exists in system

*How to install a module:*

Two methods are generally followed

-   Method 1 (recommended): Paste the command below to install the desired module(this command works for both Mac OS and linux systems)
    
    ```bash
    pip3 install module_name
    ```
    

-   Method 2: Paste the command below. this is a ubuntu(linux) specific command and can't be used in Mac OS
    
    ```bash
    sudo apt-get install python3-module_name
    ```
