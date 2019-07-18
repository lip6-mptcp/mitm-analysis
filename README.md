We put here the data set of paper "MPTCP Robustness Against Large-Scale Man-in-the-Middle Attacks"
- **_network_** file: is the AS-level  topology  dataset. Each row r  in file is an ASN pair and has the following fields:  **_{ASr1,  ASr2, Vr, Tr}_** where the first two parameters are the AS pair, **Vr** is the metric for the path between the two ASes and is set to **1** for all rows. The last parameter is the type of connection between two ASes: it takes one of the three values:
    *  1 - A connection from an AS to its provider AS
    *  2 - A peering connection
    *  3 - A connection from a provider AS to its client AS

We used the raw file from Internet Research Lab (https://irl.cs.ucla.edu/topology/) described in the paper: "Quantifying the Completeness of the Observed Internet AS-level Structure". Employing measurements over a long period allows us to capture inter-domain connection dynamics as well as inter-AS economic relationships. For instance, in one month, only 85% of inter-AS links appear more than 20 days, the remaining links with a lower frequency of occurrence being those used for backup operations or during BGP convergence periods. For the sake of consistency, we removed these unstable links.". We removed the link with frequency smaller than 20. 

The raw file 
- **_path_diversity.py_**: our source code (in Python) to find the diversity path between  pairs of AS. It uses the "**_network_**" file above as its network topology dataset and get one parameter from command line is file which contains the set of pair AS. The result is written to the file with the same name with input file plus "**_\_result_**" word in extension.   For details on the algorithm, please refer to part III of paper.

 - **_Input directory_**:  Here we put the the 137 countries which we used in our analysis. In each country file is the list of pairs between each AS of a given country to all other ASes.  Each pair is in form: **_{ASi, ASj}_** where **_ASi_** is the AS belonging to a given country and **_ASj_** is the AS not belonging to the country.

 - **_Output 2_** directory: Includes the final statistic of our analysis. The result which contains all the paths between any pair of ASes is too big to be included in this repository, but if you are interested in the this result, please contact us so that we upload it somewhere. For each country, we have 3 files which end with **_\_avg0_**, **_\_avg1_**, **_\_avg2_**.
    *    **_file\_avg0_**: statistics on the path diversity; each row has 2 fields **_{Vi, Ni}_** where **_Vi_** is number of AS pair which has **_Ni_** as path diversity.
    *  **_file\_avg1_** and **_file\_avg2_**: average of the number of paths for each AS pair in a given country and to a destination AS. Each row has 3 fields **_{ASr1, ASr2, Vr}_** where **_ASr1_**, **_ASr2_** is the AS pair and **_Vr_** is the average path diversity from **_(ASr1,ASr2)_** to any AS.  The only difference between **_file\_avg1_** and **_file\_avg2_** is the **_Vr_** field: in **_file\_avg2_** when the **_Vr_** is greater 2, it will be set to 2.
