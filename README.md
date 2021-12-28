# ResearchFinTech
These files are used for automatically download the SEC reports for corresponding SPACs. In addition, the python files can also help to search the team members'
background information for each SPAC company. 

In order to do so, first you will have to run the "research.py" file, this file contains an module that will help to download all the report links (in tsv formats).

Then, run the "main.py" this file will automatically search for report links, which is only relevant to SPAC, but keep in mind that in "main.py" there are also functions used from
other files such as "data_process_2.py" and "find_company_reports_short.py", so please put these files under the same directory with "main.py" in order to work!

After that, the urls (report links) will be printed on the terminals, these urls are the reports for SPACs only. Copy and paste these url from terminals, but I have already did.

Use these urls, then we could run "get_tables.py" to grab the tables from the reports which contains only information of each SPACs members (name, age, title/positions). Note 
that these tables will be saved in different csv files for latter usage.

Finally, run "get_name.py", this file will generate the last name from each csv file and then pass into the "get_html_test.py" to grab the corresponding texts we need for annotating.

I have commentted some of my codes

Run python command is : "python3 [file_name].py"
