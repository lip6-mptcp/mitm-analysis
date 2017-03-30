We put here the data set of paper ...
- **_network_** file: is the AS-level  topology  dataset. Each row r  in file is one pair of AS and has the following fields:  **_{ASr1,  ASr2, Vr, Tr}_** where the first two parameters are the pair AS, **Vr** is the value of path between two AS and is set to **1** for all row. The last parameter is the type of connection between two AS: it has one of three values:
	1 - A connection from AS to its provider AS
	2 - An peering connection
	3 - A connection from one provider AS to its client AS

- **_ath_diversity.py_**: our source code (in Python) to find the diversity path between  pairs of AS. It uses the "**_network_**" file above as its network topology dataset and get one parameter from command line is file which contains the set of pair AS. The result will be write to the file with the same name with input file plus "**_\_result_**" word in extension.   For detail of algorithm, reference to part III of paper.

 - **_Input directory_**:  Here we put the the 137 countries which we used in our analysis. In each country file is the list of pair between each AS of country to all other AS in the Internet.  Each pair is in form: **_{ASi, ASj}_** where **_ASi_** is the AS belong to country and **_ASj_** is the AS not belong to the country.

 - **_Output 2_** directory: Includes the final statistic of our analysis. The result which contain all the path between any pair of AS is too big to put in github but if you are interested in the this result, we will upload to somewhere. For each country, we have 3 files which end with **_\_avg0_**, **_\_avg1_**, **_\_avg2_**.
    *    **_file\_avg0_**: statistic the number of diversity path, each row has 2 fields **_{Vi, Ni}_** where **_Vi_** is number of pair AS which has **_Ni_** diversity paths
    *  **_file\_avg1_** and **_file\_avg2_**: average the number of path of each pair AS in country to and destination AS in the Internet. Each row has 3 fields **_{ASr1, ASr2, Vr}_** where **_ASr1_**, **_ASr2_** are the pair of AS and **_Vr_** is the average the number of deversity path from **_(ASr1,ASr2)_** to any AS in the Internet.  The only difference between **_file\_avg1_** and **_file\_avg2_** is on **_Vr_** field: in **_file\_avg2_** when the **_Vr_** is greater 2, it will be set to 2.
