


# hadith_analysis
Creating a graph-based encoding of the chain of narrations in  کتاب سُليم بن قيس الهلالي


Next Step:
1. Add the graph generation and visualization process
2. Expand the ETL to include all books with under 100 entries


Backlog:
1. Build a daily screenshot job using Mac Automator or crontab
2. Fix the manabe_generator.py to include all sources not just the first 25 elements




references
Extraction and Visualization of the Chain of Narrators from Hadiths using Named Entity Recognition and Classification
https://www.dline.info/jcl/fulltext/v5n1/2.pdf

Trophic Analysis
Shuaib, Choudhry, et al. "Trophic analysis of a historical network reveals temporal information." Applied Network Science 7.1 (2022): 31.

Knowledge Graphs
Kamran, Amna Binte, Bushra Abro, and Amna Basharat. "SemanticHadith: An ontology-driven knowledge graph for the hadith corpus." Journal of Web Semantics 78 (2023): 100797.
Wiharja, Kemas Rahmat Saleh, et al. "A questions answering system on hadith knowledge graph." Journal of ICT Research and Applications 16.2 (2022): 184-196.

Graph-based representation
Alias, Nursyahidah, et al. "Graph-based text representation for Malay translated hadith text." 2016 Third International Conference on Information Retrieval and Knowledge Management (CAMP). IEEE, 2016.
Graphs are everywhere - also in Religious Texts: https://gist.github.com/rvanbruggen/a6e2e80a6fa7a253f46de9fbe9ce361f
Al-Absi, Hamada RH, et al. "Al-Ahadeeth: A Visualization Tool of the Hadiths’ Chain of Narrators." International Conference on Human-Computer Interaction. Cham: Springer Nature Switzerland, 2024.
Farooqi, Aziz Mehmood, et al. "Multi-IsnadSet MIS for Sahih Muslim Hadith with chain of narrators, based on multiple ISNAD." Data in Brief 54 (2024): 110439.
The MIS dataset represents a directed graph that consists of 2092 nodes, representing individual narrators, and 77,797 edges representing the Sanad-Hadith connections. The MIS dataset represents multiple ISNAD of the Hadith based on the Sahih Muslim Hadith book.  four different tools The dataset was carefully extracted from online multiple Hadith sources using data scraping and web crawling techniques tools, providing extensive Hadith details.  four different tools: NetworkX, Neo4j graph database, and two different network analysis tools named Gephi and CytoScape
A Novel Graph-Based Representation for Hadith Sanad
November 2019International Journal of Advanced Trends in Computer Science and Engineering 8(1.5):355-363
DOI:10.30534/ijatcse/2019/5881.52019

variant generation
Reconstructing the Variant Generation Process of Hadith: Based on the Quantitative and the Isnād-cum-Matn Analysis
equinoxpub.com/home/reconstructing-variant-gen/

Data Scraping
Abdallah Namoun, Mohammad Ali Humayun and Waqas Nawaz, “A Multimodal Data Scraping Tool for Collecting Authentic Islamic Text Datasets” International Journal of Advanced Computer Science and Applications(ijacsa), 15(12), 2024. http://dx.doi.org/10.14569/IJACSA.2024.0151224

PageRank Algorithm
Venkat, Ibrahim, et al. "An Adapted Google's PageRank Algorithm for Hadith Sequencing." 2022 International Conference on Digital Transformation and Intelligence (ICDI). IEEE, 2022.

<details>
<summary> genetic algorithms </summary>
 Najeeb, Moath Mustafa Ahmad. "A novel hadith processing approach based on genetic algorithms." IEEE Access 8 (2020): 20233-20244.
</details>



<details>
<summary>Auto ML </summary>
Mohamed, Emad, and Raheem Sarwar. "Linguistic features evaluation for hadith authenticity through automatic machine learning." Digital Scholarship in the Humanities 37.3 (2022): 830-843.
</details>

<details>
<summary>ML</summary>
Sulistio, Bambang, et al. "The utilization of machine learning on studying Hadith in Islam: A systematic literature review." Education and Information Technologies 29.5 (2024): 5381-5419.
</details>

 
<details>
<summary>Supervised classification</summary>
1. Abdelaal, Hammam M., and Hassan A. Youness. "Hadith classification using machine learning techniques according to its reliability." Romanian Journal of Information Science and Technology 22.3 (2019): 259-271.
2. AbdElaal, Hammam M., et al. "Classifications of Hadiths based on Supervised Learning Techniques." International Journal of Computer Science & Network Security 22.11 (2022): 1-10.
3. Binbeshr, Farid, Amirrudin Kamsin, and Manal Mohammed. "A systematic review on hadith authentication and classification methods." Transactions on Asian and Low-Resource Language Information Processing 20.2 (2021): 1-17.
4. Masruroh, Siti Ummi, et al. "Performance Analysis of Naïve Bayes Classifier Algorithm with Chi-Square and Confix Stripping Stemmer Selection Features In Hadits Translation Classification System." 2022 3rd International Conference on Big Data Analytics and Practices (IBDAP). IEEE, 2022.
5. Ramzy, Ahmed, et al. "Hadiths classification using a novel author-based hadith classification dataset (abcd)." Big Data and Cognitive Computing 7.3 (2023): 141.
</details>


<details>
<summary>Deep Learning</summary>
Refaee, Eshrag Ali. "Detecting hadith authenticity using a deep-learning approach." Scientific Journal of King Faisal University Basic and Applied Sciences 23 (2022): 80-84.
</details>

<details>
<summary>Fabricated hadith detection using Transformer Models</summary>
1. Gaanoun, Kamel, and Mohammed Alsuhaibani. "Fabricated hadith detection: A novel matn-based approach with transformer language models." IEEE Access 10 (2022): 113330-113342.
</details>

