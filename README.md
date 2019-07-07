# Ancient-Mitochondrial-Database-AmtDB
Understanding the role of dinucleotides, especially CpG dinucleotides in the evolution of human mitochondrial DNA sequences


Download all the fasta files available on the AmtDB website(https://amtdb.org/records/)
Keep them all in a common folder. Name the folder as AmtDB

Paste the fastaFileReader.py, bashScript.sh in that same folder
Now check if all the needds for the code are satisfied on your system or not. We've used Python3 for this purpose along with bash scripting. You'll need to have Python3 installed on your system along with some of its modules (pandas, openpyxl)


how to check if you've python3 installed on your system or not:
Either paste the command below in your terminal
> python3 --version

You should get some output like Python 3.x.x (e.g Python 3.6.5) if it's installed
Or you can go to the directory of the script python3Checker.sh and run it by pasting the command below in the terminal
> sh python3Checker.sh

It'll print out a statement based on if it's installed or not


how to install python3:
two methods are generally followed
method1: normal installation (for ubuntu(linux) users)
> sudo apt-get install python3

method2: installing python3 using package managers
if you've brew installed on your system, then paste the command below in the terminal(to check for brew, just type brew in terminal, if it gives any error then it's not installed but if it gives some options, then it's installed)
> brew install python3


how to know if the modules required are installed in your python environment or not:
paste the command below in your terminal
> python -c "import module_name"

if a module exists in the system, then you won't get any error and run the command below to verify it
> echo $?  

if you get a '0' as an output, then that means that the module we looked for exists in system

if a module doesn't exists in the system, then you'll get an error like this

> Traceback (most recent call last):
> 	  File "<string>", line 1, in <module>
> 	ImportError: No module named numpy
to further verify it, paste the command below
> echo $?
	
if you get a '1' as an output, then that means that the module we looked for does not exists in system


how to install a module:
two methods are generally followed.
method1(recommended): paste the command below to install the desired module(this command works for both Mac OS and linux systems)
> pip3 install module_name

method2: paste the command below. this is a ubuntu(linux) specific command and can't be used in Mac OS
> sudo apt-get install python3-module_name

Now that all the needs are satisfied on your system, we'll run the scripts
bashScript is a script in bash that will run the fastaFileReader.py on all the fasta files and will merge all the output files to give a single output file
To run the bashScript.sh, paste the command below in the terminal
> sh bashScript.sh

You'll get a merged.csv in that same folder along with the other csv files created
Create a new folder named Data and paste the merged.csv in that folder
Now return to the folder in which all the analysis was done
To remove all the csv files in that folder, paste the command below in the terminal
> rm *.csv

If you want to delete all the fasta files in that folder too, paste the command below in the terminal
> rm *.fa

Now copy the reference table from the website(https://amtdb.org/records/) and paste it into an excel sheet. Save it as a .csv file(with separator as tab). Name the file as ReferenceTable.csv
Open the merged.csv, ReferenceTable.csv in the application of your choice(MS Excel, LibreOffice, OpenOffice, Numbers). NOTE: MS Excel converts entries like Jan1 to Jan-01 or 01-Jan which will create problems for our further analysis. I'd recommend using OpenOffice or LibreOffice
Rename the second column of ReferenceTable.csv as info(instead of Name)
Now, sort the files according to the column named 'info'
After the sorting is done, check for some entries manually and then merge them both into a same datafile and name that datafile as mergedData.csv
mergedData.csv is the file needed to analyse now.





