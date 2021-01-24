# faa_eval
(A video demonstrating the installation and use of the program on Windows can be found [here](https://youtu.be/LOAakilAzmQ).)

# Description
**faa_eval** is a utility written in Python to automate inputs into the Federal Aviation Administration's online structure notification criteria tool found [here](https://oeaaa.faa.gov/oeaaa/external/gisTools/gisAction.jsp?action=showNoNoticeRequiredToolForm). The FAA's webform takes structure data and informs the submitter whether or not filing is required under Title 14, Part 77 of the *Code of Federal Regulations*. However, for large projects with many tall structures (such as power lines and wind farms), entering each structure individually is tedious and error-prone. **faa_eval** saves time by taking an input CSV file and running the webform for each structure, saving the resultant web page and the producing a summary of filing requirements. This summary can then be used in mapping programs such as Google Earth or ArcGIS to present results to clients, engineers, and other project stakeholders.

# Installation
**faa_eval** can be installed on either Linux or Windows. [Python](https://www.python.org) must be installed for it to work. The installation process is similar on the two platforms.

1. Download the repository. Place the faa_eval folder where you would like it to stay.
2. Open a terminal emulator (Linux) or command prompt (Windows) and `cd` into the faa_eval folder.
3. To install necessary dependencies, Run these two commands in the terminal:
    ```sh
    python3 setup.py build
    ```
    ```sh
    python3 setup.py install
    ```
    On Windows, `.py` files may be associated with python already; in this case, run:
    ```
    setup.py build
    ```
    ```
    setup.py install
    ```
4. Download the latest stable release of [chromedriver](https://chromedriver.chromium.org) for your platform. Place it in the faa_eval folder.
5. To link the program to your system, run the platform-dependent setup script:
    - On Linux, run `linux_setup.sh` in a terminal.
    - On Windows, right click `windows_setup.ps1` and select `run with PowerShell`
6. faa_eval can now be run:
    - On Linux, enter `faa_eval` in the terminal emulator to start the program.
    - On Windows, an icon is placed on the desktop that can be double-clicked to run the program.

# How to Use

## Input
Using the [template CSV file](faa_eval_template.csv), enter data for all structures. Input coordinates may be in either decimal degrees or in DMS formats. A brief demonstration of some variety permissible in the inputs is below:

| Structure Designation | Latitude | Longitude | Horizontal Datum | Site Elevation (ft) | Structure Height (ft) | Traverseway? | Is structure on airport? |
| -- | -- | -- | -- | -- | -- | -- | -- |
| 1 | 5d30'25.53"N | 103d35'35"W | NAD83 | 55.9 | 200.02 | No Traverseway | No |
| 1/1 | 50d 45' 17.59"S | 103d20'18.75" | NAD83 | 700 | 150.13 | No Traverseway | No |
| Turbine #3 | -30.45351 | -97.89134 | NAD27 | 1000.751 | 499.5 | Public Roadway | No |

Take care that the **Traverseway?** field matches that on the FAA website.

## Run
1. Run **faa_eval**.
2. **faa_eval** prompts for the input path with the CSV; either: 
    * Press `Enter` to open a file picker and select the file.
    * Enter text with the full path and file name and press `Enter`.
3. **faa_eval** then prompts for the output file path; either:  
    * Press `Enter` to default to the path from step 2.
    * Input a path.

***Note***: The recommended and easy way to use **faa_eval** is to create a dated and tracked folder and use the folder for the input CSV and output.

 ### Linux Only
 On Linux only, relative path references are supported for steps 2 and 3. These are all identical inputs when running from the terminal:
 ```sh
 user@sys:~$ ./faa_data/project_info.csv
 user@sys:~$ /home/user/faa_data/project_info.csv
 user@sys:~/faa_data$ project_info.csv
 ```
 Linux also allows arguments to be passed to the passed when running from console:
 ```sh
 user@sys:~/faa_data$ faa_eval project_info.csv results
 ```

## Output
**faa_eval** programmatically accesses the FAA check page for each structure in the CSV. Each result page is saved as a `.html` web document, along with ancillary common files. These web documents can be retained as a record and printed to PDF if desired. A result CSV is also generated, providing the structure name and whether or not the result required filing.

It is strongly recommended that every `.html` file be given a review for accuracy of input and representation of the FAA page.

# Issues and Contributions
Please use the "Issues" tab on GitHub to report any problems or bugs. When submitting an issue, include:
 - Steps to reproduce the issue
 - A screenshot or text of the terminal output
 - CSV input data, as available or requested

Note: sharing your CSV data on GitHub will make it publicly visible. Do not post sensitive or client data.
Contributions are welcome.

# License
This software is [released](LICENSE) under the MIT license.