<details>
<summary>Rules Mining</summary>
Abdelaal, Hammam, et al. "The Relationship between different Classifications of Hadiths Based on rules Mining." International Journal of Advanced Scientific Research and Innovation 6.1 (2023): 90-98.
</details>

<details>
<summary>LSTM</summary>
Rahman, Hendrawan Aulia, and Kemas Muslim Lhaksmana. "Classification of Hadith Quality Based on Matan Using LSTM." 2024 International Conference on Artificial Intelligence, Blockchain, Cloud Computing, and Data Analytics (ICoABCD). IEEE, 2024.
</details>

<details>
<summary>Text Mining</summary>
Hamza, Manar Ahmed Mohammed, et al. "Developing a novel Text mining Model for Exploring Knowledge from an Arabic text: Al-Hadeeth Al-shareef as case study." IJCSNS 20.12 (2020): 51.
</details>


<details>
<summary>BERT</summary>
Khusyasy, Muhammad Luthfi, Moch Arif Bijaksana, and Kemas Muslim Lhaksmana. "Classification of Hadith Authenticity Based on Sanad Using BERT." 2025 International Conference on Advancement in Data Science, E-learning and Information System (ICADEIS). IEEE, 2025.
</details>

 
<details>
<summary>NLP</summary>
1. Azmi, Aqil M., Abdulaziz O. Al-Qabbany, and Amir Hussain. "Computational and natural language processing based studies of hadith literature: a survey." Artificial Intelligence Review 52 (2019): 1369-1414.
2. Ramzy, Ahmed, et al. "Hadiths classification using a novel author-based hadith classification dataset (abcd)." Big Data and Cognitive Computing 7.3 (2023): 141.
</details>
 
<details>
<summary>other</summary>
 1. Azmi, Aqil M., and Amjad M. AlOfaidly. "A novel method to automatically pass hukm on hadith." Proceedings of the 5th International Conference on Arabic Language Processing (CITALA’14). 2014.
 2. bin Rodzman, Shaiful Bakhtiar, et al. "Experiment with text summarization as a positive hierarchical fuzzy logic ranking indicator for domain specific retrieval of Malay translated hadith." 2019 IEEE 9th Symposium on Computer Applications & Industrial Electronics (ISCAIE). IEEE, 2019.
 3. bin Rodzman, Shaiful Bakhtiar, et al. "Domain specific concept ontologies and text summarization as hierarchical fuzzy logic ranking indicator on malay text corpus." Indonesian Journal of Electrical Engineering and Computer Science 15.3 (2019): 1527-1534.
</details>

<details>
 <summary>Isnad Tagging by hidden Markov Models </summary>
 1. Najeeb, Moath Mustafa Ahmad. "A Hidden Markov Model‐Based Tagging Approach for Arabic Isnads of Hadiths." Mathematical Problems in Engineering 2022.1 (2022): 7160509
</details>


<details>
<summary>Using Edge List </summary>
1. Alias, Nursyahidah, et al. "Using Edge List." Fundamental and Applied Sciences in Asia: International Conference on Science Technology and Social Sciences (ICSTSS 2018). Springer Nature, 2023.
 2. Alias, Nursyahidah, et al. "Hadith Text Classification on Sanad Part Using Edge List." Fundamental and Applied Sciences in Asia: International Conference on Science Technology and Social Sciences (ICSTSS 2018). Singapore: Springer Nature Singapore, 2023.
</details>

<details>
<summary>Text Processing Tasks </summary>
Baradaran, Sepideh, et al. "A Review on Hadith Text Processing Tasks." Journal of Information and Communication Technology 59.59 (2024): 47.
</details>


<details>
<summary> Datasets </summary>
1. Mahmoud, S.; Saif, O.; Nabil, E.; Abdeen, M.; ElNainay, M.; Torki, M. AR-Sanad 280K: A Novel 280K Artificial Sanads Dataset for Hadith Narrator Disambiguation. Information 2022, 13, 55. doi.org/10.3390/info13020055
mdpi.com/2078-2489/13/2/55
2. Farooqi, Aziz Mehmood, et al. "Multi-IsnadSet MIS for Sahih Muslim Hadith with chain of narrators, based on multiple ISNAD." Data in Brief 54 (2024): 110439.
doi.org/10.1016/j.dib.2024.110439, Direct URL to data: https://data.mendeley.com/datasets/gzprcr93zn/2, https://www.ihsanetwork.org/hadith.aspx and http://muslimscholars.info/ using the Python Selenium automated agent-based library and Beautiful Soup to acquire the dataset with data wrangling and labeling.
3. Ramzy, Ahmed, et al. "Hadiths classification using a novel author-based hadith classification dataset (abcd)." Big Data and Cognitive Computing 7.3 (2023): 141.
</details>


<details>
<summary>Hadith Map</summary>
 
[IR 2014 HLS Think Big Talk](https://youtu.be/6DQzavdm4xU?si=6gT-vjR-MRTqLkWE&t=693)
</details>


<details>
<summary> Books </summary>
 https://muqith.wordpress.com/wp-content/uploads/2016/03/studiesinhadithmethodologyandliteraturebyshaykhmuhammadmustafaal-azami_text.pdf
</details>


<details>
<summary> علم رجال </summary>
 4 types: Sahih صحیح, Hasan حسن, Za'if ضعیف, Muwasaq مو‍‍ثق documented
 [authenticity categories](https://youtu.be/spfD8LkA8Kc?si=vLpTE5baoM_JNnsq)
</details>



<details>
<summary> </summary>
</details>

